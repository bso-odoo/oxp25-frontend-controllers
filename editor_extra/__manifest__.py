{
    'name': 'Editor Extra',
    'category': 'Example',
    'sequence': 1,
    'website': 'https://www.odoo.com/event/odoo-experience-2026-9099/track/into-the-odoo-editor-11015',
    'summary': 'Explains how to add features to Odoo Editor',
    'version': '1.0',
    'depends': ['html_editor'],
    'data': [
    ],
    'demo': [
    ],
    'application': True,
    'installable': True,
    'assets': {
        'html_editor.assets_editor': [
            'editor_extra/static/src/plugins/**/*',
            'editor_extra/static/src/plugin_sets.js',
            'editor_extra/static/src/embedded_components/**/*',
            'editor_extra/static/src/embedding_sets.js',
        ],
        'web.assets_frontend': [
            'editor_extra/static/src/embedded_components/**/*',
            'editor_extra/static/src/embedding_sets.js',
        ],
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',
}
