# -*- coding: utf-8 -*-
from iso8601 import parse_date
from datetime import timedelta

TIMEDELTA = timedelta(days=455)


def plan_filter(item, time):
    return parse_date(item.key) < (time - TIMEDELTA)
