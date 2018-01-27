
def change():

    p = round(float(input("Please input price of product >>")), 2)
    k = round(float(input("What amout of money do you have? >>")), 2)
    if p > k:
        print('You dont have enough money')
    else:
        c = k - p
        print(c)
        typeofchange(c)
        print(typeofchange(c))


def typeofchange(x):

    ch = {'500zl': 0, '200zl': 0, '100zl': 0, '50zl': 0, '20zl': 0, '10zl': 0, '5zl': 0, '2zl': 0, '1zl': 0, '50gr': 0,
          '20gr': 0, '10gr': 0, '5gr': 0, '2gr': 0, '1gr': 0}

    if x / 500 > 0:
        ch['500zl'] = int(x / 500)
        x = x - int(x / 500)*500

    if x / 200 > 0:
        ch['200zl'] = int(x / 200)
        x = x - int(x / 200)*200

    if x / 100 > 0:
        ch['100zl'] = int(x / 100)
        x = x - int(x / 100)*100

    if x / 50 > 0:
        ch['50zl'] = int(x / 50)
        x = x - int(x / 50)*50

    if x / 20 > 0:
        ch['20zl'] = int(x / 20)
        x = x - int(x / 20)*20

    if x / 10 > 0:
        ch['10zl'] = int(x / 10)
        x = x - int(x / 10)*10

    if x / 5 > 0:
        ch['5zl'] = int(x / 5)
        x = x - int(x / 5)*5

    if x / 2 > 0:
        ch['2zl'] = int(x / 2)
        x = x - int(x / 2)*2

    if x / 1 > 0:
        ch['1zl'] = int(x / 1)
        x = x - int(x / 1)*1

    if x / 0.5 > 0:
        ch['50gr'] = int(x / 0.5)
        x = x - int(x / 0.5)*0.5

    if x / 0.2 > 0:
        ch['20gr'] = int(x / 0.2)
        x = x - int(x / 0.2)*0.2

    if x / 0.1 > 0:
        ch['10gr'] = int(x / 0.1)
        x = x - int(x / 0.1)*0.1

    if x / 0.05 > 0:
        ch['5gr'] = int(x / 0.05)
        x = round(x - int(x / 0.05)*0.05, 2)

    if x / 0.02 > 0:
        ch['2gr'] = int(x / 0.02)
        x = round(x - int(x / 0.02)*0.02, 2)

    if x / 0.01 > 0:
        ch['1gr'] = int(x / 0.01)
        x = x - int(x / 0.01)*0.01

    return ch


if __name__ == '__main__':
    change()
