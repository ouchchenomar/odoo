from odoo.addons.generic_mixin.tools.sql import unlink_view
from odoo.addons.generic_mixin.tools.migration_utils import ensure_version


@ensure_version('1.126.0')
def migrate(cr, installed_version):
    unlink_view(
        cr, 'crnd_wsd.generic_request_res_config_settings_view_form')
    unlink_view(
        cr, 'crnd_wsd.generic_request_website_res_config_settings_view_form')
