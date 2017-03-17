# -*- coding: utf-8 -*-
from openprocurement.planning.api.utils import opresource
from openprocurement.archivarius.core.utils import ArchivariusResource
from openprocurement.archivarius.plans.utils import factory


@opresource(name='Plan Archivarius',
                     path='/plans/{plan_id}/dump',
                     description="Plan Archivarius View",
                     factory=factory)
class PlanArchivariusResource(ArchivariusResource):

    pass
