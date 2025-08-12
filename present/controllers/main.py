from odoo import http, tools
from odoo.http import request

class Presentation(http.Controller):
    _presentation_per_page = 3

    @http.route([
        '/present',
        '/present/page/<int:page>',
    ], type='http', auth='public', website=True)
    def present(self, page=1):
        # Use ORM
        presentations = request.env['presentation'].search([], offset=(page - 1) * self._presentation_per_page, limit=self._presentation_per_page)
        total = request.env['presentation'].search_count([])
        url_args = dict() # Fill with whichever parameter needs to be kept across pages
        # Prepare pager
        pager = tools.lazy(lambda: request.website.pager(
            url=request.httprequest.path.partition('/page/')[0],
            total=total,
            page=page,
            step=self._presentation_per_page,
            url_args=url_args,
        ))

        # Render with QWeb
        values = {
            'presentations': presentations,
            'get_url': lambda presentation: presentation.website_url,
            'pager': pager,
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
