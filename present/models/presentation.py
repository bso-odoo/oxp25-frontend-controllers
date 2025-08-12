from odoo import api, models, fields

class Presentation(models.Model):
    _name = 'presentation'
    _description = "Presentation"
    _inherit = [
        'website.published.multi.mixin',
        'website.searchable.mixin',
    ]
    _order = 'name'

    def _compute_website_url(self):
        super()._compute_website_url()
        for presentation in self:
            if presentation.id:
                presentation.website_url = '/present/%s' % (self.env['ir.http']._slug(presentation))

    name = fields.Char("Name", required=True, translate=True)
    description = fields.Char("Description", required=True, translate=True)
    page_ids = fields.One2many('presentation.page', 'presentation_id', "Presentation Pages")

    @api.model
    def _search_get_detail(self, website, order, options):
        with_description = options['displayDescription']
        search_fields = ['name']
        fetch_fields = ['id', 'name', 'website_url']
        mapping = {
            'name': {'name': 'name', 'type': 'text', 'match': True},
            'website_url': {'name': 'website_url', 'type': 'text', 'truncate': False},
        }
        if with_description:
            search_fields.append('description')
            fetch_fields.append('description')
            mapping['description'] = {'name': 'description', 'type': 'text', 'match': True}
        return {
            'model': 'presentation',
            'base_domain': [website.website_domain()],
            'search_fields': search_fields,
            'fetch_fields': fetch_fields,
            'mapping': mapping,
            'icon': 'fa-volume-up',
            'order': 'name desc, id desc' if 'name desc' in order else 'name asc, id desc',
        }
