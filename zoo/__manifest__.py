# -*- coding: utf-8 -*-
{
    'name': "zoo",

    'summary': """
        Zoo Management Application - with performance issues.
    """,

    'description': """
        Debug performance issues in Manage the status and location of all your zoo's animals.
    """,

    'author': "Odoo",
    'website': "https://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'data/data.xml',
        'security/ir.model.access.csv',
        'views/zoo.xml',
        'views/enclosure.xml',
        'views/species.xml',
        'views/animal.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
