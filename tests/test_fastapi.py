import pickle
import unittest
from typing import Any
import dispatch.coroutine
from dispatch.coroutine import Input, Output
import dispatch.fastapi
import fastapi
from fastapi.testclient import TestClient
import google.protobuf.wrappers_pb2
import ring.coroutine.v1.coroutine_pb2
from . import executor_service


class TestFastAPI(unittest.TestCase):
    def test_configure(self):
        app = fastapi.FastAPI()

        dispatch.fastapi.configure(app, api_key="test-key")

        @app.get("/")
        def read_root():
            return {"Hello": "World"}

        client = TestClient(app)

        # Ensure existing routes are still working.
        resp = client.get("/")
        self.assertEqual(resp.status_code, 200)

        # Ensure Dispatch root is working.
        resp = client.get("/dispatch/")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.text, "ok")

    def test_configure_no_app(self):
        with self.assertRaises(ValueError):
            dispatch.fastapi.configure(None, api_key="test-key")

    def test_configure_no_api_key(self):
        app = fastapi.FastAPI()
        with self.assertRaises(ValueError):
            dispatch.fastapi.configure(app, api_key=None)

    def test_configure_no_mount_path(self):
        app = fastapi.FastAPI()
        with self.assertRaises(ValueError):
            dispatch.fastapi.configure(app, api_key="test-key", mount_path=None)

    def test_fastapi_simple_request(self):
        app = dispatch.fastapi._new_app()

        @app.dispatch_coroutine()
        def my_cool_coroutine(input: Input) -> Output:
            return Output.value(
                f"You told me: '{input.input}' ({len(input.input)} characters)"
            )

        http_client = TestClient(app)

        client = executor_service.client(http_client)

        pickled = pickle.dumps("Hello World!")
        input_any = google.protobuf.any_pb2.Any()
        input_any.Pack(google.protobuf.wrappers_pb2.BytesValue(value=pickled))

        req = ring.coroutine.v1.coroutine_pb2.ExecuteRequest(
            coroutine_uri=my_cool_coroutine.__qualname__,
            coroutine_version="1",
            input=input_any,
        )

        resp = client.Execute(req)

        self.assertIsInstance(resp, ring.coroutine.v1.coroutine_pb2.ExecuteResponse)
        self.assertEqual(resp.coroutine_uri, req.coroutine_uri)
        self.assertEqual(resp.coroutine_version, req.coroutine_version)

        resp.exit.result.output.Unpack(
            output_bytes := google.protobuf.wrappers_pb2.BytesValue()
        )
        output = pickle.loads(output_bytes.value)

        self.assertEqual(output, "You told me: 'Hello World!' (12 characters)")


def response_output(resp: ring.coroutine.v1.coroutine_pb2.ExecuteResponse) -> Any:
    resp.exit.result.output.Unpack(
        output_bytes := google.protobuf.wrappers_pb2.BytesValue()
    )
    return pickle.loads(output_bytes.value)


class TestCoroutine(unittest.TestCase):
    def setUp(self):
        self.app = dispatch.fastapi._new_app()
        http_client = TestClient(self.app)
        self.client = executor_service.client(http_client)

    def execute(
        self, coroutine, input=None, state=None
    ) -> ring.coroutine.v1.coroutine_pb2.ExecuteResponse:
        """Test helper to invoke coroutines on the local server."""
        req = ring.coroutine.v1.coroutine_pb2.ExecuteRequest(
            coroutine_uri=coroutine.__qualname__,
            coroutine_version="1",
        )

        if input is not None:
            input_bytes = pickle.dumps(input)
            input_any = google.protobuf.any_pb2.Any()
            input_any.Pack(google.protobuf.wrappers_pb2.BytesValue(value=input_bytes))
            req.input.CopyFrom(input_any)
        if state is not None:
            print("SENDING BACK STATE: ", state)
            req.poll_response.state = state

        resp = self.client.Execute(req)
        self.assertIsInstance(resp, ring.coroutine.v1.coroutine_pb2.ExecuteResponse)
        return resp

    def test_no_input(self):
        @self.app.dispatch_coroutine()
        def my_cool_coroutine(input: Input) -> Output:
            return Output.value("Hello World!")

        resp = self.execute(my_cool_coroutine)
        out = response_output(resp)
        self.assertEqual(out, "Hello World!")

    def test_string_input(self):
        @self.app.dispatch_coroutine()
        def my_cool_coroutine(input: Input) -> Output:
            return Output.value(f"You sent '{input.input}'")

        resp = self.execute(my_cool_coroutine, input="cool stuff")
        out = response_output(resp)
        self.assertEqual(out, "You sent 'cool stuff'")

    def test_two_simple_coroutines(self):
        @self.app.dispatch_coroutine()
        def echoroutine(input: Input) -> Output:
            return Output.value(f"Echo: '{input.input}'")

        @self.app.dispatch_coroutine()
        def len_coroutine(input: Input) -> Output:
            return Output.value(f"Length: {len(input.input)}")

        data = "cool stuff"
        resp = self.execute(echoroutine, input=data)
        out = response_output(resp)
        self.assertEqual(out, "Echo: 'cool stuff'")

        resp = self.execute(len_coroutine, input=data)
        out = response_output(resp)
        self.assertEqual(out, "Length: 10")

    def test_coroutine_with_state(self):
        @self.app.dispatch_coroutine()
        def coroutine3(input: Input) -> Output:
            if input.is_first_call:
                counter = input.input
            else:
                counter = input.state
            counter -= 1
            if counter <= 0:
                return Output.value("done")
            return Output.callback(state=counter)

        # first call
        resp = self.execute(coroutine3, input=4)
        state = resp.poll.state
        self.assertTrue(len(state) > 0)

        # resume, state = 3
        resp = self.execute(coroutine3, state=state)
        state = resp.poll.state
        self.assertTrue(len(state) > 0)

        # resume, state = 2
        resp = self.execute(coroutine3, state=state)
        state = resp.poll.state
        self.assertTrue(len(state) > 0)

        # resume, state = 1
        resp = self.execute(coroutine3, state=state)
        state = resp.poll.state
        self.assertTrue(len(state) == 0)
        out = response_output(resp)
        self.assertEqual(out, "done")
