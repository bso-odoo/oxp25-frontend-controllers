from odoo import http
from odoo.http import request

class Presentation(http.Controller):

    @http.route([
        '/present/plain',
    ], type='http', auth='public', website=True)
    def present(self):
        # Use ORM
        presentations = request.env['presentation'].search([])
        # Render with QWeb
        values = {
            'presentations': presentations,
            'get_url': lambda presentation: '/present/plain/%s' % (self.env['ir.http']._slug(presentation)),
        }
        return request.render('present.plain_presentation_list', values)

    @http.route([
        '/present/plain/<model("presentation"):presentation>',
        '/present/plain/<model("presentation"):presentation>/<int:page_index>',
    ], type='http', auth='public', website=True)
    def presentation(self, presentation, page_index=0):
        return request.render('present.plain_presentation', {
            'presentation': presentation,
            'page_index': page_index,
            'get_url': lambda presentation: '/present/plain/%s' % (self.env['ir.http']._slug(presentation)),
            'list_url': '/present/plain',
        })
