from datetime import datetime, timezone as tz


class Analytics:
    def __init__(self):
        pass

    def log_event(action: str, success: bool, **kwargs: dict[str, str]):
        msg = ' '.join([
            f'now="{datetime.now(tz=tz.utc)}"',
            f'action="{action}"',
            f'success="{success}"',
            *[f'{k}="{v}"' for k, v in kwargs.items()],
        ])
        print(f"::Analytics:: {msg}")
