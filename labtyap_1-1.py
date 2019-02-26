a = int(input("введите а - ")) 
b = int(input("введите b - ")) 
c = int(input("введите c - ")) 
d = int(input("введите d - ")) 
k = int(input("введите k - ")) 
if b==0 or a==0: print("A=0 или B=0, деление на 0") 
else: 
    vir = pow((pow(a,2)-pow(b,3)-pow(c,3)*pow(a,2)) * (b-c+c*(k-(d/pow(b,3)))) - (k/b-k/a)*c,2) - 20000 
    if vir<0: vir=-vir 
    print(vir)
