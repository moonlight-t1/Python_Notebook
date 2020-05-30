class NotPalindromeError(Exception):
    def __init__(self):
        if word != "".join(reversed(word)):  # 회문판별 1
            super().__init__("회문이 아닙니다")


def palindrome(word):
    if word != word[::-1]:  # 회문판별 2
        raise NotPalindromeError
    else:
        print(word)


try:
    word = input()
    palindrome(word)
except NotPalindromeError as e:
    print(e)
