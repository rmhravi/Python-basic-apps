def mulTable():
    num = int(input("Enter a number to be multiplied: "))
    n = int(input("Enter a number to be number of times: "))

    while True:
        for i in range(1, n+1):
            mul = i * num
            print(i, "*", num, "=", mul)
            pass
        print("\n")
        mulTable()
        break

mulTable() 