"""
These contain small helpers to ensure that we always respond to lambdas in the expected format.
"""

def success(msg: str):
    return {
        "statusCode": 200,
        "body": msg
    }


def bad_input(msg: str):
    return {
        "statusCode": 400,
        "body": msg
    }


def failed(msg: str):
    return {
        "statusCode": 500,
        "body": msg
    }
