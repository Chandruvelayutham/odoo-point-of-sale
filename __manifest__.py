{
    'name' : 'OnlinePOS',
    'version' : '2.1',
    'summary': 'Online Point of Sale',
    'sequence': 10,
    'description': """
Online Point of Sale    """,
    'category': 'Website',
    'website': '',
    'depends' : [],
    'data': [
        'Security/ir.model.access.csv',
        'wizard/createInventoryView.xml',
        'views/Billing.xml',
        'views/History.xml',
        'views/Inventory.xml',
        'views/productDetail.xml',
        'views/customer.xml',
        'views/paymentmethod.xml'
        ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,

}