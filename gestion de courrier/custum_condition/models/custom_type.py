from odoo import models, fields

class RequestType(models.Model):
    _inherit = 'request.type'

    condition_ids = fields.Many2many(
        'generic.condition',
        string='Conditions'
    )
