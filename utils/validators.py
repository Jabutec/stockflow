def is_valid_name(name):
    return bool(name.strip())

def is_valid_phone(phone):
    phone = phone.strip()
    
    if not phone:
        return False
    
    return phone.isdigit() and len(phone) == 10

def is_valid_email(email):
    return bool(email.strip())

def is_postive_integer(value):
    return value > 0
    