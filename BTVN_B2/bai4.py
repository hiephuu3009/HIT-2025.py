def sochai(N):
    mua = N // 28
    chai = mua
    vo = mua

    while vo >= 3:
        doi = vo // 3
        chai += doi
        vo = vo % 3 + doi  

    return chai

if __name__ == "__main__":
    N = int(input("Nhap xu ban co:  "))
    so_chai = sochai(N)
    print(f"Tong so chai co the uong: {so_chai}")
