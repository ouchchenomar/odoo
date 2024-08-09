from odoo import models, fields,api
class RequestStageRoute(models.Model):
    _inherit = 'request.stage.route'

    condition_ids = fields.Many2many(
        'generic.condition',
        string='Conditions'
    )

    next_stage_id = fields.Many2one(
        'request.stage',
        string='Next Stage'
    )
