# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Zoo(models.Model):
    _name = 'zoo.zoo'
    _description = 'Zoo'

    name = fields.Char(required=True)
    caretaker_count = fields.Integer("Number of hired Caretakers")
    caretaker_work_hours = fields.Integer(default=8)
    total_caretaker_hours = fields.Integer(_compute='_compute_total_caretaker_hours')

    @api.depends('caretakers_count', 'caretakers_work_hours')
    def _compute_total_caretaker_hours(self):
        for zoo in self:
            zoo.total_caretaker_hours = zoo.caretaker_count * zoo.caretaker

    # TODO inverse total_caretaker_hours -> caretaker_work_hours
