from odoo import api,fields,models


class OnlinePOS(models.Model):
    _name = "online.pos.billing"
    _description = "Online POS"
    
    
    
    
    product_name=fields.Many2one(comodel_name='online.pos.inventory',required=True)
    quantity=fields.Integer(String='quantity',required=True,default=1)
    price=fields.Integer(String='Price',required=True,related='product_name.price')
    gst=fields.Integer(String='GST',required=True,default='', related='product_name.gst')
    total=fields.Float(String='Total',compute='onchange_total',required=True,readonly=True)
    discount=fields.Selection([('0','None'),('5','5%'),('10','10%'),('15','15%')],default='0')
    create_product_record=fields.Many2one('online.pos.product.details','product_details_id',String='product_id')
    product_image=fields.Binary(related='product_name.set_product_image',String="order image")
                
    @api.onchange('product_name','quantity','price','gst','discount','total')             
    def onchange_total(self):
        
        for pos_total in self:
            pos_total.total = (pos_total.price * pos_total.quantity * (100 + pos_total.gst ) * 0.01) * (100 - int(pos_total.discount)) * 0.01
