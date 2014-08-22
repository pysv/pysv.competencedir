# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from plone.theme.interfaces import IDefaultPloneLayer
from plone.supermodel import model


class IPysvCompetencedirLayer(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer."""


class ICompetenceDir(model.Schema):
    model.load("models/pysv_competencedir.xml")


class ICompetenceDirEntry(model.Schema):
    model.load("models/pysv_competencedir_entry.xml")
