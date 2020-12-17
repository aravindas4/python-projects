def injection():
    items = 28,20.8,True,'A'
    var = ""
    for value in items:
        strng = str(value)
        var = var + strng + ' '
    return var

print(injection())
