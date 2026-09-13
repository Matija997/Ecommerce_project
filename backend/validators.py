import re

EMAIL_RE = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
PHONE_RE = re.compile(r'^\+381\d{6,12}$')


def validate_email_format(email):
    return bool(email and EMAIL_RE.match(email))


def validate_password_strength(password):
    return bool(
        password
        and len(password) >= 8
        and re.search(r'[A-Z]', password)
        and re.search(r'[a-z]', password)
        and re.search(r'[0-9]', password)
    )


def validate_phone_format(phone):
    return bool(phone and PHONE_RE.match(phone))
