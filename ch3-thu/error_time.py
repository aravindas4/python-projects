def fix(name):
    if name == "Jack":
        "Hello Jack"
    else:
        return "Hello John"

def military_time(time):
    if time < 1200:
        return "Good Morning"
    elif 1200 >= time <= 1700:
        "Good Afternoon"
    elif time > 1700:
        return "Good Evening"
