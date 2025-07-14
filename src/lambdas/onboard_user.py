import logging

from pydantic import ValidationError

from integrations.backend import Backend
from integrations.analytics import Analytics

from custom_types.aws_context import AWSContext
from lib.response_codes import bad_input, success, failed
from lib.password_generator import random_temporary_password
from custom_types.onboard_user_event import OnboardUserEventRoot


def lambda_handler(event: dict, context: AWSContext):
    try:
        onboard_event = OnboardUserEventRoot.parse_obj(event)

        succeeded = add_user_to_backend(onboard_event)
        if succeeded:
            return success("onboarding complete")
        else:
            return failed("Unable to onboard user")
    except ValidationError as e:
        logging.error(f"Unexpected event shape: {e}.  Exiting...")
        return bad_input("Unexpected message format")


def add_user_to_backend(user_event: OnboardUserEventRoot) -> bool:
    be = Backend()

    succeeded, user = be.add_user(
        {
            "name": user_event.first_name + " " + user_event.last_name,
            "email": user_event.contact_info.email.lower().strip(),
            "external_id": user_event.system_id,
            "payment_id": user_event.payment_id,
            "password": random_temporary_password()
        }
    )

    a = Analytics()
    if succeeded:
        a.log_event("ADD_USER", True, user_id=user.user_id, username=user.username)
        return True
    
    a.log_event("ADD_USER", False)
    return False
