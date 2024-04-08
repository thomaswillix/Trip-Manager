# -*- coding: utf-8 -*-

from odoo import models, fields

class TripPhase(models.Model):
    _name = 'tfs_trip_manager.trip_phase'
    _description = 'Trip phase'

    name = fields.Char(string='Name of the phase', required=True)
    _rec_name = "name"
    description = fields.Text(string='Description')
    state = fields.Selection([
        ('0', 'Pending'),
        ('1', 'In progress'),
        ('2', 'Completed')
    ], string='State', default='0', required=True)
    trip_id = fields.Many2one('tfs_trip_manager.trip', string='Trip', required=True)
