from odoo import api,fields,models

class OnlinePOSproductID(models.Model):
    _name = "online.pos.customer"
    _description = "Online POS Customer"
    
    customer_id=fields.Integer(String='id',required=True)
    name=fields.Char(String='name',required=True)
    gender=fields.Selection([('male','Male'),('female','Female'),('non-binary','Non-Binary')],required=True)
    
    _sql_constraints=[('unique_customer_id','unique(customer_id)','This Customer ID already exists')]
    _order='customer_id asc'
    
    