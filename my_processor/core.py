
from .utils import clean_name, validate_email, validate_phone



class InvalidMemberDataError(Exception):
       
        def __init__(self, member_name, reason):
            self.member_name = member_name
            self.reason = reason
            message = f"Invalid data for member '{member_name}': {reason}"
            super().__init__(message)  
class Member:
    
    def __init__(self, name, email, phone):

        if not name or not isinstance(name, str):
            raise InvalidMemberDataError(name or "Unknown", "missing or invalid name")
        if not validate_email(email):
            raise InvalidMemberDataError(name, "invalid email format")
        if not validate_phone(phone):
            raise InvalidMemberDataError(name, "invalid phone format")
        self.name = clean_name(name)
        self.email = email.strip().lower()
        self.phone = phone.strip()
    def __str__(self):
         return f"Member(name='{self.name}', email='{self.email}', phone='{self.phone}')"
    def __repr__(self):
         return self.__str__()
    def to_dict(self):
        
         return {"name": self.name, "email": self.email, "phone": self.phone}
def process_raw_members(raw_members):

    successful_members = []
    error_count = 0
    for raw in raw_members:
        
        name = raw.get("name", "InvalidData")
        email = raw.get("email")
        phone = raw.get("phone")
        print(f"Processing member: {name}...", end=" ")
        try:
           member = Member(name, email, phone)
        except InvalidMemberDataError as exc:
           print("Validation Failed.")
           print(f"Error: {exc.reason} for member '{name}'. Skipping.")
           error_count += 1
           continue
        except (KeyError, ValueError, TypeError) as exc:
        
           print("Validation Failed.")
           print(f"Error: Unexpected error for member '{name}': {exc}. Skipping.")
           error_count += 1
           continue
        print("Validation Successful.")
        successful_members.append(member)
    print(f"Summary: {len(successful_members)} members processed successfully.")
    return successful_members, error_count

def filter_members_by_domain(members, domain):

    return list(filter(lambda m: m.email.endswith(f"@{domain}"), members))
def get_all_names(members):

    return list(map(lambda m: m.name, members))