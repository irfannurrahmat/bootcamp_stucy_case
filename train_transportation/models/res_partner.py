from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    train_state = fields.Selection([
        ('passenger', 'Passengger'),
        ('machinist', 'Machinist'),
    ], string='Train State')
    identity = fields.Char(string='Identity')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string='Gender')
    born_date = fields.Date(string='Born Date')