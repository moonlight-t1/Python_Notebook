# 단순한 일반 함수
def simple_html_tag(tag, msg):
    print("<{0}>{1}<{0}>".format(tag, msg))

simple_html_tag("h1", "Simple Heading Title")

print("-" * 30)

# 함수를 리턴하는 함수
def html_tag(tag):
    def wrap_text(msg):
        print("<{0}>{1}<{0}>".format(tag, msg))
    return wrap_text

print_h1 = html_tag('h1')
print_h1('First Heading Title')
print_h1('Second Heading Title')

print_p = html_tag('h')
print_p('This is a paragraph')


