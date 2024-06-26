# -*- coding: utf-8 -*-
import random

from odoo import models, fields, api
from datetime import timedelta

import logging
_logger = logging.getLogger(__name__)

# order matters !
ANIMAL_STATUS = [
    ('fed', 'Fed'),
    ('hungry', 'Hungry'),
    ('starving', 'Starving'),
    ('dead', 'Dead'),
]


class Animal(models.Model):
    _name = 'zoo.animal'
    _description = 'Animal'

    name = fields.Char(required=True)
    species_id = fields.Many2one('zoo.species', 'Species', required=True)
    enclosure_id = fields.Many2one('zoo.enclosure', 'Enclosure', required=True)
    status = fields.Selection(ANIMAL_STATUS, compute='_compute_status', store=True)
    last_feeding_time = fields.Datetime(default=fields.Datetime.now(), required=True)
    next_feeding_time = fields.Datetime()

    @api.depends('last_feeding_time')
    def _compute_status(self):
        now = fields.Datetime.now()
        for animal in self:
            species = animal.species_id
            if not species:
                animal.status = ANIMAL_STATUS[-1][0]
                continue
            feeding_interval = timedelta(**{species.feeding_interval_type: species.feeding_interval_number})
            missed_feedings = int((now - animal.last_feeding_time) / feeding_interval)
            try:
                animal.status = ANIMAL_STATUS[missed_feedings][0]
            except IndexError:
                animal.status = ANIMAL_STATUS[-1][0]

    @property
    def _populate_sizes(self):
        return {
            'small': 10,  # minimal representative set
            'medium': 2000,  # average database load
            'large': 300000, # maxi database load
        }

    def _populate(self, size):
        """ Generate filled enclosures of all species until we've reached given size
        """
        def generate_name():
            return (random.choice('BCDFGHJKLMNPQRSTVWZ') +
                    random.choice('aeiou') +
                    random.choice('bcdfghjklmnpqrstvwz') +
                    random.choice('aeiou') +
                    random.choice('bcdfghjklmnpqrstvwz'))

        size = self._populate_sizes[size]
        animals_created = self
        zoo = self.env['zoo.zoo'].search([])[0]
        species = self.env['zoo.species'].search([])
        while len(animals_created) < size:
            # create enclosures and animals until size is reached
            for spec in species:
                enclosure = self.env['zoo.enclosure'].create({
                    'zoo_id': zoo.id,
                    'species_id': spec.id,
                })
                while enclosure.animal_count < enclosure.capacity:
                    if len(animals_created) >= size:
                        return animals_created
                    animals_created |= self.create({
                        'name': generate_name(),
                        'species_id': spec.id,
                        'enclosure_id': enclosure.id,
                    })
                    if len(animals_created) % 1000 == 0:
                        _logger.info("%s/%s animals created", len(animals_created), size)

        return animals_created

    def feed(self):
        self.write({'last_feeding_time': fields.Datetime.now()})

    @api.model
    def _cron_compute_status(self):
        self.search([])._compute_status()

    @api.model
    def _get_next_animal_to_feed(self):
        pass

    @api.model
    def _cron_feed_today(self):
        """ Feed animals by prioritizing hungry animals
        """
        pass
