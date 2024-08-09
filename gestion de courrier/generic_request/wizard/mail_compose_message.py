from odoo import models, api


class MailComposer(models.TransientModel):
    _inherit = 'mail.compose.message'

    @api.model
    def get_record_data(self, values):
        """We override this method so that when the
           'generic_request.request_mail_use_special_name'
            setting is set True, the subject of the message sent using
            the message composer uses a special name for records
            of the model 'request.request'
        """
        model = values.get('model')
        use_special_name = self.sudo().env['ir.config_parameter'].get_param(
            'generic_request.request_mail_use_special_name')
        if (use_special_name
                and model == 'request.request' and values.get('res_id')):
            return super(
                MailComposer,
                self.with_context(generic_request_use_special_name=True),
            ).get_record_data(values=values)
        return super(MailComposer, self).get_record_data(values=values)
