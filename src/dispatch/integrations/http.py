from dispatch.status import Status


def http_response_code_status(code: int) -> Status:
    """Returns a Status that's broadly equivalent to an HTTP response
    status code."""
    match code:
        case 429:  # Too Many Requests
            return Status.THROTTLED
        case 501:  # Not Implemented
            return Status.PERMANENT_ERROR

    category = code // 100
    match category:
        case 1:  # 1xx informational
            return Status.PERMANENT_ERROR
        case 2:  # 2xx success
            return Status.OK
        case 3:  # 3xx redirection
            return Status.PERMANENT_ERROR
        case 4:  # 4xx client error
            return Status.PERMANENT_ERROR
        case 5:  # 5xx server error
            return Status.TEMPORARY_ERROR

    return Status.UNSPECIFIED
