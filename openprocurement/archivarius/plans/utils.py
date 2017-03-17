# -*- coding: utf-8 -*-

from openprocurement.archivarius.core.utils import Root


def factory(request):
    request.validated['plan_src'] = {}
    root = Root(request)
    if not request.matchdict or not request.matchdict.get('plan_id'):
        return root
    request.validated['plan_id'] = request.matchdict['plan_id']
    plan = request.plan
    plan.__parent__ = root
    request.validated['plan'] = request.validated['db_doc'] = plan
    return plan
