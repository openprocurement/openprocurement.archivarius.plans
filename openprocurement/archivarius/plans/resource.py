# -*- coding: utf-8 -*-
import os
from iso8601 import parse_date
from datetime import timedelta

SANDBOX_MODE = os.environ.get('SANDBOX_MODE', False)
TIMEDELTA = timedelta(days=20) if SANDBOX_MODE else timedelta(days=455)


def plan_filter(item, time):
    return parse_date(item.key) < (time - TIMEDELTA)
