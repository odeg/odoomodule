{
    "name": "Cotización Heredada",
    "version": "1.0",
    "category": "Sales",
    "summary": "Extiende el modelo sale.order con un nuevo campo y validación.",
    "depends": ["sale", "account"],
    "data": [
        "security/ir.model.access.csv",
        "views/sale_order_view.xml"
    ],
    "installable": True
}
