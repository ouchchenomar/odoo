import logging
from odoo import models, api

_logger = logging.getLogger(__name__)


class Message(models.Model):
    _inherit = 'mail.message'

    @api.model
    def _get_record_name(self, values):
        """We override this method so that when the
           'generic_request.request_mail_use_special_name'
            setting is set True, the subject of the message sent using
            the message_post() method uses a special name for records
            of the model 'request.request'
        """
        model = values.get('model', self.env.context.get('default_model'))
        use_special_name = self.sudo().env['ir.config_parameter'].get_param(
            'generic_request.request_mail_use_special_name')
        if use_special_name and model == 'request.request':
            return super(
                Message,
                self.with_context(generic_request_use_special_name=True),
            )._get_record_name(values=values)
        return super()._get_record_name(values=values)
