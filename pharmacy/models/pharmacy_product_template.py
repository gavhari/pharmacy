from odoo import models, fields, api

class PharmacyProductTemplate(models.Model):
    _inherit = "product.template"
    
    exp_date = fields.Date(string="Expired Date")
    batch_number = fields.Char(string="Batch Number")
    category = fields.Many2one(comodel_name="pharmacy.drug.category", string="Category")
    available = fields.Boolean(string="Availability")
    
    
class PharmacyDrugCategory(models.Model):
    _name = "pharmacy.drug.category"
    _description = "Drug Category"
    
    name = fields.Char(string="Category Name")
    desc = fields.Text(string="Category description detail")