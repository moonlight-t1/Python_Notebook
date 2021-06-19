def outer_func(tag):
    text = "Some text"
    tag = tag

    def inner_func():
        print("<{0}>{1}<{0}>".format(tag, text))

    return inner_func


h1_func = outer_func("h1")
p_func = outer_func("p")

h1_func()
p_func()

