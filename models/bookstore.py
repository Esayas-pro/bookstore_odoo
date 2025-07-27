# -*- coding: utf-8 -*-

from odoo import models, fields, api


class bookstore(models.Model):
    _name = 'book.details'
    _description = 'Book Details'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    title = fields.Char(string='Title')
    author = fields.Char(string='Author')
    publisher = fields.Char(string='Publisher')
    published_date = fields.Date(string='Published Date')
    book_age = fields.Integer(string="Book Age", default=0)
    cover = fields.Binary(string='Cover Image')

    @api.depends('published_date')
    def _compute_book_age(self):
        for rec in self:
            if rec.published_date:
                rec.book_age = fields.Date.today().year - rec.published_date.year
            else:
                rec.book_age = 0

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
