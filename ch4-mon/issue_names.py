def string(sport):
    line = []
    for item in sport:
        line.append(f"I like to play {item}")
    return ", ".join(line)

def group(name):
    first_letter = []
    for item in name:
        first_letter.append(item[0])
    return ",".join(first_letter)
