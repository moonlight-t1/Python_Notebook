import ftplib
from tqdm import tqdm
import os


# 파일인지 폴더인지 구분하기 위해
# 파일이 아니라 폴더면 에러발생
def is_file(ftp, filename):
    current = ftp.pwd()
    try:
        ftp.cwd(filename)
    except:
        ftp.cwd(current)
        return True
    ftp.cwd(current)  # 처음 경로로 이동
    return False


FTP_SERVER = ""  # FTP 서버 IP
FTP_PORT = 6500  # FTP 서버 PORT
FTP_ID = ""  # 아이디
FTP_PASS = ""  # 비밀번호

ftp = ftplib.FTP()
ftp.encoding = "euc-kr"  # 윈도우 한글 인코딩
ftp.connect(FTP_SERVER, FTP_PORT)
print(ftp.login(FTP_ID, FTP_PASS))

while True:
    current = ftp.pwd()  # 현재 경로
    cmd = input("FTP {}> ".format(current))
    args = cmd.split(" ")
    if len(args) <= 0:
        continue

    command = args[0]
    del args[0]
    if command == "exit":
        break

    # 폴더 목록
    if command == "dir" or command == "ls":
        lists = ftp.nlst()
        for l in lists:  # 파일인 경우
            if is_file(ftp, l):
                print(l)
            else:  # 폴더인 경우
                print("{}{}/".format(current, l))

    # 폴더 이동
    elif command == "cd":
        target = args[0]
        if not is_file(ftp, target):
            ftp.cwd(target)

    # 폴더 만들기
    elif command == "mkdir" or command == "mk":
        target = args[0]
        ftp.mkd(target)

    # 삭제
    elif command == "delete" or command == "del":
        target = args[0]
        ftp.delete(target)

    # 업로드
    elif command == "up":
        target = args[0]
        size = os.path.getsize(target)  # 업로드할 파일의 사이즈
        filename = target.split("\\")[-1]  # 파일 이름(윈도우 기준), 경로에서 맨 마지막 이름
        # 프로그레스바
        with open(target, "rb") as file:
            with tqdm(unit='blocks', unit_scale=True, leave=True, miniters=1, desc="Uploading...", total=size) as tq:
                def callback(data):
                    tq.update(len(data))

                # blocksize(2048): 데이터를 전송하는 패킷의 크기 설정
                ftp.storbinary("STOR " + filename, file,
                               2048, callback=callback)

    # 다운로드
    elif command == "down":
        target = args[0]
        with open(target, "wb") as file:
            size = ftp.size(target)  # 다운로드 받을 파일의 사이즈
            # 프로그레스바
            with tqdm(unit='blocks', unit_scale=True, leave=True, miniters=1, desc="Downloading...", total=size) as tq:
                # 콜백 함수는 무언가에 의해 호출되는 함수이다
                def callback(data):
                    tq.update(len(data))  # 프로그레스바 업데이트
                    file.write(data)
                ftp.retrbinary("RETR " + target, callback=callback)

ftp.close()
