# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons import decimal_precision as dp


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'
    _order = 'date_release desc, name'
    _rec_name = 'short_name'

    name = fields.Char('Title', required=True)
    author_ids = fields.Many2many('res.partner', string='Authors')
    short_name = fields.Char('Short Title', required=True)
    notes = fields.Text('Internal Notes')
    state = fields.Selection([('draft', 'Not Available'),
                              ('available', 'Available'),
                              ('lost', 'Lost')], 'State')
    description = fields.Html('Description')
    cover = fields.Binary('Book Cover')
    out_of_print = fields.Boolean('Out of Print?')
    date_release = fields.Date('Release Date')
    date_updated = fields.Date('Last Updated')
    pages = fields.Integer('Number of Pages')
    reader_rating = fields.Float('Reader Average Rating', digits=(14, 4), )
    cost_price = fields.Float('Book Cost', dp.get_precision('Book Price'))
    currency_id = fields.Many2one('res.currency', string='Currency',
                                  # optional: currency_field='currency_id',
                                  )
    retail_price = fields.Monetary('Retail Price', )
    publisher_id = fields.Many2one('res.partner', string='Publisher',
                                   # optional: ondelete='set null', context={}, domain=[],
                                   )


class ResPartner(models.Model):
    _inherit = 'res.partner'
    published_book_ids = fields.One2many(
        'library.book', 'publisher_id', string='Published Books')
    authored_book_ids = fields.Many2many(
        'library.book', string='Authored Books',
        # relation='library_book_res_partner_rel' # optional,
    )

    #     @api.depends('value')
    #     def _value_pc(self):
    #         self.value2 = float(self.value) / 100
