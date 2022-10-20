# -*- coding: utf-8 -*-
from odoo import fields, models


class Purchase(models.Model):
    _inherit = "purchase.py"

    gse_default_analytic_id = fields.Many2one(
        'account.analytic.account',
        string='Default Analytic Accounting',
        )
