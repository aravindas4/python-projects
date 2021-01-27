def string(sport):
    line = [f"I like to play {item}" for item in sport]
    return ", ".join(line)

def group(name):
    first_letter = [item[0] for item in name]
    return ",".join(first_letter)
