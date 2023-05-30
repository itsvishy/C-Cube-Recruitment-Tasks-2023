# Simple Pattern Recogniser

def pattrec(l):
    lg = len(l)

    for size in range(1, lg//2+1):
        pattern = l[:size]
        rep = lg//size
        if (pattern*rep == l[:size * rep]):
            print("List: ", l)
            print("Pattern Found: ", pattern)
            print("Repititions: ", rep)
            print()
            n = 1
            break
        else:
            n = 0
    if n == 0:
        print("List: ", l)
        print("Pattern not found.")
        print()


l1 = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pattrec(l1)
pattrec(l2)
