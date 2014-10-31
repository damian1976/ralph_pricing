#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework.response import Response


class Menu(APIView):
    def get(self, request, format=None):
        return Response([
            {
                'name': 'Components',
                'href': '#/components/',
                'leftMenu': ['services'],
            },
            {
                'name': 'Allocations',
                'href': '#/allocation/client/',
                'leftMenu': ['services', 'teams'],
            },
            {
                'name': 'Allocations Admin',
                'href': '/scrooge/services-usages-report/',
                'leftMenu': [],
            }
        ])
