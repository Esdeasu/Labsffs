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
bred.send(s.encode())

res = bred.recv(34000)
res = res.decode()
bred.close()
print(res)
