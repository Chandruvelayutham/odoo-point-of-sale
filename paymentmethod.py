from odoo import api,fields,models

class OnlinePOSpayment(models.Model):
    _name = "online.pos.paymentmethod"
    _description = "Online POS Paymentmethod"
    
   
    
    grand_total=fields.Float(String='grand_total')
    cash=fields.Float(String='cash')
    upi_payment=fields.Char(String='upi_paqyment')
    card_payment=fields.Selection([('credit','Credit'),('debit','Debit')])
    card_holder=fields.Char(String='card_holder')
    card_number=fields.Integer(String='card_number')
    
    
    def online_payment(self):
        print('upi_payment')

            
    
    
    
    
    