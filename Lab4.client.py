import socket
bred = socket.socket()
bred.connect(('localhost', 7890))

s = []
a = input("input a - ")
b = input("input b - ")
c = input("input c - ")
d = input("input d - ")
k = input("input k - ")
s.append(a)
s.append(b)
s.append(c)
s.append(d)
s.append(k)
s = str(s)
if b == 0 or a == 0:
    print("A=0 or B=0. Error")
else:
    bred.send(s.encode())

res = bred.recv(34000)
res = res.decode()
bred.close()
print(res)
