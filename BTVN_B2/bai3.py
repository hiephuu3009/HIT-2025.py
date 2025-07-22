def dem_va_tong(n):
    dem = 0
    tong = 0
    while n > 0:
        chu_so = n % 10
        tong += chu_so
        dem += 1
        n //= 10
    return dem, tong

if __name__ == "__main__":
    n = int(input("Nhap n = "))
    if n <= 0:
        print("n phai >0")
    else:
        dem, tong = dem_va_tong(n)
        print(f"So luong chu so cua {n} la : {dem}")
        print(f"Tong cac chua so cua {n} la : {tong}")
