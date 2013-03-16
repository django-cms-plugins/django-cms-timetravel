from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import TimetravelPlugin


class CMSTimetravelPlugin(CMSPluginBase):
    model = TimetravelPlugin
    name = 'Timetravel Plugin'
    render_template = 'plugin.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(CMSTimetravelPlugin)
