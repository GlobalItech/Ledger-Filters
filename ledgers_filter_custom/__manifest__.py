# -*- coding: utf-8 -*-
{
    'name': 'Ledger Filters',
    'version': '1.0',
    'category': 'Accounting',
    'author':'itech resources',
    'website': 'http://itechresources.net/',
    'summary': 'Filter on accounts Reports ,Partner, General and Financial Ledger by partner',
    'depends' : ['account_reports'],
    'installable' : True,
    'auto_install' : True,
    'data' :[
                'views/general_ledger_view.xml',
                'views/partner_ledger_view.xml'
            ],
    'demo':[
        ], 
    'price':20.00,
    'currency':'EUR',		
}