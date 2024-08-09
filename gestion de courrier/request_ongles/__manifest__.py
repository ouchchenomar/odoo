{
    'name': "Request Ongle",

    'summary': """
        Generic  management.
    """,

    'author': "monopoli133 Development",
    'category': 'Generic',
    'version': '1.0',

    "depends": [
        "base", "generic_request", 'mail'
    ],

    "data": [
        'views/request_ongles.xml',
        'views/mail_activity_type_data.xml',
        'data/sequence_data.xml',

    ],
    "installable": True,
    'license': 'LGPL-3',
}
