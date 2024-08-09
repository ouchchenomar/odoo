from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class RequestRequest(models.Model):
    _inherit = 'request.request'

    test_condition_ids = fields.Many2many(
        'generic.condition',
        string='Test Conditions'
    )
    test_result = fields.Text(
        string='Test Result',
        readonly=True
    )

    is_fail = fields.Boolean(string='Fail', compute='_compute_test_result')
    is_true = fields.Boolean(string='True', compute='_compute_test_result')
    is_unknown = fields.Boolean(string='Unknown', compute='_compute_test_result')

    @api.depends('test_result')
    def _compute_test_result(self):
        for record in self:
            _logger.info(f"Computing test result for record: {record.id} with test_result: {record.test_result}")
            record.is_fail = record.test_result == 'Toutes les conditions ne sont pas remplies.'
            record.is_true = record.test_result == 'Toutes les conditions sont remplies. La demande est passée à l\'état suivant.'
            record.is_unknown = record.test_result == 'Les conditions sont remplies mais aucun état suivant n\'a été trouvé.'
            _logger.info(f"Results - is_fail: {record.is_fail}, is_true: {record.is_true}, is_unknown: {record.is_unknown}")

    def action_open_generic_condition_test(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Test Condition',
            'res_model': 'generic.condition.test_condition',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
            'views': [(self.env.ref('generic_condition.generic_condition_test_wizard_form').id, 'form')],
            'context': self.env.context,
        }

    def button_test_conditions(self):
        conditions_met = all(condition in self.stage_id.condition_ids for condition in self.test_condition_ids)
        if conditions_met:
            next_stage = self.stage_id.get_next_stage(self.test_condition_ids)
            if next_stage:
                self.write({'stage_id': next_stage.id})
                message = 'Toutes les conditions sont remplies. La demande est passée à l\'état suivant.'
                notification_type = 'success'
            else:
                message = 'Les conditions sont remplies mais aucun état suivant n\'a été trouvé.'
                notification_type = 'warning'
        else:
            message = 'Toutes les conditions ne sont pas remplies.'
            notification_type = 'danger'

        self.write({'test_result': message})
        self._compute_test_result()

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Test des Conditions',
                'message': message,
                'type': notification_type,
                'sticky': False,
            }
        }
