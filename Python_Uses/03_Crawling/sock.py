import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IP4, TCP 통신
google_ip = socket.gethostbyname("google.com")  # DNS 서버를 통해 아이피를 알아낸다
sock.connect((google_ip, 80))  # 튜플 형태로 넘겨줘야 하므로 괄호 한번 더, 80 포트

# 루트로 접속, HTTP 1.1 프로토콜 사용해서 요청
# 문자이므로 바이너리로 encode 해야 한다
sock.send("GET / HTTP/1.1\n".encode())
sock.send("\n".encode())

buffer = sock.recv(4096)  # 4096 바이트만큼 receive
buffer = buffer.decode().replace("\r\n", "\n")
sock.close()

print(buffer)

"""
HTTP/1.1 200 OK
Date: Sat, 08 Feb 2020 06:47:20 GMT
Expires: -1
Cache-Control: private, max-age=0
Content-Type: text/html; charset=ISO-8859-1
P3P: CP="This is not a P3P policy! See g.co/p3phelp for more info."
Server: gws
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN
Set-Cookie: 1P_JAR=2020-02-08-06; expires=Mon, 09-Mar-2020 06:47:20 GMT; path=/; domain=.google.com; Secure
Set-Cookie: NID=197=jWJTnUv8nivtBkkpdyTjYhDbyLiuhSGGkMTufJUf_S80PRAQVT4ws_xX8E9NRKVY3JSSB1OcOj9N8bGlvrZB5tMjtfTBQlg0EqEdiQTLTf_DrdxaQUpAWBsp7tRwvttZpTOFobLbj9NHUVJpwGmoZJPu3jN9hj5lnfis291Ls9k; expires=Sun, 09-Aug-2020 06:47:20 GMT; path=/; domain=.google.com; HttpOnly
Accept-Ranges: none
Vary: Accept-Encoding
Transfer-Encoding: chunked
"""
