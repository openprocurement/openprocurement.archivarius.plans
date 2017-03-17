# -*- coding: utf-8 -*-
import os
import webtest
from openprocurement.planning.api.tests.base import BasePlanWebTest, PrefixedRequestClass


class BasePlanArchivariusWebTest(BasePlanWebTest):

    def setUp(self):
        self.app = webtest.TestApp(
            "config:tests.ini", relative_to=os.path.dirname(__file__))
        self.app.RequestClass = PrefixedRequestClass
        self.app.authorization = ('Basic', ('token', ''))
        self.couchdb_server = self.app.app.registry.couchdb_server
        self.db = self.app.app.registry.db
        if self.docservice:
            self.setUpDS()
        self.create_plan()
