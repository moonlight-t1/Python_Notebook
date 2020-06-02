from pynput.keyboard import Key, Listener, KeyCode
import win32api  # To use Windows library

# 어떤 키를 누르면 어떤 함수를 호출되게 만든다
MY_HOT_KEYS = [
    {"function1": {Key.alt_l, KeyCode(char="c")}},
    {"function2": {Key.alt_l, KeyCode(char="n")}},
    {"function3": {Key.alt_l, KeyCode(char="g")}},
]

# 키를 누르고 있으면 계속 입력이 되므로
# 이를 방지하기 위해집합으로 만든다
current_keys = set()


def function1():
    print("계산기 실행")
    win32api.WinExec("calc.exe")


def function2():
    print("메모장 실행")
    win32api.WinExec("notepad.exe")


def function3():
    print("크롬 실행")
    win32api.WinExec(
        "c:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")


def key_pressed(key):
    print("Pressed {}".format(key))
    for data in MY_HOT_KEYS:
        FUNCTION = list(data.keys())[0]
        KEYS = list(data.values())[0]  # 딕셔너리를 리스트로 형변환

        if key in KEYS:  # 현재 눌린 키가 KEYS에 있으면 add를 한다
            current_keys.add(key)
            # checker = True
            # for k in KEYS: # 현재 눌린키가 단축키 모두를 누르지 않으면 작동을 안하게 한다
            #     if k not in current_keys:
            #         checker = False
            #         break
            # if checker: # 단축키의 모든 키가 눌리면 함수 동작
            #     function = eval(FUNCTION)
            #     function()

            if all(k in current_keys for k in KEYS):  # 하나라도 false면 작동 안한다
                function = eval(FUNCTION)
                function()


def key_released(key):
    print("Released {}".format(key))

    # 키를 떼면 remove 해준다
    if key in current_keys:
        current_keys.remove(key)

    if key == Key.esc:
        return False


with Listener(on_press=key_pressed, on_release=key_released) as listner:
    listner.join()
