
{
   
    'name': 'Odoo Pro Biometric Integration',
    'version': '8.0.1.0.1',
    'summary': 'Professional biometric integration with advanced logging, UI, and configuration.',
    'author': 'Dimas Aryo Novantri',
    'category': 'Human Resources/Attendances',

  
    'license': 'OPL-1', 
    'price': 350.00,
    'currency': 'USD',


    'images':[
        'images/banner.png',
        ],
    

    'long_description': open('static/description/index.html').read(),

    
    
    'depends': [
        'hr_attendance',
    ],
    

    'data': [
        'security/ir.model.access.csv',
        'views/res_config_settings_views.xml',
        'views/hr_biometric_data_views.xml',
        'views/hr_attendance_views.xml',
        'views/biometric_menus.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}


