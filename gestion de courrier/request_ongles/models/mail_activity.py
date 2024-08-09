from odoo import models, fields, api

class MailActivity(models.Model):
    _inherit = 'mail.activity'

    next_destination = fields.Many2one('res.partner',string="Destination Suivante")
    final_destination = fields.Many2one('res.partner',string="Destination Finale")
    next_destinations = fields.Many2one('res.partner',string="Destinataires Suivantes")
    hierarchical_way = fields.Boolean(string="Voie Hiérarchique")
    echeance = fields.Date(string="Echéance")
    urgence = fields.Selection([
        ('normal', 'Normal'),
        ('urgent', 'Très Urgent')
    ], string="Urgence")
    type_instruction = fields.Selection([
        ('diffusion', 'POUR DIFFUSION'),
        ('other', 'Other')
    ], string="Type Instruction")

    instructions = fields.Text(string="Instructions")

    is_test_activity = fields.Boolean(string='Is Transfer Activity', compute='_compute_is_test_activity')

    @api.depends('activity_type_id')
    def _compute_is_test_activity(self):
        test_activity_type = self.env.ref('request_ongles.mail_activity_type_test')
        for record in self:
            record.is_test_activity = record.activity_type_id == test_activity_type



