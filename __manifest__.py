# -*- coding: utf-8 -*-
{
    'name': "tfs_trip_manager",

    'summary': """
        Business trip management module""",

    'description': """
        A module for the management of business trips with detail
        and tracking of every step.
    """,

    'author': "Thomas Freitas",
    'website': "https://github.com/thomaswillix",
    'license': "LGPL-3",

    'category': 'Human Resources',
    'version': '0.1',

    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/trip.xml',
        'views/hr_employee_custom.xml',
        'views/trip_progress.xml',
        'views/trip_expense.xml',
        'views/trip_phase.xml',
    ],
    # only loaded in demonstration mode
    'application' : True,
    'demo': [
        'demo/demo.xml'
    ],
}
