N = int(input("Nhap so phan tu N: "))
lst = []
for i in range(N):
    x = int(input("Nhap phan tu thu {}: ".format(i+1)))
    lst.append(x)
print("LIST vua nhap: ", lst)
X=int(input("Nhap so X: "))
print('So lan xuat hien cua',X,'trong LIST: ', lst.count(X))
lst2=[8, 5, 4, 0, 1, 3]
lst[2:8]=lst2
print(lst)
print("So lon nhat trong LIST:",max(lst))
Y=int(input("Nhap so Y: "))
lst.insert(0,Y)
print("LIST sau khi chen: ",lst)
saptang = True
sapgiam = True
for i in range(len(lst) - 1):
    if lst[i] < lst[i+1]:
        sapgiam = False
    elif lst[i] > lst[i+1]:
        saptang = False
if saptang:
    print("TĂNG")
elif sapgiam:
    print("GIẢM")
else:
    print("NO")