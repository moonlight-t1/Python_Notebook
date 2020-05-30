import os


def rename_file():
    # 현재 위치(.)의 파일을 모두 가져온다
    for filename in os.listdir("."):
        print(filename)

        # 파일 확장자가 (properties)인 것만 처리
        if filename.endswith("properties"):
            # 파일명에서 AA를 BB로 변경하고 파일명 수정
            new_filename = filename.replace("AA", "BB")
            os.rename(filename, new_filename)


if __name__ == "__main__":
    rename_file()
