def format(name,sport,language):
    a = "{}'s favorite sports is {}.".format(name,sport)
    b = "{} is working on {} programming!".format(name,language)
    return "\n".join({a,b})
