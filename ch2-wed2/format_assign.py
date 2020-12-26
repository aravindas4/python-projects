def format(*all):
    assign1,assign2,assign3 = all
    a = "{}'s favorite sports is {}.".format(assign1,assign2)
    b = "{} is working on {} programming!".format(assign1,assign3) 
    return "\n".join({a,b})

print(format("Anand","cricket","python"))
