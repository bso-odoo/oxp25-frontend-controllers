{
    'name': 'Present',
    'category': 'Example',
    'sequence': 1,
    'website': 'https://www.odoo.com/event/odoo-experience-2025-6601/track/how-to-create-website-front-end-controllers-8769',
    'summary': 'Explains how to use controllers',
    'version': '1.0',
    'depends': ['website'],
    'data': [
        'views/templates.xml',
        'views/plain.xml',
        'views/website.xml',
        'views/portal.xml',
        'views/snippets/snippets.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
        'data/website.xml',
        'data/demo.xml',
    ],
    'application': True,
    'installable': True,
    'assets': {
        'web.assets_frontend': [
            'present/static/src/**/*',
        ],
        'website.website_builder_assets': [
            'present/static/src/website_builder/**/*',
        ],
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',
}
