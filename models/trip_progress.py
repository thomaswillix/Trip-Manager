# -*- coding: utf-8 -*-

from odoo import models, fields

class TripProgress(models.Model):
    _name = 'tfs_trip_manager.trip_progress'
    _description = 'Progress track'

    name = fields.Char(string='Name of the task', required=True)
    _rec_name = "name"
    description = fields.Text(string='Description of the task')
    state = fields.Selection([
        ('0', 'Pending'),
        ('1', 'In progress'),
        ('2', 'Completed')
    ], string='State', default='0', required=True)
    trip_id = fields.Many2one('tfs_trip_manager.trip', string='Trip', required=True)
