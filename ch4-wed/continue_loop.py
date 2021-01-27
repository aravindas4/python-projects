def type():
    while True:
        word = input("Enter: ")
        if word == "quit":
            break 

def double_loop(num,game_over = True):
    while True:
        output = []
        for item in range(num):
            output.append(item)
            if item == 2:
                game_over = True
                break
        return ",".join(map(str,output))
        