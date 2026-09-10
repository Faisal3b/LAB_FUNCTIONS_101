def x(n: int):
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

x(5)

print("---"*25)
def y(n: int) ->str:
    result = ""
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            result += str(j) + " "
        result += "\n"
    return result

print(y(5))