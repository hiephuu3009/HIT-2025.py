def nhapnam(nam):
    return (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)

def ngay(thang, nam):
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang in [4, 6, 9, 11]:
        return 30
    elif thang == 2:
        if nhapnam(nam):
            return 29
        else:
            return 28
    else:
        return -1  

if __name__=='__main__':
    thang = int(input("Nhap thang (1-12): "))
    nam = int(input("Nhap nam: "))
    so_ngay = ngay(thang, nam)
    if so_ngay == -1:
        print("Thang khong hop le.")
    else:
        print(f"Thang {thang} nam {nam} co {so_ngay} ngay.")
