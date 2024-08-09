from odoo import api, fields, models

class ScheduleWizard(models.Model):
    _name = 'schedule.wizard'
    description = 'Schedule Wizard'

    def _default_sesi(self):
        return self.env['train.train'].browse(self._context.get('active_ids'))
 
    train_id = fields.Many2one('train.train', string="Sesi", default=_default_sesi)
    schedule_ids = fields.Many2many('train.schedule', string='Schedule')
    train_ids = fields.Many2many('train.train', string="Sesi", default=_default_sesi)

    def add_schedule(self):
        self.train_id.schedule_ids |= self.schedule_line

    def add_more_schedule(self):
        for sesi in self.train_ids:
            sesi.schedule_ids |= self.schedule_line
