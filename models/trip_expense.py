# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TripExpenses(models.Model):
    _name = 'tfs_trip_manager.trip_expense'
    _description = 'Expenses associated'

    name = fields.Char(string='Expense', required=True)
    _rec_name = "name"
    description = fields.Text(string='Description', required=True)
    amount = fields.Float(string='Amount', required=True)
    date = fields.Date(string='Date', default=fields.Date.today(), required=True)
    trip_id = fields.Many2one('tfs_trip_manager.trip', string='Trip', required=True)

    @api.constrains('amount')
    def _check_amount(self):
        for record in self:
            if record.amount < 0:
                raise ValidationError("Your amount value cannot be lower than 0")
    