import os
from chardet import detect  # 인코딩 확인
import argparse

# 현재 파이썬 파일 절대경로 + text폴더 경로
# path = str(os.path.dirname(os.path.abspath(__file__))) + "\\text"


# 재귀 호출을 이용해 파일 명만 리스트에 담는다
def search_dir(dirname):
    result_list = []
    filenames = os.listdir(dirname)

    for filename in filenames:
        full_path = os.path.join(dirname, filename)

        # 디렉토리라면 재귀호출 아니고 파일이면 append
        if os.path.isdir(full_path):
            result_list.extend(search_dir(full_path))
        else:
            result_list.append(full_path)

    return result_list


# 인코딩 확인
def get_encoding_type(filepath):
    with open(filepath, "rb") as f:
        rawdata = f.read()

    codec = detect(rawdata)
    return codec["encoding"]


INCLUDE_EXT_LIST = [".txt", ".pdf"]  # 확장자

# parse 옵션
parse = argparse.ArgumentParser()
parse.add_argument("-f", type=str)  # 파일 경로 (str)
parse.add_argument("-e", nargs="+")  # 여러개 입력 가능하게 함 -e .txt .smi
args = parse.parse_args()  # 실행


if args.f is not None:  # 파일경로가 None이 아니라면
    path = args.f
    filelists = search_dir(path)

    if args.e is not None:  # 확장자명이 None이 아니라면
        if len(args.e) > 0:
            # INCLUDE_EXT_LIST = []
            # for e in args.e:
            #     if e[0:1] == ".":
            #         INCLUDE_EXT_LIST.append(e)
            #     else:
            #         INCLUDE_EXT_LIST.append("." + e)

            # 다음과 같이 대체 가능하다
            INCLUDE_EXT_LIST = [e.lower() if e[0:1] == "." else ".{}".format(
                e.lower()) for e in args.e]
            print(INCLUDE_EXT_LIST)

    for file in filelists:
        filename, ext = os.path.splitext(file)  # 파일명과 확장자명 분리

        tempfile = filename + "_tmp" + ext  # 임시 파일명
        if ext.lower() in INCLUDE_EXT_LIST:  # 확장자가 포함이 되면
            encoding = get_encoding_type(file)  # 인코딩을 가져온다
            if encoding.lower().find("utf") < 0:  # utf 파일이 아니라면 유니코드로 바꿔준다
                try:
                    with open(file, "r") as read, open(tempfile, "w", encoding="utf-8") as write:
                        write.write(read.read())  # read 파일에서 내용을 읽어 write를 한다

                    os.unlink(file)  # 원본 파일 삭제
                    os.rename(tempfile, file)  # 임시파일명을 원본파일명으로 바꿔준다
                    print("{} 이 저장되었습니다.".format(file))
                except:
                    pass
                finally:
                    if os.path.exists(tempfile):
                        os.unlink(tempfile)
