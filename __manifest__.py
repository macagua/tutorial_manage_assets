# -*- coding: utf-8 -*-
{
    'name': 'Tutorial Manage JavaScript Assets',
    'version': '13.0.1.0.0',
    'author': 'Leonardo J. Caballero G.',
    'website': 'https://www.oocademy.com/v13.0/tutorial/creating-and-using-javascript-assets-in-odoo-54',
    'license': 'AGPL-3',
    'maintainer': 'Pidela.App',
    'support': 'leonardocaballero@gmail.com',
    'category': 'Website/Website',
    'sequence': 1000,
    'description': """
Tutorial Manage JavaScript Assets
=================================

Creating and using JavaScript assets in Odoo 13.
""",
    'depends': [
        'base',
        'web',
        'website',
        'website_theme_install'
    ],
    'data': [
        'views/assets.xml',
        'views/views.xml',
    ],
    'qweb': ['static/src/xml/hello_world.xml',], 
    'demo': [],
    'installable': True
}
