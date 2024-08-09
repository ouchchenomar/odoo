from odoo import models, fields

class Dossier(models.Model):
    _name = 'menus_list_request.dossier'
    _description = 'Dossier'

    name = fields.Char(string='Dossier Name', required=True)
