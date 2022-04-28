from odoo import api,fields,models

class createProductDetails(models.Model):
    
    _name="online.pos.product.details"
    _description="Online POS Product Details"
    
    product_name=fields.Many2one(comodel_name='online.pos.customer',required=True)
    grand_total=fields.Float(String='grand_total',required=True,compute='onchange_product_details_id')
    
    product_details_id=fields.One2many('online.pos.billing','create_product_record',String='create_product_details_id')
    #calculate_product_quantity=fields.One2many('online.pos.inventory','calculate_quantity',String='calculate_product_quantity')
    
    
    @api.onchange('grand_total','product_details_id')
    def onchange_product_details_id(self):
        for find_total in self:
            find_total.grand_total=0
            for find_product_details in find_total.product_details_id:
                find_total.grand_total+=find_product_details.total
                
                