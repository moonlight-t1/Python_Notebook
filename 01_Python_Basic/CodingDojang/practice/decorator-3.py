## HTML 태그 데코레이터 만들기
def html_tag(tag_name):
    def real_decorator(func):
        def wrapper():
            return f"<{tag_name}>{func()}</{tag_name}>"

        return wrapper

    return real_decorator


a, b = input().split()


@html_tag(a)
@html_tag(b)
def hello():
    return "Hello, World!"


print(hello())


class HTML_Tag:
    def __init__(self, tag_name):
        self.tag_name = tag_name

    def __call__(self, func):
        def wrapper():
            return f"<{self.tag_name}>{func()}</{self.tag_name}>"

        return wrapper


@HTML_Tag(a)
@HTML_Tag(b)
def bye():
    return "Bye"


print(bye())
