#Nice day to start, i think

import math as m



print("Helo, ma frend, i wan to help u, can i?")
print("write 1 if it is True, 0 if it is False.")


startunderstandable = str(input())
if startunderstandable == "1":
    print("ohhh of course, why i think, that et may be smth anoter. Let's start.")
elif startunderstandable == "0":
    print("nice, thnx for talking.")
    exit(0)
else:
    print("smth wrong, try again.")
    exit(0)


print("Now, pls, wrate smth intersting abot ur triangle: ")
print("да хватит уже этого американского, кстати, если ты не знаешь чё там да как чему равно, то напиши нолик.")
print("сначала стороны:")
a = float(input())
b = float(input())
c = float(input())
print("теперь углы:")
A = float(input())
B = float(input())
C = float(input())

if (A + B + C > 180):
    print("ты чё, такого треугольника не может быть, у тебя углы в сумме больше 180 будут, ну ты дундук!")
    exit(0)

if (a < b + c) and (b < a + c) and (c < a + b):
    A = b*b + c*c - a*a
    A /= 2*b*c
    A = m.degrees(m.acos(A))

    B = a*a + c*c - b*b
    B /= 2*a*c
    B = m.degrees(m.acos(B))

    C = 180 - A - B

    print("угол A = " + A)
    print("угол B = " + B)
    print("угол C = " + C)
    print("ну а стороны ты уже знашеь, мне лень их расписывать, всё пока.")
    exit(0)

if ((a != 0) and (b != 0) and (C != 0)):
    c = a * a + b * b - 2 * a * b * m.cos(m.radians(C))
    c = m.sqrt(c)

    A = b * b + c * c - a * a
    A /= 2 * b * c
    A = m.degrees(m.acos(A))

    B = 180 - A - C

    print("угол A = " + str(A))
    print("угол B = " + str(B))
    print("сторона с = " + str(c))

    exit(0)

elif ((c != 0) and (b != 0) and (A != 0)):
    a = c * c + b * b - 2 * c * b * m.cos(m.radians(A))
    a = m.sqrt(a)

    B = a * a + c * c - b * b
    B /= 2 * a * c
    B = m.degrees(m.acos(B))

    C = 180 - A - B

    print("сторона а = " + str(a))
    print("угол B = " + str(B))
    print("угол C = " + str(C))

    exit(0)

elif ((a != 0) and (c != 0) and (B != 0)):
    b = c * c + a * a - 2 * c * a * m.cos(m.radians(B))
    b = m.sqrt(b)

    A = b * b + c * c - a * a
    A /= 2 * b * c
    A = m.degrees(m.acos(A))

    C = 180 - B - A

    print("угол A = " + str(A))
    print("сторона b = " + str(b))
    print("угол C = " + str(C))

    exit(0)


if ((a != 0) and (b != 0) and (A != 0)):
    B = b * (m.sin(m.radians(A))) / a
    B = m.degrees(m.asin(B))

    C = 180 - A - B

    c = a * a + b * b - 2 * a * b * m.cos(m.radians(C))
    c = m.sqrt(c)

    print("сторона a = " + str(a))
    print("сторона b = " + str(b))
    print("сторона c = " + str(c))
    print("угол A = " + str(A))
    print("угол B = " + str(B))
    print("угол C = " + str(C))
    exit(0)


elif ((c != 0) and (b != 0) and (C != 0)):
    B = b * (m.sin(m.radians(C))) / c
    B = m.degrees(m.asin(B))

    A = 180 - C - B

    a = c * c + b * b - 2 * c * b * m.cos(m.radians(A))
    a = m.sqrt(a)

    print("сторона a = " + str(a))
    print("сторона b = " + str(b))
    print("сторона c = " + str(c))
    print("угол A = " + str(A))
    print("угол B = " + str(B))
    print("угол C = " + str(C))
    exit(0)


elif ((a != 0) and (c != 0) and (A != 0)):
    C = c * (m.sin(m.radians(A))) / a
    C = m.degrees(m.asin(C))

    B = 180 - A - C

    b = a * a + c * c - 2 * a * c * m.cos(m.radians(B))
    b = m.sqrt(b)

    print("сторона a = " + str(a))
    print("сторона b = " + str(b))
    print("сторона c = " + str(c))
    print("угол A = " + str(A))
    print("угол B = " + str(B))
    print("угол C = " + str(C))
    exit(0)


elif ((c != 0) and (a != 0) and (C != 0)):
    A = a * (m.sin(m.radians(C))) / c
    A = m.degrees(m.asin(A))

    B = 180 - C - A

    b = c * c + a * a - 2 * c * a * m.cos(m.radians(B))
    b = m.sqrt(b)

    print("сторона a = " + str(a))
    print("сторона b = " + str(b))
    print("сторона c = " + str(c))
    print("угол A = " + str(A))
    print("угол B = " + str(B))
    print("угол C = " + str(C))
    exit(0)


elif ((b != 0) and (a != 0) and (B != 0)):
    A = a * (m.sin(m.radians(B))) / b
    A = m.degrees(m.asin(A))

    C = 180 - A - B

    c = a * a + b * b - 2 * a * b * m.cos(m.radians(C))
    c = m.sqrt(c)

    print("сторона a = " + str(a))
    print("сторона b = " + str(b))
    print("сторона c = " + str(c))
    print("угол A = " + str(A))
    print("угол B = " + str(B))
    print("угол C = " + str(C))
    exit(0)


elif ((b != 0) and (c != 0) and (B != 0)):
    C = c * (m.sin(m.radians(B))) / b
    C = m.degrees(m.asin(C))

    A = 180 - C - B

    a = c * c + b * b - 2 * c * b * m.cos(m.radians(A))
    a = m.sqrt(a)

    print("сторона a = " + str(a))
    print("сторона b = " + str(b))
    print("сторона c = " + str(c))
    print("угол A = " + str(A))
    print("угол B = " + str(B))
    print("угол C = " + str(C))
    exit(0) #ну тут я уже задолбался, поэтому не буду расписывать что именно мы получаем, может потом как-нибудь, но навряд ли

if ((C != 0) and (B != 0)):
    A = 180 - C - B

elif ((A != 0) and (C != 0)):
    B = 180 - A - C

elif ((B != 0) and (A != 0)):
    C = 180 - B - A

if ((a != 0) and (C != 0) and (B != 0)):
    c = a * m.sin(m.radians(C)) / m.sin(m.radians(A))

    b = a * m.sin(m.radians(B)) / m.sin(m.radians(A))

    print("сторона a = " + str(a))
    print("сторона b = " + str(b))
    print("сторона c = " + str(c))
    print("угол A = " + str(A))
    print("угол B = " + str(B))
    print("угол C = " + str(C))
    exit(0)


elif ((c != 0) and (A != 0) and (B != 0)):
    b = c * m.sin(m.radians(B)) / m.sin(m.radians(C))

    a = c * m.sin(m.radians(A)) / m.sin(m.radians(C))

    print("сторона a = " + str(a))
    print("сторона b = " + str(b))
    print("сторона c = " + str(c))
    print("угол A = " + str(A))
    print("угол B = " + str(B))
    print("угол C = " + str(C))
    exit(0)

elif ((b != 0) and (C != 0) and (A != 0)):
    c = b * m.sin(m.radians(C)) / m.sin(m.radians(B))

    a = b * m.sin(m.radians(A)) / m.sin(m.radians(B))

    print("сторона a = " + str(a))
    print("сторона b = " + str(b))
    print("сторона c = " + str(c))
    print("угол A = " + str(A))
    print("угол B = " + str(B))
    print("угол C = " + str(C))
    exit(0)
