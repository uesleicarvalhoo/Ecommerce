from datetime import datetime

from pytz import timezone

DEFAULT_TIMEZONE = timezone("America/Sao_Paulo")


def get_now_datetime(tz: timezone = DEFAULT_TIMEZONE) -> datetime:
    return datetime.now(tz=tz)
