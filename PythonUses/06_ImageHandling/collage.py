import os
import cv2
import numpy as np
import mimetypes  # 확장자 확인 라이브러리

path = os.getcwd() + "\\PythonUses\\Videos\\"
filepath = path + "1.mp4"


def get_video(filepath, capture_count=1):
    images = []

    cap = cv2.VideoCapture(filepath)  # 비디오 정보
    v_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    v_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    v_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    v_fps = cap.get(cv2.CAP_PROP_FPS)
    v_duration = v_frames / v_fps

    # 구간
    jump_frame = int(v_frames / capture_count)

    for i in range(capture_count):
        pos = 1 + (jump_frame * i)
        cap.set(cv2.CAP_PROP_POS_FRAMES, pos)  # 캡쳐할 위치로 pos 점프
        ret, frame = cap.read()  # 이미지 가져오기
        if ret:
            images.append(frame)
    cap.release()  # cap은 다쓰면 release를 해줘야 한다
    return images


# 콜라쥬 만들기
# thumb_size는 한 칸의 크기, rowcols는 칸의 갯수
def create_collage(image_list, thumb_size=(210, 137), rowcols=(5, 5)):
    canvas_width = thumb_size[0] * rowcols[0]
    canvas_height = thumb_size[1] * rowcols[1]
    canvas = np.zeros(shape=(canvas_height, canvas_width, 3),
                      dtype=np.uint8)  # 넘파이
    canvas.fill(255)  # 배경 하얀색

    cursor = [0, 0]  # 각 칸을 기억할 변수

    for img in image_list:
        img = cv2.resize(img, thumb_size)  # 리사이즈
        # image[y: y+h, x: x+w]
        # 높이 / 폭, cursor[0]은 가로, cursor[1]은 세로
        canvas[cursor[1]:cursor[1] + thumb_size[1],
               cursor[0]:cursor[0] + thumb_size[0]] = img
        cursor[0] += thumb_size[0]

        # 다음 줄로 이동
        if cursor[0] >= rowcols[0] * thumb_size[0]:
            cursor[1] += thumb_size[1]
            cursor[0] = 0

    return canvas


def search_dir(dirname):
    result_file_lists = []
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filepath = os.path.join(dirname, filename)
        if os.path.isdir(full_filepath):
            result_file_lists.extend(search_dir(full_filepath))
        else:
            # 비디오 파일만 필터링
            # mimetype = "" if mimetpyes.guess_type(full_filepath)[0] is None else mimetypes.guess_type(full_filepath)[0]
            mimetype = mimetypes.guess_type(full_filepath)
            if mimetype[0] is None:
                mimetype = ""
            else:
                mimetype = mimetype[0]

            if mimetype.find("video") >= 0:
                result_file_lists.append(full_filepath)
            result_file_lists.append(full_filepath)
    return result_file_lists


# cv2의 imwrite는 한글 폴더 경로가 있으면 오류가 난다
# 그래서 my_imwrite를 만들어준다
def my_imwrite(filename, img):
    try:
        ext = os.path.splitext(filename)[-1]
        result, buffer = cv2.imencode(ext, img)  # ext로 img를 encode해준다
        if result:
            with open(filename, mode="wb") as f:
                buffer.tofile(f)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


target = path
filelist = search_dir(target)
for file in filelist:
    new_filename = os.path.splitext(file)[0] + ".jpg"
    images = get_video(file, 25)
    canvas = create_collage(images, rowcols=(5, 5))
    my_imwrite(new_filename, canvas)
