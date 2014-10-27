# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.db import models as db
from django.utils.translation import ugettext_lazy as _
from lck.django.choices import Choices
from lck.django.common.models import (
    EditorTrackable,
    Named,
    TimeTrackable,
    WithConcurrentGetOrCreate,
)


class WarehouseType(Choices):
    _ = Choices.Choice
    datacenter = _('Datacenter')
    backoffice = _('Backoffice')


class Warehouse(TimeTrackable, EditorTrackable, Named,
                WithConcurrentGetOrCreate):
    """
    Pricing warehouse model contains name and id from assets and own create
    and modified date
    """
    show_in_report = db.BooleanField(
        verbose_name=_("Show warehouse in report"),
        default=False,
    )
    id_from_assets = db.IntegerField(
        verbose_name=_("Warehouse id from assets"),
        null=False,
        blank=False,
        unique=True,
    )
    type = db.PositiveIntegerField(
        verbose_name=_("Warehouse type"),
        choices=WarehouseType(),
        null=True,
        blank=True,
    )

    class Meta:
        app_label = 'ralph_scrooge'

    def __unicode__(self):
        return self.name
