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
    'website': 'https://www.oocademy.com/',
    'license': 'Other proprietary',
    'maintainer': 'Leonardo J. Caballero G. <leonardocaballero@gmail.com>',
    'price': 0.00,
    'currency': 'EUR',
    'category': 'Tutorial',
    'sequence': 1000,
    'depends': [
        'base',
        'web',
        'website',
        'website_theme_install'
    ],
    'data': [
        'views/assets.xml',
        'views/views.xml'
    ],
    'qweb': [
        'static/src/xml/hello_world.xml'
    ],
    'demo': [],
    'images': [
        'static/description/icon.png',
        'static/description/banner.jpg'
    ],
    'application': True,
}
