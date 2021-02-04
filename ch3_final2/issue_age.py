def group(age):
    if age < 13:
        return "Kid"
    if age < 20:
        return "Teenager"
    if age < 31:
        return "Young Adult"
    if age < 65:
        return "Adult"
    if age >= 65:
        return "Senior"
