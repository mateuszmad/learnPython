def vowels(a):
    qa = 0
    qe = 0
    qi = 0
    qo = 0
    qu = 0
    qy = 0

    for sign in a:

        if sign == "a":
            qa += 1

        if sign == "e":
            qe += 1

        if sign == "i":
            qi += 1

        if sign == "o":
            qo += 1

        if sign == "u":
            qu += 1

        if sign == "y":
            qy += 1

    return qa, qe, qi, qo, qu, qy


if __name__ == '__main__':
    x = str(input("Please enter a text to check vawels in it >>"))
    vowels(x)
    print(x)
    a, e, i, o, u, y = vowels(x)
    print("Amonut of a:", a)
    print("Amount of e:", e)
    print("Amount of i:", i)
    print("Amount of o:", o)
    print("Amount of u:", u)
    print("Amount of y:", y)
