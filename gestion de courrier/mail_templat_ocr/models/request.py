from odoo import models, fields, api, _
import pytesseract
from PIL import Image
import re
import io
import base64
from pdf2image import convert_from_bytes
import logging

_logger = logging.getLogger(__name__)

class HrEmployee(models.Model):
    _inherit = 'request.request'

    cin = fields.Char(string="CIN")
    email_from = fields.Char(string="Email From")
    email_cc = fields.Char(string="Email CC")
    email_subject = fields.Char(string="Email Subject")
    courrier = fields.Binary("Courrier")
    document_type = fields.Selection([('image', 'Image'), ('pdf', 'PDF')], string="Type de Document", default='image')

    def extract_text_from_image(self):
        for record in self:
            if record.courrier:
                try:
                    document_data = base64.b64decode(record.courrier)
                    ocr_result = ""

                    if record.document_type == 'pdf':
                        images = convert_from_bytes(document_data)
                        for image in images:
                            ocr_result += pytesseract.image_to_string(image) + "\n"
                    else:
                        image_buffer = io.BytesIO(document_data)
                        image = Image.open(image_buffer)
                        ocr_result = pytesseract.image_to_string(image)

                    organized_data = self._organize_text(ocr_result)
                    if 'CIN' in organized_data:
                        record.cin = organized_data.get('CIN')
                    if 'Email from' in organized_data:
                        record.email_from = organized_data.get('Email from')
                    if 'Email CC' in organized_data:
                        record.email_cc = organized_data.get('Email CC')
                    if 'Email subject' in organized_data:
                        record.email_subject = organized_data.get('Email subject')

                    return organized_data

                except Exception as e:
                    _logger.error(f"Error extracting text from document: {e}")
                    return {}

    @staticmethod
    def _organize_text(ocr_text):
        patterns = {
            'CIN': r'CIN\s*:\s*([A-Z]{1,2}[0-9]{6,7})',
            'Email from': r'From\s*:\s*(.+)',
            'Email CC': r'Cc\s*:\s*(.+)',
            'Email subject': r'Subject\s*:\s*(.+)'
        }
        organized_data = {}
        lines = ocr_text.split('\n')
        for line in lines:
            for key, pattern in patterns.items():
                result = re.search(pattern, line, re.IGNORECASE)
                if result:
                    organized_data[key] = result.group(1).strip()
        return organized_data
