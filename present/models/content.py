from odoo import models, fields

class Content(models.Model):
    _name = 'presentation.content'
    _description = "Presentation Page Content"

    text = fields.Char("Text", required=True, translate=True)
    type = fields.Selection([
        ('heading', "Heading"),
        ('plain', "Plain text"),
        ('bullet', "Bullet point"),
        ('code', "Code"),
        ('link', "Link"),
    ], string="Type", required=True, default='plain')
    page_id = fields.Many2one('presentation.page', "Page", ondelete='cascade')

    def get_description(self):
        return "<TO DO>"
