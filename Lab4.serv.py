import socket
import re

bred = socket.socket()
bred.bind(('', 7890))
bred.listen(1)
serv, addr = bred.accept()
while True:
    print('Ожидание соединения...')
    data = serv.recv(34000)
    print('Соединение установлено.')
    data = data.decode()
    data = re.findall(r'\d+', data)
    a = float(data[0])
    b = float(data[1])
    c = float(data[2])
    d = float(data[3])
    k = float(data[4])
    
    if a == 0 or b == 0:
        o = 'Ошибка: деление на ноль'
        serv.send(o.encode())
    else:
        res = ((a**2-b**3 - c**3*a**2)*(b-c+c*(k-d/b**3)) - (k/b - k/a)*c)**2 - 2000
        res = 'Ответ = ' + str(res)
        serv.send(res.encode())
    if not data:
        w = 'wtf men'
        serv.send(w.encode())
    break
