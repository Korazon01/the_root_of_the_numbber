while True:
    ZXC = input('Enter the number you wanted to find out the root of:\n')
    try:
        ZXC = int(ZXC)
    except:
        print("you didn't enter a number")
    else:
        break
def mota(x,err = 0.000000000000001):
    start = 0
    finaly = x+1
    middle = (start+finaly) / 2
    er = []
    while abs(middle**2 - x) > err:
        er.append(middle)
        if middle**2 >x:
            finaly = middle
        else:
            start = middle
        middle = (start+finaly)/2
        if er[-1] == middle:
            return f'there is no root, but there is {middle}'
    return f'the root of number: {x}\nis: {middle}'

print(mota(ZXC))