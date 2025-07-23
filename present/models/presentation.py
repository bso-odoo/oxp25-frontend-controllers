from odoo import models, fields

class Presentation(models.Model):
    _name = 'presentation'
    _description = "Presentation"
    _inherit = ['website.published.multi.mixin']
    _order = 'name'

    def _compute_website_url(self):
        super()._compute_website_url()
        for presentation in self:
            if presentation.id:
                presentation.website_url = '/present/%s' % (self.env['ir.http']._slug(presentation))

    name = fields.Char("Name", required=True, translate=True)
    description = fields.Char("Description", required=True, translate=True)
    page_ids = fields.One2many('presentation.page', 'presentation_id', "Presentation Pages")
