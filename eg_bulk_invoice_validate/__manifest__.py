{
    'name': 'Bulk Invoice Validate',
    'version': '15.0.1.0.0',
    'category': 'purchase',
    'summery': 'Confirm Bulk Invoice Validate',
    'author': 'INKERP',
    'website': "https://www.INKERP.com",
    'depends': ['purchase', 'account'],

    'data': [
        'views/purchase_order_view.xml',
    ],
    
    'images': ['static/description/banner.png'],
    'license': "OPL-1",
    'installable': True,
    'application': True,
    'auto_install': False,
}
