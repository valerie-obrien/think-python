import math

def eval_loop():
    while True:
        line = input("Enter a mathematical expression or 'done' > ")
        if line == 'done':
            break
        print(eval(line))
        x = eval(line)
    print(x)

eval_loop()