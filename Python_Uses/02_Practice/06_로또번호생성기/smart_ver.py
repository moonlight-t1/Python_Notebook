"""
1. 특정 숫자를 포함해서 로또 번호를 생성해주는 기능
2. 특정 숫자를 제외해서 로또 번호를 생성해주는 기능
3. 정해진 자리수만큼 연속 숫자를 포함하는 번호를 생성하는 기능
"""

import numpy


def make_lotto_number(**kwargs):
    rand_number = numpy.random.choice(
        range(1, 46), 6, replace=False)  # 중복 없이 6개의 숫자를 뽑아낸다
    rand_number.sort()  # sort 해준다

    lotto = []  # 로또 번호

    # kwargs는 사용자의 옵션이 들어간다
    # 특정 숫자를 포함하길 원할 때 include 사용한다
    if kwargs.get("include"):
        include = kwargs.get("include")
        lotto.extend(include)

        # 특정 숫자 제외한 만큼 랜덤 생성하면 된다
        cnt_make = 6 - len(lotto)

        for i in range(cnt_make):
            for j in rand_number:
                if lotto.count(j) == 0:
                    lotto.append(j)
                    break
    else:
        lotto.extend(rand_number)

    # 특정 숫자를 제외하는 기능
    if kwargs.get("exclude"):
        exclude = kwargs.get("exclude")
        # 집합을 이용해 숫자 제외해준다
        lotto = list(set(lotto) - set(exclude))

        # 나머지 숫자들로 랜덤 숫자를 뽑아준다
        while len(lotto) != 6:
            for _ in range(6 - len(lotto)):
                rand_number = rand_number = numpy.random.choice(
                    range(1, 46), 6, replace=False)
                rand_number.sort()

                for j in rand_number:
                    if lotto.count(j) == 0 and j not in exclude:
                        lotto.append(h)
                        break

    # 연속된 숫자들을 포함하게 하는 기능
    if kwargs.get("continuty"):
        continuty = kwargs.get("continuty")
        start_number = numpy.random.choice(lotto, 1)

        seq_num = []

        for i in range(start_number[0], start_number[0] + continuty):
            seq_num.append(i)

        seq_num.sort()
        cnt_make = 6 - len(seq_num)
        lotto = []
        lotto.extend(seq_num)

        while len(lotto) != 6:
            for _ in range(6 - len(lotto)):
                rand_number = numpy.random.choice(
                    range(1, 46), 6, replace=False)
                rand_number.sort()

                for j in rand_number:
                    if lotto.count(j) == 0 and j not in seq_num:
                        lotto.append(j)
                        break

                lotto = list(set(lotto))

    lotto.sort()
    return lotto


print(make_lotto_number(include=[1, 11]))
print(make_lotto_number(exclusive=[5, 10]))
print(make_lotto_number(continuty=3))
