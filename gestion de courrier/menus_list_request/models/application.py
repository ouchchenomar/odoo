from odoo import models, fields

class Application(models.Model):
    _name = 'menus_list_request.application'
    _description = 'Application'

    name = fields.Char(string='Application Name', required=True)
