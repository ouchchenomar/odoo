from odoo import models, fields, api

class GenericConditionTestCondition(models.TransientModel):
    _inherit = 'generic.condition.test_condition'
    _description = 'Test Condition Wizard'

    condition_id = fields.Many2one('generic.condition', string='Condition')
    res_model = fields.Char(string='Model Name')
    res_id = fields.Integer(string='Record ID')
    test_as_user_id = fields.Many2one('res.users', string='Test As User')

    @api.model
    def default_get(self, fields_list):
        res = super(GenericConditionTestCondition, self).default_get(fields_list)
        context = self._context
        res['res_model'] = context.get('default_res_model')
        res['res_id'] = context.get('default_res_id')
        return res

    def process(self):
        record = self.env[self.res_model].browse(self.res_id)
        if record:
            record.button_test_conditions()
        return {'type': 'ir.actions.act_window_close'}
