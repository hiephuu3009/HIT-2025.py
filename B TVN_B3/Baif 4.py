#Dùng hàm có sẵn
def chuanhoa(hoten: str) -> str:   
    Ten = hoten.strip().split()  
    Ten = [ten.capitalize() for ten in Ten]   
    return " ".join(Ten)
if __name__ == "__main__":
    s = input("Nhập họ tên: ")
    print(chuanhoa(s))