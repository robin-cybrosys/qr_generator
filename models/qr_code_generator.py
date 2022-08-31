try:
    import qrcode
except ImportError:
    qrcode = None
try:
    import base64
except ImportError:
    base64 = None
from io import BytesIO
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class QrCodeGenerator(models.Model):
    _name = 'qr.code.generator'

    qr_code = fields.Binary('QRcode', compute="_generate_qr")

    @api.model
    def generate_qr(self, data):
        if data != "":
            img = qrcode.make(data)
            result = BytesIO()
            img.save(result, format='PNG')
            result.seek(0)
            img_bytes = result.read()
            base64_encoded_result_bytes = base64.b64encode(img_bytes)
            base64_encoded_result_str = base64_encoded_result_bytes.decode(
                'ascii')
            return base64_encoded_result_str
