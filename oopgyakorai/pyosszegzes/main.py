def osszegzes():
    n = int(input("N = "))
    while n < 0:
        n = int(input("N = "))
    osszeg = 0
    for i in range(1,n+1):
        osszeg+=1
    print(f"Az első {n} db természetes szám összege: {osszeg}")