from hyde.plugin import Plugin

from gfm import gfm

# Add any other custom Jinja2 filters here
filters = {
    "gfm": gfm
}

class CustomFilterPlugin(Plugin):
    def __init__(self, site):
        super(CustomFilterPlugin, self).__init__(site)

    def template_loaded(self, template):
        super(CustomFilterPlugin, self).template_loaded(template)
        self.template.env.filters.update(filters)