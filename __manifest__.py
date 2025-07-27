# -*- coding: utf-8 -*-
{
    'name': "bookstore",
    'summary': "It is the module that work on the Book Store",
    'description': """This module is designed to efficiently manage all aspects of a book store's operations. 
     It handles inventory management, book categorization, sales transactions, customer records, supplier 
     information, and reporting.""",
    'author': "Esayas",
    'website': "https://www.yourcompany.com",
    'license': 'LGPL-3',
    'category': 'Book',
    'version': '0.1',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/detail_view.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,

}
