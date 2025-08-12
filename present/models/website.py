from odoo import models, fields

class Website(models.Model):
    _inherit = 'website'

    def _search_get_details(self, search_type, order, options):
        result = super()._search_get_details(search_type, order, options)
        if search_type in ['presentations', 'all']:
            result.append(self.env['presentation']._search_get_detail(self, order, options))
        return result
