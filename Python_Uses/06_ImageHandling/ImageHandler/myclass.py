from PIL import Image
import os


class MyImage:
    def __init__(self, **kwargs):
        # 키워드 형 인자로 folder와 resize를 받는다
        self.folder = kwargs.get("folder", None)
        self.resize = kwargs.get("resize", False)

        # 기본 사이즈
        self.r_width = kwargs.get("r_width", 500)
        self.r_height = kwargs.get("r_height", 500)

        # 변경될 확장자
        self.ext = kwargs.get("ext", None)

        # 새 폴더
        self.newfolder = "__convert__"
        self.path_separator = "\\"

    # 이미지 유효성 검사
    def is_valid_image(self, filename):
        try:
            img = Image.open(filename)
            img.verify()
            img.close()
            return True
        except:
            return False

    # 파일 목록 가져오기
    def search_dir(self, dirname):
        result_file_list = []  # 파일들의 경로가 담기는 리스트

        filenames = os.listdir(dirname)  # dirname에 있는 폴더와 파일 목록을 저장
        for filename in filenames:
            full_path = os.path.join(dirname, filename)  # 전체 파일 경로 완성

            if os.path.isdir(full_path):  # full path가 dir이라면 재귀 호출
                if filename == self.newfolder:
                    continue
                # 재귀 함수에서 리턴되는 값들이 extend
                result_file_list.extend(self.search_dir(full_path))
            else:
                result_file_list.append(full_path)  # 파일이라면 파일 경로를 리스트에 append
        return result_file_list

    # 확장자 변경
    def change_format(self, img, filename, ext):
        new_folder = os.path.split(
            filename)[0] + self.path_separator + self.newfolder
        if not os.path.exists(new_folder):
            os.mkdir(new_folder)

        src_filename = os.path.splitext(filename)[0]
        new_filename = new_folder + self.path_separator + \
            src_filename.split(self.path_separator)[-1] + ext
        img.save(new_filename)

    # 리사이즈
    def resize_image(self, filename):
        img = Image.open(filename)
        width, height = img.size
        if width < height:                      # 세로가 더 길 경우
            aspect = height / self.r_height     # 축소 비율
            new_width = int(width / aspect)     # 비율만큼 width 값도 변경
            new_height = self.r_height
        else:                                   # 가로가 더 길 경우
            aspect = width / self.r_width
            new_width = self.r_width
            new_height = int(height / aspect)

        new_size = (new_width, new_height)
        return img.resize(new_size)

    # 시작 함수
    def start(self):
        cnt_resize = 0
        cnt_format = 0

        if self.ext is None and self.resize is False:
            return

        file_list = self.search_dir(self.folder)

        for file in file_list:
            # 리사이즈
            if not self.is_valid_image(file):
                continue
            if self.resize:
                img = self.resize_image(file)
                cnt_resize += 1
            else:
                img = Image.open(file)

            # 확장자 변경
            if self.ext is None:
                ext = str(file.split(self.path_separator)[-1]).split(".")[-1]
            else:
                ext = self.ext
                cnt_format += 1

            if ext[0] != ".":
                ext = "." + ext
            self.change_format(img, file, ext)
        return (cnt_resize, cnt_format)
