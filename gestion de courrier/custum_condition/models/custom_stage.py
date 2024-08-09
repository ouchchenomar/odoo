from odoo import models, fields,api

class RequestStage(models.Model):
    _inherit = 'request.stage'

    condition_ids = fields.Many2many(
        'generic.condition',
        string='Conditions'
    )

    def get_next_stage(self, conditions):
        # Logique pour obtenir le prochain stage basé sur les conditions
        for route in self.route_ids:
            if all(condition in route.condition_ids for condition in conditions):
                return route.next_stage_id
        return super(RequestStage, self).get_next_stage(conditions)
