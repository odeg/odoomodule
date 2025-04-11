from odoo import models, fields

class ProductoPersonalizado(models.Model):
    _name = 'producto.personalizado'
    _description = 'Producto Personalizado'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Descripción')
    price = fields.Float(string='Precio')
    stock = fields.Integer(string='Inventario')
