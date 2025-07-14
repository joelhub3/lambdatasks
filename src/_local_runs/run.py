from lambdas import onboard_user
from custom_types.aws_context import AWSContext


def dummy_aws_context():
    return AWSContext(
        get_remaining_time_in_millis=lambda: 60_000,
        function_name='demo-context',
        function_version='1',
        invoked_function_arn='arn:local:lambda:invocation',
        memory_limit_in_mb=1024,
        aws_request_id='112233',
        log_group_name='local-lambda-logs',
        log_stream_name='lll-123',
    )


def test_onboard_user_event():
    return {
        "system_id": "0ee21120-c610-442f-a12b-bd6aeda15db8",
        "first_name": "John",
        "last_name": "Jingleheimer-Schmidt",
        "middle_name": "Jacob",
        "preferred_username": "JazzyJeff",
        "related_accounts": [
            {
                "id": "a1",
                "user_description": "my only account"
            }
        ],
        "contact_info": {
            "preferred_language": "en-US",
            "email": "john@jjclan.fam",
            "address": None,
            "phone": None,
        },
        "payment_id": "69395728-8b88-4c2f-8559-19ce4e121fd2",
    }


def main():
    print("Starting test run")
    try:
        result = onboard_user.lambda_handler(
            test_onboard_user_event(),
            dummy_aws_context()
        )
        print(result)
    except Exception as e:
        print(f"Got an exception trying to run lambda: {e}")

    print("Done!")


if __name__ == '__main__':
    main()
