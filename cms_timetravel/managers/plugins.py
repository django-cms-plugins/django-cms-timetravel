from django.core.exceptions import ValidationError

from cms.models import CMSPlugin
from cms.models.placeholdermodel import Placeholder
from cms.plugin_rendering import PluginContext, render_plugin as _render_plugin

from ..utils import get_timetravel_date
from ..models import Schedulable


def render_plugin(self, context=None, placeholder=None, admin=False, processors=None):
    instance, plugin = self.get_plugin_instance()
    if instance and not (admin and not plugin.admin_preview):
        if not self.published():
            return ""

        if not isinstance(placeholder, Placeholder):
            placeholder = instance.placeholder
        placeholder_slot = placeholder.slot
        context = PluginContext(context, instance, placeholder)
        context = plugin.render(context, instance, placeholder_slot)
        if plugin.render_plugin:
            template = hasattr(instance, 'render_template') and instance.render_template or plugin.render_template
            if not template:
                raise ValidationError("plugin has no render_template: %s" % plugin.__class__)
        else:
            template = None
        return _render_plugin(context, instance, placeholder, template, processors)
    return ""


def published(self):
        """
        Checks if the plugin should be published, depending on the publication
        start and/or end date (if available).
        """
        ref_date = get_timetravel_date()
        instance, plugin = self.get_plugin_instance()
        if isinstance(instance, Schedulable):
            return (instance.publication_date is None or instance.publication_date < ref_date) and \
                (instance.publication_end_date is None or instance.publication_end_date >= ref_date)
        else:
            return True

CMSPlugin.published = published
CMSPlugin.render_plugin = render_plugin
