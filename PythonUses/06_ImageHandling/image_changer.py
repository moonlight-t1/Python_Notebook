import os
from PIL import Image
import argparse

path = os.getcwd() + "\\PythonUses\\Images\\"


# 파일 목록 가져오기
def search_dir(dirname):
    result_file_list = []  # 파일들의 경로가 담기는 리스트

    filenames = os.listdir(dirname)  # dirname에 있는 폴더와 파일 목록을 저장
    for filename in filenames:
        full_path = os.path.join(dirname, filename)  # 전체 파일 경로 완성

        if os.path.isdir(full_path):  # full path가 dir이라면 재귀 호출
            if filename != "convert":
                # 재귀 함수에서 리턴되는 값들이 extend
                result_file_list.extend(search_dir(full_path))
        else:
            result_file_list.append(full_path)  # 파일이라면 파일 경로를 리스트에 append
    return result_file_list


# 인자 받기
p = argparse.ArgumentParser()
p.add_argument("-f", type=str)
p.add_argument("-e", type=str)
args = p.parse_args()

if args.f is None or args.e is None:
    print("사용법: python image_changer.py -f <대상폴더> -e <변환될확장자>")
else:
    new_format = args.e

    if new_format[0] != ".":
        new_format = "." + new_format

    file_list = search_dir(args.f)

    for file in file_list:
        new_folder = os.path.split(
            file)[0] + "\\convert"  # convert된 파일들이 저장될 폴더
        # 폴더가 존재하지 않는다면 폴더 생성
        if not os.path.exists(new_folder):
            os.mkdir(new_folder)
        src_filename = os.path.splitext(file)[0]  # a.jpg에서 a

        new_file = new_folder + "\\" + \
            src_filename.split("\\")[-1] + "_converted" + \
            new_format  # a.jpg -> a.png

        try:
            img = Image.open(file)  # 파일 열기
            img.verify()  # 이미지의 유효성 검사(pillow) 이미지인지 아닌지 판단
            img.close()  # 이미지 유효성 검사를 하면 이미지를 닫고 다시 열어줘야 한다.

            img = Image.open(file)  # 파일 열기
            img.save(new_file)  # 파일 저장
        except:
            pass
