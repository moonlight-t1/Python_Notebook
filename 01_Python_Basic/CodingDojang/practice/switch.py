switch = {"+": lambda x, y: x + y, "*": lambda x, y: x * y, "-": lambda x, y: x - y}

x = "+"

try:
    print(switch[x](10, 20))
except KeyError:
    print("default")

