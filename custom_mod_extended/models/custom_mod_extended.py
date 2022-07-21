# -*- coding: utf-8 -*-

from odoo import api, models, fields
import logging
_logger = logging.getLogger(__name__)

class CustomModExtended(models.Model):

    _inherit = 'sale.order'
    
    cap_customer_phone_number = fields.Char(string='Customer phone number')
    cap_customer_nickname = fields.Char(string='Customer Nickname')
    cap_customer_age = fields.Integer(string='Customer Age')
    cap_customer_address = fields.Char(string='Customer Address')
    
    
    

