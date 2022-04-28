from odoo import api,fields,models

class OnlinePOSproductID(models.TransientModel):
    _name = "online.pos.wizard"
    _description = "Online POS Inventory"        
    
    product_id=fields.Integer(String='product_id',required=True,related='name.product_id')
    name=fields.Many2one(comodel_name='online.pos.inventory',required=True)
    price=fields.Integer(String='price',required=True,related='name.price')
    gst=fields.Integer(String='GST',required=True,related='name.gst')
    quantity=fields.Integer(String='quantity',required=True,related='name.quantity')
    set_product_image=fields.Binary(String='set_product_image',max_width=0.1,max_height=0.1,related='name.set_product_image')
    
    
    def action_create_product_details(self):
        
        vals={
            'product_id': self.product_id.product_id,
            'name': self.name.name,
            'price':self.price.price,
            'gst':self.gst.gst,
            'quantity': self.quantity.quantity,
            'set_product_image':self.set_product_image.set_product_image
            }
    
    