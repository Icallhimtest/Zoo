# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Zoo(models.Model):
    _name = 'zoo.zoo'
    _description = 'Zoo'

    name = fields.Char(required=True)
    caretaker_count = fields.Integer("Number of hired Caretakers")
    caretaker_work_hours = fields.Integer(default=8)
    total_caretaker_hours = fields.Integer(compute='_compute_total_caretaker_hours')

    @api.depends('caretaker_count', 'caretaker_work_hours')
    def _compute_total_caretaker_hours(self):
        for zoo in self:
            zoo.total_caretaker_hours = zoo.caretaker_count * zoo.caretaker_work_hours

    def set_required_caretaker_count(self):
        # so no animal dies of hunger (can be an overestimation)
        for zoo in self:
            pass
