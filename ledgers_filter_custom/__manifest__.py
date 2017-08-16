# -*- coding: utf-8 -*-
{
    'name': 'Account and Partner Ledger Filters(Enterprise v10)',
    'version': '1.0',
    'category': 'Accounting',
    'author':'itech resources',
    'website': 'http://itechresources.net/',
    'summary': 'Filter on Partner ledger and General ledger',
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
