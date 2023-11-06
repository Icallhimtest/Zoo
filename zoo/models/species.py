# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Species(models.Model):
    _name = 'zoo.species'
    _description = 'Species'

    name = fields.Char(required=True)
    animal_ids = fields.One2many('zoo.animal', 'species_id', 'Animals')
    enclosure_capacity = fields.Integer('Default Enclosure Capacity')
    feeding_time = fields.Integer(default=1, help="Time it takes to feed one enclosure (minutes)")
    feeding_interval_number = fields.Integer(default=1, help="Feed every x.", required=True)
    feeding_interval_type = fields.Selection([
        ('hours', 'Hours'),
        ('days', 'Days'),
        ('weeks', 'Weeks'),
    ], string='Interval Unit', default='days', help="Feed every x.", required=True)
