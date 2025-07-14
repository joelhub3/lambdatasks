from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class AWSContext:
    """
    Documents the type of the context passed to each lambda.
    """

    get_remaining_time_in_millis: Callable[[], int]
    function_name: str
    function_version: str
    invoked_function_arn: str
    memory_limit_in_mb: int
    aws_request_id: str
    log_group_name: str
    log_stream_name: str
