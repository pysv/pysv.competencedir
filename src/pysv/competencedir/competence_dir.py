from zope.interface import implements
from plone.dexterity.content import Container

from interfaces import (
    ICompetenceDir, ICompetenceDirEntry)


class CompetenceDir(Container):
    """
    """
    implements(ICompetenceDir)


class CompetenceDirEntry(Container):
    """
    """
    implements(ICompetenceDirEntry)
