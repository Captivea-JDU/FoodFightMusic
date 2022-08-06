# -*- coding: utf-8 -*-

{
    'name': 'Custom Module',
    'category': 'Sales',
    'summary': "Pulls phone number associated with sale order",
    'version': '1.0 (v13)',
    'author': 'Captivea software Consulting, Jarvis Dumas',
    'website': 'https://www.captivea.com/',
    'license': 'OPL-1',
    'description': """Pulls phone number associated with sale order
        """,
    'depends': ['base', 'sale'],
    'data': [
        'views/views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
