from odoo import models, fields

class Activity(models.Model):
    _name = 'menus_list_request.activity'
    _description = 'Activity'

    name = fields.Char(string='Activity Name', required=True)
