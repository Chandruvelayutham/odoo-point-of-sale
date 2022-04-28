from odoo import api,fields,models

class OnlinePOSproductID(models.Model):
    _name = "online.pos.inventory"
    _description = "Online POS Inventory"        
    
    product_id=fields.Integer(String='product_id',required=True)
    name=fields.Char(String='product_name',required=True)
    price=fields.Integer(String='price',required=True)
    gst=fields.Integer(String='GST',required=True)
    quantity=fields.Integer(String='quantity',required=True)
    set_product_image=fields.Binary(String='set_product_image',max_width=10,max_height=10)
    state=fields.Selection([('godown','Godown'),('selling floor','Selling Floor')],String='Status',default='godown')
    
    calculate_quantity=fields.Many2one('online.pos.product.details',String='calculate_quantity')
    
    
    
