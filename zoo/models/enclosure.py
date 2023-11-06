# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Enclosure(models.Model):
    _name = 'zoo.enclosure'
    _description = 'Enclosure'

    name = fields.Char(compute='_compute_name')
    zoo_id = fields.Many2one('zoo.zoo', required=True)
    species_id = fields.Many2one('zoo.species', required=True)
    capacity = fields.Integer(related='species_id.enclosure_capacity')
    animal_ids = fields.One2many('zoo.animal', 'enclosure_id', 'Animals')
    animal_count = fields.Integer(compute='_compute_animal_count')

    @api.depends('name', 'capacity', 'animal_count')
    def _compute_name(self):
        for enclosure in self:
            enclosure.name = "%s (%s/%s)" % (
                enclosure.species_id.name,
                enclosure.animal_count,
                enclosure.capacity)

    @api.depends('animal_ids')
    def _compute_animal_count(self):
        for enclosure in self:
            enclosure.animal_count = self.env['zoo.animal'].search_count([('enclosure_id', '=', enclosure.id)])
