k=int(input("Nhap k: "))
a=[]
for i in range(k):
    x = int(input("Nhap phan tu thu {}: ".format(i+1)))
    a.append(x)
print("LIST vua nhap: ", a)

n=int(input("Nhap n: "))
m=int(input("Nhap m: "))
if n * m > len(a):
    print("NO")
else:
    X = []  
    vitri = 0
    for i in range(n):
        Y= []
        for j in range(m):
            Y.append(a[vitri])
            vitri += 1
        X.append(Y)
    print("Ma trận X:")
    for Y in X:
        print(Y)