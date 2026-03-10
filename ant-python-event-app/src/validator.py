import re

VALID_TICKETS = {"general", "vip", "student"}

def is_valid_email(email: str) -> bool:
    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    return re.match(pattern, email) is not None

def validate_identifier(attendee:dict):
    if not attendee.get("identifier"):
        return "Invalid registration code"
    else:
        if len(attendee.get("identifier").split("-")) != 2:
            return "Invalid registration code"
        if attendee.get("identifier").split("-")[0] != "EV":
            return "Invalid registration code"
        if "-" not in attendee.get("identifier"):
            return "Invalid registration code"
        else:
            if len(attendee.get("identifier").split("-")[1]) != 4:
                return "Invalid registration code"
            for i in attendee.get("identifier").split("-")[1]:
                if not i.isdigit():
                    return "Invalid registration code"

def validate_attendee(attendee: dict) -> list:
    errors = []

    if not attendee.get("name") or not attendee["name"].strip():
        errors.append("Invalid name")

    if not is_valid_email(attendee.get("email", "")):
        errors.append("Invalid email")

    age = attendee.get("age")
    if not isinstance(age, int) or age < 18:
        errors.append("Attendee must be 18 or older")

    if attendee.get("ticket_type") not in VALID_TICKETS:
        errors.append("Invalid ticket type")
    if validate_identifier(attendee):
        errors.append(validate_identifier(attendee))
    
    return errors