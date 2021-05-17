def uppercase(word):
    if word.istitle() == True:
        return True
    else:
        return False

def name(first_name='No name',last_name='passed in'):
    return first_name + " " + last_name
