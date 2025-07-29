s1=str(input("Nhap chuoi thu nhat: "))
s2=str(input("Nhap chuoi thu hai: "))
daos1 = s1[::-1]
print(daos1)

a=int(input("Nhap a: "))
while a<1 :
     a=int(input("Nhap lai a: "))
b=int(input("Nhap b: "))
while b>len(s2):
     b=int(input("Nhap lai b: "))
s2moi = s2[:a-1] + s2[a-1:b][::-1] + s2[b:]
print("Chuỗi sau khi đổi:", s2moi)

s3=s1[::2]
print("Chuoi sau khi xoa cac ki tu vi tri chan:",s3)

danxen = min(len(s1), len(s2))
s4 = ""
for i in range(danxen):
    s4 += s1[i] + s2[i]
s4 += s1[danxen:] + s2[danxen:]
print("Chuỗi s4:", s4)



