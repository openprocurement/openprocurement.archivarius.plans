# -*- coding: utf-8 -*-
from iso8601 import parse_date
from datetime import timedelta

TIMEDELTA = timedelta(days=30)


def plan_filter(item, time):
    return parse_date(item.key) < (time - TIMEDELTA)
