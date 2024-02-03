# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dispatch/sdk/v1/executor.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2

from dispatch.sdk.v1 import status_pb2 as dispatch_dot_sdk_dot_v1_dot_status__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1e\x64ispatch/sdk/v1/executor.proto\x12\x0f\x64ispatch.sdk.v1\x1a\x1c\x64ispatch/sdk/v1/status.proto\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/duration.proto"\xe3\x01\n\x0e\x45xecuteRequest\x12#\n\rcoroutine_uri\x18\x01 \x01(\tR\x0c\x63oroutineUri\x12+\n\x11\x63oroutine_version\x18\x02 \x01(\tR\x10\x63oroutineVersion\x12,\n\x05input\x18\x03 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00R\x05input\x12\x44\n\rpoll_response\x18\x04 \x01(\x0b\x32\x1d.dispatch.sdk.v1.PollResponseH\x00R\x0cpollResponseB\x0b\n\tcoroutine"\xfb\x01\n\x0f\x45xecuteResponse\x12#\n\rcoroutine_uri\x18\x01 \x01(\tR\x0c\x63oroutineUri\x12+\n\x11\x63oroutine_version\x18\x02 \x01(\tR\x10\x63oroutineVersion\x12/\n\x06status\x18\x03 \x01(\x0e\x32\x17.dispatch.sdk.v1.StatusR\x06status\x12+\n\x04\x65xit\x18\x04 \x01(\x0b\x32\x15.dispatch.sdk.v1.ExitH\x00R\x04\x65xit\x12+\n\x04poll\x18\x05 \x01(\x0b\x32\x15.dispatch.sdk.v1.PollH\x00R\x04pollB\x0b\n\tdirective"k\n\x04\x45xit\x12/\n\x06result\x18\x01 \x01(\x0b\x32\x17.dispatch.sdk.v1.ResultR\x06result\x12\x32\n\ttail_call\x18\x02 \x01(\x0b\x32\x15.dispatch.sdk.v1.CallR\x08tailCall"d\n\x06Result\x12,\n\x06output\x18\x03 \x01(\x0b\x32\x14.google.protobuf.AnyR\x06output\x12,\n\x05\x65rror\x18\x05 \x01(\x0b\x32\x16.dispatch.sdk.v1.ErrorR\x05\x65rror"5\n\x05\x45rror\x12\x12\n\x04type\x18\x01 \x01(\tR\x04type\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message"\xa0\x01\n\x04Poll\x12\x14\n\x05state\x18\x01 \x01(\x0cR\x05state\x12+\n\x05\x63\x61lls\x18\x02 \x03(\x0b\x32\x15.dispatch.sdk.v1.CallR\x05\x63\x61lls\x12\x34\n\x08max_wait\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationR\x07maxWait\x12\x1f\n\x0bmax_results\x18\x04 \x01(\x05R\nmaxResults"[\n\x0cPollResponse\x12\x14\n\x05state\x18\x01 \x01(\x0cR\x05state\x12\x35\n\x07results\x18\x02 \x03(\x0b\x32\x1b.dispatch.sdk.v1.CallResultR\x07results"\xab\x01\n\x04\x43\x61ll\x12#\n\rcoroutine_uri\x18\x01 \x01(\tR\x0c\x63oroutineUri\x12+\n\x11\x63oroutine_version\x18\x02 \x01(\tR\x10\x63oroutineVersion\x12%\n\x0e\x63orrelation_id\x18\x03 \x01(\x04R\rcorrelationId\x12*\n\x05input\x18\x04 \x01(\x0b\x32\x14.google.protobuf.AnyR\x05input"\xb6\x01\n\nCallResult\x12#\n\rcoroutine_uri\x18\x01 \x01(\tR\x0c\x63oroutineUri\x12+\n\x11\x63oroutine_version\x18\x02 \x01(\tR\x10\x63oroutineVersion\x12%\n\x0e\x63orrelation_id\x18\x03 \x01(\x04R\rcorrelationId\x12/\n\x06result\x18\x04 \x01(\x0b\x32\x17.dispatch.sdk.v1.ResultR\x06result2a\n\x0f\x45xecutorService\x12N\n\x07\x45xecute\x12\x1f.dispatch.sdk.v1.ExecuteRequest\x1a .dispatch.sdk.v1.ExecuteResponse"\x00\x42\x82\x01\n\x13\x63om.dispatch.sdk.v1B\rExecutorProtoP\x01\xa2\x02\x03\x44SX\xaa\x02\x0f\x44ispatch.Sdk.V1\xca\x02\x0f\x44ispatch\\Sdk\\V1\xe2\x02\x1b\x44ispatch\\Sdk\\V1\\GPBMetadata\xea\x02\x11\x44ispatch::Sdk::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "dispatch.sdk.v1.executor_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals["DESCRIPTOR"]._serialized_options = (
        b"\n\023com.dispatch.sdk.v1B\rExecutorProtoP\001\242\002\003DSX\252\002\017Dispatch.Sdk.V1\312\002\017Dispatch\\Sdk\\V1\342\002\033Dispatch\\Sdk\\V1\\GPBMetadata\352\002\021Dispatch::Sdk::V1"
    )
    _globals["_EXECUTEREQUEST"]._serialized_start = 141
    _globals["_EXECUTEREQUEST"]._serialized_end = 368
    _globals["_EXECUTERESPONSE"]._serialized_start = 371
    _globals["_EXECUTERESPONSE"]._serialized_end = 622
    _globals["_EXIT"]._serialized_start = 624
    _globals["_EXIT"]._serialized_end = 731
    _globals["_RESULT"]._serialized_start = 733
    _globals["_RESULT"]._serialized_end = 833
    _globals["_ERROR"]._serialized_start = 835
    _globals["_ERROR"]._serialized_end = 888
    _globals["_POLL"]._serialized_start = 891
    _globals["_POLL"]._serialized_end = 1051
    _globals["_POLLRESPONSE"]._serialized_start = 1053
    _globals["_POLLRESPONSE"]._serialized_end = 1144
    _globals["_CALL"]._serialized_start = 1147
    _globals["_CALL"]._serialized_end = 1318
    _globals["_CALLRESULT"]._serialized_start = 1321
    _globals["_CALLRESULT"]._serialized_end = 1503
    _globals["_EXECUTORSERVICE"]._serialized_start = 1505
    _globals["_EXECUTORSERVICE"]._serialized_end = 1602
# @@protoc_insertion_point(module_scope)
