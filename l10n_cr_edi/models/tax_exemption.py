from odoo import fields, models


class L10CrEdiTaxExemption(models.Model):
    _name = 'l10n_cr_edi.tax.exemption'
    _description = 'Save the exemption data'

    exempt_type = fields.Selection([
        ('01', 'Compras autorizadas'),
        ('02', 'Ventas excentas a diplomáticos'),
        ('03', 'Autorizadas por ley especial'),
        ('04', 'Exenciones emitidas por la D.G. de Hacienda'),
        ('05', 'Transitorio V'),
        ('06', 'Transitorio IX'),
        ('07', 'Transitorio XVII'),
        ('99', 'Otros')],
        string='Type', track_visibility=True, help='Exemption type.', required=True)
    name = fields.Char(
        'Document number', track_visibility=True, required=True,
        help='eInvoice exemption document number.')
    issuer = fields.Char(
        copy=False, track_visibility=True, required=True, help='eInvoice exemption issuer.')
    exempt_datetime = fields.Datetime(
        'Date and time of issue', copy=False, track_visibility=True, required=True,
        help='eInvoice exemption date and time of issue.')
    partner_id = fields.Many2one(
        'res.partner', help='Partner that can use this record.', required=True, track_visibility=True)
    active = fields.Boolean(
        default=True,
        help='If the exemption has expired, this could be deactivated.')
