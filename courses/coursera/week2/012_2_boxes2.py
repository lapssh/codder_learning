a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())

box1 = [a1, b1, c1]
box2 = [a2, b2, c2]
box1.sort()
box2.sort()
vbox1 = a1 * b1 * c1
vbox2 = a2 * b2 * c2
cs = box1[0] <= box2[0] and box1[1] <= box2[1] and box1[2] <= box2[2]
cb = box1[0] >= box2[0] and box1[1] >= box2[1] and box1[2] >= box2[2]

if a1 >= 0 and b1 >= 0 and c1 >= 0 and a2 >= 0 and b2 >= 0 and c2 >= 0:
    if vbox1 == vbox2 and box1 == box2:
        print('Boxes are equal')
    elif vbox1 < vbox2 and cs is True:
        print('The first box is smaller than the second one')
    elif vbox1 > vbox2 and cb is True:
        print('The first box is larger than the second one')
    else:
        print('Boxes are incomparable')
else:
    print('Boxes are incomparable')
