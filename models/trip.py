# -*- coding: utf-8 -*-

from odoo import api, models, fields
from odoo.exceptions import ValidationError

class Trip(models.Model):
    _name = 'tfs_trip_manager.trip'
    _description = 'Trip'

    color = fields.Integer(default = '0')
    image = fields.Binary(string='Foto del viaje')
    start_date = fields.Date(string= 'Start date', default=fields.Date.today(), required=True)
    end_date = fields.Date(string = 'End date', required=True)
    destination = fields.Char(string='Destination', required=True)
    _rec_name = "destination"
    motive = fields.Text(string='Motive',required=True)
    state = fields.Selection([
        ('0', 'Canceled'),
        ('1', 'Pending'),
        ('2', 'Approved'),
        ('3', 'In course'),
        ('4', 'Completed')       
    ], string='State', default='1', required=True)
    employees_ids = fields.Many2many('hr.employee', string='Employees')
    trip_phases_ids = fields.One2many('tfs_trip_manager.trip_phase', 'trip_id',string='Phases')
    trip_expenses_ids = fields.One2many('tfs_trip_manager.trip_expense', 'trip_id', string='Expenses')
    trip_progress_ids = fields.One2many('tfs_trip_manager.trip_progress', 'trip_id', string='Progress')

    @api.constrains('color')
    def _check_color(self):
        for record in self:
            if record.color < 0:
                raise ValidationError("The color cannot be lower than 0")

    @api.constrains('end_date')
    def _check_date_end(self):
        for record in self:
            if record.end_date < record.start_date:
                raise ValidationError("The end date cannot be set before the start date")

            
    
