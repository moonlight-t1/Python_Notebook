##  1. 기본
# """
# 문제: 어떤 예외를 무시할지 결정하는 두 불 변수의 위치를 혼동하기 쉽다
# """


# def safe_division(number, divisor, ignore_overflow, ignore_zero_division):
#     """number를 divisor로 나눈다

#     Parameters:
#         number: 피제수
#         divisor: 제수
#         ignore_overflow: True면 나눗셈의 오버플로우를 무시하고 0을 반환
#         ignore_zero_division: True면 0으로 나눈 경우 오류 무시하고 무한대 반환


#     Returns:
#         float: 나눗셈 결과
#     """
#     try:
#         return number / divisor
#     except OverflowError:
#         if ignore_overflow:
#             return 0
#         else:
#             raise
#     except ZeroDivisionError:
#         if ignore_zero_division:
#             return float("inf")
#         else:
#             raise


# result = safe_division(1.0, 10 ** 500, True, False)
# print(result)

# result = safe_division(1.0, 0, False, True)
# print(result)

## 2. 키워드 인자 사용
# """
# 해결: 키워드 인자 사용

# 또 다른 문제: 명확성을 위해 키워드 인자를 꼭 사용하도록 강제할 수 없다.
# """


# def safe_division_b(number, divisor, ignore_overflow=False, ignore_zero_division=False):
#     """number를 divisor로 나눈다

#     Parameters:
#         number: 피제수
#         divisor: 제수
#         ignore_overflow: True면 나눗셈의 오버플로우를 무시하고 0을 반환
#         ignore_zero_division: True면 0으로 나눈 경우 오류 무시하고 무한대 반환


#     Returns:
#         float: 나눗셈 결과
#     """
#     try:
#         return number / divisor
#     except OverflowError:
#         if ignore_overflow:
#             return 0
#         else:
#             raise
#     except ZeroDivisionError:
#         if ignore_zero_division:
#             return float("inf")
#         else:
#             raise


# result = safe_division_b(1.0, 10 ** 500, ignore_overflow=True)
# print(result)

# result = safe_division_b(1.0, 0, ignore_zero_division=True)
# print(result)

# assert safe_division_b(1.0, 10 ** 500, True, False) == 0  # 여전히 위치인자 그대로 사용 가능

## 3. * 추가
# """
# 해결: * 기호 사용. * 기호는 위치 인자의 마지막과 키워드만 사용하는 인자의 시작을 구분해준다

# 또 다른 문제: 호출하는 쪽에서 함수의 맨 앞에 있는 두 필수 인자(number, divisor)를 호출하면서
# 위치와 키워드를 혼용할 수 있다.
# 이 필수 인자들의 이름이 변경되기라도 하면 기존 호출 코드가 깨질 수도 있다.
# """


# def safe_division_c(
#     number, divisor, *, ignore_overflow=False, ignore_zero_division=False  # * 추가
# ):
#     """number를 divisor로 나눈다

#     Parameters:
#         number: 피제수
#         divisor: 제수
#         ignore_overflow: True면 나눗셈의 오버플로우를 무시하고 0을 반환
#         ignore_zero_division: True면 0으로 나눈 경우 오류 무시하고 무한대 반환


#     Returns:
#         float: 나눗셈 결과
#     """
#     try:
#         return number / divisor
#     except OverflowError:
#         if ignore_overflow:
#             return 0
#         else:
#             raise
#     except ZeroDivisionError:
#         if ignore_zero_division:
#             return float("inf")
#         else:
#             raise


# # 맨 두 필수 인자들의 위치와 키워드 인자 혼용
# result = safe_division_c(number=1.0, divisor=5)
# print(result)
# result = safe_division_c(divisor=5, number=2)
# print(result)
# result = safe_division_c(2, divisor=5)
# print(result)


## 4. / 사용하여 위치로만 지정하는 인자 지정
# """
# 해결: 파이썬 3.8 이상. 위치로만 지정하는 인자 지정
# 인자 목록의 / 기호는 위치로만 지정하는 인자의 끝을 표시한다.

# 또 다른 문제: 호출하는 쪽에서 함수의 맨 앞에 있는 두 필수 인자(number, divisor)를 호출하면서
# 위치와 키워드를 혼용할 수 있다.
# 이 필수 인자들의 이름이 변경되기라도 하면 기존 호출 코드가 깨질 수도 있다.
# """


# def safe_division_d(
#     number, divisor, /, *, ignore_overflow=False, ignore_zero_division=False  # * 추가
# ):
#     """number를 divisor로 나눈다

#     Parameters:
#         number: 피제수
#         divisor: 제수
#         ignore_overflow: True면 나눗셈의 오버플로우를 무시하고 0을 반환
#         ignore_zero_division: True면 0으로 나눈 경우 오류 무시하고 무한대 반환


#     Returns:
#         float: 나눗셈 결과
#     """
#     try:
#         return number / divisor
#     except OverflowError:
#         if ignore_overflow:
#             return 0
#         else:
#             raise
#     except ZeroDivisionError:
#         if ignore_zero_division:
#             return float("inf")
#         else:
#             raise


# # 맨 두 필수 인자들의 위치와 키워드 인자 혼용
# # result = safe_division_d(number=1.0, divisor=5)  # error
# # print(result)

# result = safe_division_d(5, 2)
# print(result)
# result = safe_division_d(5, 0, ignore_zero_division=True)
# print(result)

## 5. 섞어 쓰기
"""
인자 목록에서 /와 * 기호 사이에 있는 모든 파라미터는 위치를 사용해 전달할 수도 있고
이름을 키워드로 사용해 전달할 수 있다.
"""


def safe_division_e(
    numerator,
    denominator,
    /,
    ndigits=10,
    *,
    ignore_overflow=False,
    ignore_zero_division=False,  # * 추가
):
    """number를 divisor로 나눈다
    
    Parameters:
        numerator: 피제수
        denominator: 제수
        ndigits: 얼마나 많은 자릿수를 사용할지
        ignore_overflow: True면 나눗셈의 오버플로우를 무시하고 0을 반환
        ignore_zero_division: True면 0으로 나눈 경우 오류 무시하고 무한대 반환
    
    
    Returns:
        float: 나눗셈 결과
    """
    try:
        fraction = numerator / denominator
        return round(fraction, ndigits)
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float("inf")
        else:
            raise


# ndigits는 위치나 키워드를 사용해 전달할 수 있는 선택적인 파라미터
result = safe_division_e(22, 7)
print(result)

result = safe_division_e(22, 7, 5)
print(result)

result = safe_division_e(22, 7, ndigits=2)
print(result)
