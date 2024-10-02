LABELS = {
    'FACTURAS': ['factura', 'recibo', 'pago'],
    'OCIO/PROGRAMACIÓN': ['leetcode', 'programming', 'code', 'challenge'],
    'PENDIENTE': ['seguridad', 'alerta', 'confirmar'],
    'DESECHO': ['promoción', 'regalo', 'ganar', 'premio']
}

def categorize_email(content):
    content_lower = content.lower()
    for label, keywords in LABELS.items():
        if any(keyword in content_lower for keyword in keywords):
            return label
    return 'DESECHO'  # Categoría por defecto si no coincide con ninguna otra
