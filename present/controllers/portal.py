from odoo import http
from odoo.http import request

from odoo.addons.portal.controllers import portal


class CustomerPortal(portal.CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        Presentation = request.env['presentation']
        PresentationContent = request.env['presentation.content']
        if 'presentation_count' in counters:
            values['presentation_count'] = Presentation.search_count([]) if Presentation.has_access('read') else 0
        if 'presentation_alert_count' in counters:
            values['presentation_alert_count'] = PresentationContent.search_count([('text', 'like', 'TODO')]) if PresentationContent.has_access('read') else 0
        return values

    @http.route([
        '/my/presentations',
    ], type='http', auth='public', website=True)
    def present(self):
        # Use ORM
        presentations = request.env['presentation'].search([])
        # Render with QWeb
        values = {
            'presentations': presentations,
            'get_url': lambda presentation: '/my/presentation/%s' % (self.env['ir.http']._slug(presentation)),
        }
        return request.render('present.portal_presentation_list', values)

    @http.route([
        '/my/presentation/<model("presentation"):presentation>',
        '/my/presentation/<model("presentation"):presentation>/<int:page_index>',
    ], type='http', auth='public', website=True)
    def presentation(self, presentation, page_index=0):
        return request.render('present.portal_presentation', {
            'presentation': presentation,
            'page_index': page_index,
            'get_url': lambda presentation: '/my/presentation/%s' % (self.env['ir.http']._slug(presentation)),
            'list_url': '/my/presentations',
        })
