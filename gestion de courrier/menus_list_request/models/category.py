from odoo import models, fields

class Category(models.Model):
    _name = 'menus_list_request.category'
    _description = 'Category'

    name = fields.Char(string='Category Name', required=True)
