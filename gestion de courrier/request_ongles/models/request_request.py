from odoo import models, fields, api

class RequestRequest(models.Model):
    _name = 'request.request'
    _inherit = 'request.request'

    ref_bo = fields.Char(string="Réf BO")
    document=fields.Char(string="document attaché")

    date_saisie = fields.Datetime(string="Date de saisie", default=lambda self: fields.Datetime.now())
    org = fields.Many2one('res.partner', string="Orge")
    date_reception = fields.Date(string="Date de réception")
    application = fields.Many2one('menus_list_request.application',string="Application")
    expediteur = fields.Many2one('res.partner', string="Expéditeur")
    categorie = fields.Many2one('menus_list_request.category',string="Catégorie")
    autre_expediteur = fields.Many2one('res.partner', string="Autre Expéditeur")
    activite = fields.Many2one('menus_list_request.activity',string="Activité")
    dossier = fields.Many2one('menus_list_request.dossier',string="Dossier")

    recu_par = fields.Many2one('hr.employee', string="Reçu par")
    mode_reception = fields.Selection([
        ('fax', 'FAX'),
        ('chronopost', 'CHRONOPOST'),
        ('courier', 'COURIER'),
        ('recommande', 'RECOMMANDE'),
        ('bordereau', 'BORDEREAU D\'ENVOIE')
    ], string="Mode de réception")
    entite_destinataire = fields.Many2one('hr.department', string="Entité destinataire")
    objet = fields.Text(string="Objet")
    nombre_pieces_jointes = fields.Integer(string="Nombre des Pièces jointes", compute='_compute_nombre_pieces_jointes', store=True)

    attachment_ids = fields.Many2many(
        'ir.attachment', 'request_request_attachment_rel',
        'request_id', 'attachment_id',
        string="Attachments"
    )

    transfer_activity_ids = fields.One2many(
        'mail.activity', 'res_id',
        string="Transfer Activities"
    )


    transfer_activity_ids = fields.One2many('mail.activity', 'res_id', string="Transfer Activities", domain=[('res_model', '=', 'request.request')])

    def action_open_activity_form(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Create Activity',
            'res_model': 'mail.activity',
            'view_mode': 'form',
            'view_id': False,
            'target': 'new',
            'context': {
                'default_res_id': self.id,
                'default_res_model': self._name,
            },
        }

    @api.depends('attachment_ids')
    def _compute_nombre_pieces_jointes(self):
        for record in self:
            record.nombre_pieces_jointes = len(record.attachment_ids)

