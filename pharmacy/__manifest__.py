# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Pharmacy',
    'version' : '1.2',
    'summary': 'Drug and Medicine',
    'sequence': -1,
    'description': """
    Drug and Medicine 
    """,
    'category': 'Pharmacy/Pharmacy',
    'website': 'https://www.github.com/gavhari',
    'images' : [],
    'depends' : ['board','stock','product'],
    'data': [
        'views/pharmacy_menu.xml',
        'views/pharmacy_inventory_product_view.xml'
    ],
    'demo': [
        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {
    },
    'license': 'LGPL-3',
}
