# -*- coding: utf-8 -*-
{
    'name': "Salesman from Employee",

    'summary': "Add Salesman from Employee",

    'description': """
This module is for using Employee as Salesman/Salesperson instead of from res.user
    """,

    'author': "Lintang Utama Infotek",
    'website': "www.lui.co.id",
    'category': 'Sales',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'hr', 'sale_management', 'account'],

    # always loaded
    'data': [
        'views/hr_employee_view.xml',
        'views/sale_order_view.xml',
        # 'views/sale_report_view.xml',
    ],
    'installable': True,
    'application': False,
}

