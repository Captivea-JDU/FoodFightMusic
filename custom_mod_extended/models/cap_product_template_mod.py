# -*- coding: utf-8 -*-

from datetime import date
from odoo import api, models, fields
import logging
_logger = logging.getLogger(__name__)

class CustomModExtended(models.Model):

    _inherit = 'product.template'
    
    cap_genre = fields.Char(string='Genre')