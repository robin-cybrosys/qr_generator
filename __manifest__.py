{
    'name': "QR Code Generator",

    'application': "True",

    'sequence': "-11",

    'author': "R",

    'website': "http://www.cybrosys.com",

    'version': '15.0.1.0.0',

    'licence': "LGPL-3",

    'depends': ['base', 'web'],
    'assets': {
        'web.assets_backend': {
            '/qr_generator/static/src/js/qr_systray.js',
        },
        'web.assets_qweb': {
            '/qr_generator/static/src/xml/qr_systray.xml',
        },
    },

    'data': [
        'security/ir.model.access.csv',
        # 'views/qr_generator.xml',
        # 'views/temp.xml',

    ],
}
