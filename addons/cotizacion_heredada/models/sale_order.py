from odoo import models, fields, exceptions

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    tipo_cotizacion = fields.Selection(
        [('normal', 'Normal'), ('promocion', 'Promoción')],
        string='Tipo de Cotización',
        default='normal'
    )

    def action_confirm(self):
        for order in self:
            if order.tipo_cotizacion == 'promocion':
                partner = order.partner_id
                facturas_vencidas = self.env['account.move'].search([
                    ('partner_id', '=', partner.id),
                    ('state', '=', 'posted'),
                    ('payment_state', '=', 'not_paid'),
                    ('move_type', '=', 'out_invoice')
                ])
                if facturas_vencidas:
                    raise exceptions.UserError("Este cliente tiene facturas vencidas. No se puede confirmar la cotización con promoción.")
        return super(SaleOrder, self).action_confirm()
