def type():
    while True:
        word = input()
        if word == "quit":
            break 

def double_loop(num):
    game_over = False
    output = []
    while not game_over:
        for item in range(num):
            if item == 3:
                game_over = True
                break
            output.append(item)
    return ",".join(map(str, output))
