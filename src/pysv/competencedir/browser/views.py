from Products.Five.browser import BrowserView
from plone import api


class CompetenceDirEntries(BrowserView):

    def __call__(self):
        # FIXME: use plone.api methods here:
        return self.index()

    def get_items(self):
        searchable_text = self.request.get('SearchableText', '')
        if not searchable_text:
            return self.index()
        catalog = api.portal.get_tool(name='portal_catalog')
        query = {}
        query["portal_type"] = "pysv_competencedir_entry"
        query["path"] = "/".join(self.context.getPhysicalPath())
        if searchable_text:
            query["SearchableText"] = searchable_text
        entries = catalog(query)
        return entries
