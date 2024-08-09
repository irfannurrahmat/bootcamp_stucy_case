from odoo import models, fields, api
from datetime import timedelta


class TrainCity(models.Model):
    _name = 'train.city'
    _description = 'Train City'
    
    name = fields.Char(string='Name')
    code = fields.Char(string='Code')

class TrainStation(models.Model):
    _name = 'train.station'
    _description = 'Train Station'

    code = fields.Char(string='Code')
    name = fields.Char(string='Name')
    city_id = fields.Many2one('train.city', string='City')
    address = fields.Text(string='Address')

class TrainTrain(models.Model):
    _name = 'train.train'
    _description = 'Train Train'

    name = fields.Char(string='Name')
    code = fields.Char(string='Code')
    capacity = fields.Integer(string='Capacity')
    state = fields.Selection([
        ('ready', 'Ready'),
        ('notready', 'Not Ready'),
        ('maintenance', 'Maintenance')
    ], string='State')
    active = fields.Boolean(string='Active', default=True)
    schedule_line = fields.One2many('train.schedule', 'train_id', string='Schedule')

class TrainSchedule(models.Model):
    _name = 'train.schedule'
    _description = 'Train Schedule'

    code = fields.Char(string='Sequence', readonly=True)
    origin_id = fields.Many2one('train.station', string='Origin', required=True)
    destination_id = fields.Many2one('train.station', string='Destination', required=True)
    schedule_time = fields.Datetime(string='Schedule Time')
    duration = fields.Float(string='Duration')
    arrival_time = fields.Datetime(string='Arrival Time', compute='_compute_arrival', store=True)
    train_id = fields.Many2one('train.train', string='Train', required=True)
    capacity = fields.Integer(string='Capacity', related='train_id.capacity')

    @api.model
    def create(self, vals):
        vals['code'] = self.env['ir.sequence'].next_by_code('train.schedule.seq')
        return super(TrainSchedule, self).create(vals)

    @api.depends('schedule_time', 'duration')
    def _compute_arrival(self):
        for rec in self:
            if rec.arrival_time:
                rec.arrival_time = rec.schedule_time + timedelta(hours=rec.duration)
            else:
                rec.arrival_time = 0
        


