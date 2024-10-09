# write your code here

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg += msg_7
    if (v1 == 0 or v2 == 0) and v3 in ('*', '+', '-'):
        msg += msg_8
    if msg != '':
        msg = msg_9 + msg
        print(msg)


def is_one_digit(v):
    if -10 < v < 10 and v == int(v):
        return True
    else:
        return False


memory = 0
while True:
    print(msg_0)
    calc = input()
    x, op, y = calc.split(' ')
    if x == 'M':
        x = memory
    if y == 'M':
        y = memory
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
        continue
    match op:
        case '+' | '-' | '*' | '/':
            pass
        case _:
            print(msg_2)
            continue
    check(x, y, op)
    match op:
        case '+':
            result = x + y
        case '-':
            result = x - y
        case '*':
            result = x * y
        case '/':
            try:
                result = x / y
            except ZeroDivisionError:
                print(msg_3)
                continue
    print(result)
    while True:
        print(msg_4)
        answer = input()
        if answer == 'y':
            break_to_msg_5 = False
            if is_one_digit(result):
                msg_index = 10
                while True:
                    print(globals()[f'msg_{msg_index}'])
                    answer = input()
                    if answer == 'y':
                        if msg_index < 12:
                            msg_index += 1
                        else:
                            break
                    elif answer == 'n':
                        break_to_msg_5 = True
                        break
                    else:
                        continue
            if break_to_msg_5:
                break
            memory = result
            break
        elif answer == 'n':
            break
        else:
            continue
    while True:
        print(msg_5)
        answer = input()
        if answer == 'y':
            continue_calc = True
            break
        elif answer == 'n':
            continue_calc = False
            break
        else:
            continue
    if continue_calc:
        continue
    else:
        break
