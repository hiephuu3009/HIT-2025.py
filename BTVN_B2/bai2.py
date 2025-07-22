def thueluong(luong):
    if luong >= 15000000:
        return luong * 0.30
    elif luong >= 7000000:
        return luong * 0.20
    else:
        return luong * 0.10
def main():
    ten = input("Nhap ten nhan vien: ")
    luong = float(input("Nhap luong: "))
    thue = thueluong(luong)
    luong_rong = luong - thue
    print("\n--- BANG TINH---")
    print(f"Ten nhan vien: {ten}")
    print(f"Luong thue  : {luong:,.0f} VND")
    print(f"Thue : {thue:,.0f} VND")
    print(f"Luong rong  : {luong_rong:,.0f} VND")
if __name__ == "__main__":
    main()
