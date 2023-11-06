# -*- coding: utf-8 -*-
from odoo.tests import tagged
from odoo.addons.zoo.tests.common import TestZooCommon

import logging
_logger = logging.getLogger(__name__)


@tagged('zoo', 'at_install')
class TestZooHunger(TestZooCommon):

    # -------------------------------------------------------------------------
    # TESTS: Animal Hunger
    # -------------------------------------------------------------------------

    def test_general_ledger_folded_unfolded(self):
        self.assertNotEqual(self.monkey_1, 'fed')
        self.monkey_1.feed()
        self.assertEqual(self.monkey_1, 'fed', "Animal should be status='fed' after feeding")
