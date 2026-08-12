import re

EMAIL_PATTERN = re.compile(
r"^[A-Za-z0-9._%+-]+@(?:[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\.)+[A-Za-z]{2,}$"
)

PHONE_PATTERN = re.compile(
r"^(\+\d{1,3}[- .]?)?\d{3}[- .]?\d{4}$"
)
def clean_name(raw_name):

    if not isinstance(raw_name, str):
        return ""

    name = raw_name.strip()

    name = re.sub(r"\s+", " ", name)
    return name.title()
def validate_email(email):
   
    if not isinstance(email, str):
       return False
    return bool(EMAIL_PATTERN.match(email.strip()))
def validate_phone(phone):
 
    if not isinstance(phone, str):
       return False
    return bool(PHONE_PATTERN.match(phone.strip()))