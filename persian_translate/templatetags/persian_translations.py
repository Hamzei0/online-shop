from django import template

register = template.Library()

@register.filter
def translate_number(value):
    value = str(value)
    english_to_persian__table = value.maketrans('1234567890','١٢٣٤٥٦٧٨٩٠') 
    
    return value.translate(english_to_persian__table)
    
