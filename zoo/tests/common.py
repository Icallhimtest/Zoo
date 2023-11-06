# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields
from odoo.tests.common import SavepointCase

# import logging
# _logger = logging.getLogger(__name__)


class TestZooCommon(SavepointCase):

    # -------------------------------------------------------------------------
    # DATA GENERATION
    # -------------------------------------------------------------------------

    @classmethod
    def setUpClass(cls):
        super(TestZooCommon, cls).setUpClass()
        cls.zoo = cls.env['zoo.zoo'].create({
            'name': 'Test Zoo',
            'caretaker_count': 1,
            'caretaker_work_hours': 8,
        })

        cls.monkey = cls.env['zoo.species'].create({
            'name': 'Monkey',
            'enclosure_capacity': 15,
            'feeding_time': 1,
            'feeding_interval_number': 8,
            'feeding_interval_type': 'hours',
        })

        cls.monkey_enclosure = cls.env['zoo.enclosure'].create({
            'species_id': cls.monkey.id,
            'zoo_id': cls.zoo.id,
        })

        cls.monkey_0 = cls.env['zoo.enclosure'].create({
            'name': 'Caesar',
            'species_id': cls.monkey.id,
            'enclosure_id': cls.monkey_enclosure.id,
            'status': 'hungry',
            'last_feeding_time': fields.Datetime.subtract(fields.Datetime.now(), hours=12),
        })
        cls.monkey_1 = cls.env['zoo.enclosure'].create({
            'name': 'Caesar',
            'species_id': cls.monkey.id,
            'enclosure_id': cls.monkey_enclosure.id,
            'status': 'starving',
            'last_feeding_time': fields.Datetime.subtract(fields.Datetime.now(), hours=20),
        })
