from collections import defaultdict


def open_picture(profile_path):
    try:
        return open(profile_path, "a+b")
    except OSError:
        print(f"경로를 열 수 없습니다: {profile_path}")
        raise


class Pictures(dict):
    def __missing__(self, key):  # dict에 키가 없는 경우 처리
        value = open_picture(key)
        self[key] = value
        return value


path = "1.jpg"
pictures = Pictures()
handle = pictures[path]
handle.seek(0)
image_data = handle.read()
