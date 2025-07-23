from odoo import http
from odoo.http import request

class Presentation(http.Controller):

    @http.route([
        '/present',
    ], type='http', auth='public', website=True)
    def present(self):
        # Use ORM
        presentations = request.env['presentation'].search([])
        # Render with QWeb
        values = {
            'presentations': presentations,
            'get_url': lambda presentation: presentation.website_url,
        }
        return request.render('present.website_presentation_list', values)

    @http.route([
        '/present/<model("presentation"):presentation>',
        '/present/<model("presentation"):presentation>/<int:page_index>',
    ], type='http', auth='public', website=True)
    def presentation(self, presentation, page_index=0):
        return request.render('present.website_presentation', {
            'presentation': presentation,
            'page_index': page_index,
            'get_url': lambda presentation: presentation.website_url,
            'list_url': '/present',
            'main_object': presentation,
        })

    @http.route([
        '/present/metadata',
        '/present/metadata/<model("presentation"):presentation>',
    ], type='jsonrpc', auth='public', website=True)
    def metadata(self, presentation=None, **kwargs):
        if not presentation:
            presentation = request.env['presentation'].browse(kwargs.get('presentation_id'))
        return {
            'date': presentation.write_date,
            'author': presentation.write_uid.name,
        }
