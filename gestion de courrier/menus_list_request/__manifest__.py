{
    'name': 'Menus List Request',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Module for managing categories, dossiers, and activities',
    'description': 'This module provides a way to manage categories, dossiers, and activities with a menu and submenus.',
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/category_views.xml',
        'views/dossier_views.xml',
        'views/activity_views.xml',
        'views/application_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}
