def pyramid(num):
    store = [digit*"x " for digit in range(num)]
    pyramid = "\n".join(store)
    return pyramid

def extract(names):
    name = [word for word in names if str(word).isalpha() == True]
    return name

def temperature(celsius):
    fahernheit = [9/5*num+32 for num in celsius]
    return fahernheit
