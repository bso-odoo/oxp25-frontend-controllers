from odoo import models, fields

class Page(models.Model):
    _name = 'presentation.page'
    _description = "Page"

    title = fields.Char("Title", required=True, translate=True)
    content_ids = fields.One2many('presentation.content', 'page_id', "Page Content")
    presentation_id = fields.Many2one('presentation', "Presentation", ondelete='cascade')
