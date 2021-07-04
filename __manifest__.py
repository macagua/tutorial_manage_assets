# -*- coding: utf-8 -*-
{
    'name': "Tutorial adding assets",
    'summary': """
        Tutorial about how to create and use Javascript files in Odoo""",
    'description': """
        This module is a tutorial in the form of an app. In this app you can find the code to create and use
        JavaScript functionalities in Odoo 13.

        Source: https://www.oocademy.com/v13.0/tutorial/creating-and-using-javascript-assets-in-odoo-54
    """,
    'version': '13.0.0.1',
    'author': 'Oocademy',
    'support': 'info@oocademy.com',
    'website': 'https://www.oocademy.com/',
    'license': 'Other proprietary',
    'maintainer': 'Leonardo J. Caballero G. <leonardocaballero@gmail.com>',
    'price': 0.00,
    'currency': 'EUR',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tutorial',
    'sequence': 1000,
    # Any module necessary for this one to work correctly
    'depends': [
        'base',
        'web',
        'website',
        'website_theme_install'
    ],
    # Always loaded
    'data': [
        'views/assets.xml',
        'views/views.xml'
    ],
    # Only loaded in demonstration mode
    'demo': [],
    # QWeb templates
    'qweb': [
        'static/src/xml/hello_world.xml'
    ],
    'images': [
        'static/description/icon.png',
        'static/description/banner.jpg'
    ],
    'application': True,
}
