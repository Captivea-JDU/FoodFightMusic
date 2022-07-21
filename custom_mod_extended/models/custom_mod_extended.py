# -*- coding: utf-8 -*-

from datetime import date
from odoo import api, models, fields
import logging
_logger = logging.getLogger(__name__)

class CustomModExtended(models.Model):

    _inherit = 'sale.order'
    
    cap_year = fields.Integer(string='Year')
    cap_customer_birth_year = fields.Integer(string='Customer Birth Year')
    cap_customer_phone_number = fields.Char(string='Customer phone number')
    cap_customer_nickname = fields.Char(string='Customer Nickname')
    cap_customer_age = fields.Integer(string='Customer Age')
    cap_customer_address = fields.Char(string='Customer Address')
    cap_customer_favorite_genre = fields.Char(string='Favorite Genre')
    cap_year = 2022
    @api.onchange('cap_customer_birth_year')
    def calculate_age(cap_customer_birth_year, cap_year):
        
        cap_customer_age = cap_year - cap_customer_birth_year

        return cap_customer_age