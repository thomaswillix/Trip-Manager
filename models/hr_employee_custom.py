from odoo import models, fields
# -*- coding: utf-8 -*-

class HrEmployeeCustom(models.Model):
    _inherit = 'hr.employee'
    
    trips_ids = fields.Many2many('tfs_trip_manager.trip', string='Trips')
