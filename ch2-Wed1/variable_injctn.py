def injection(*vars):
    return ' '.join([str(var) for var in vars])

print(injection(False,122,'wrong',22.4))