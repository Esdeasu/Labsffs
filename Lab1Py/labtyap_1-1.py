a = float(input("input a - "))
b = float(input("input b - "))
c = float(input("input c - "))
d = float(input("input d - "))
k = float(input("input k - "))
if b == 0 or a == 0:
    print("A=0 or B=0. Error")
else:
    vir = ((a**2-b**3 - c**3*a**2)*(b-c+c*(k-d/b**3)) - (k/b -k/a)*c)**2 - 20000
if vir < 0:
    vir = -vir
    print(vir)
