a, b, c = map(float, input("nhap 3 canh cua tam giac: ").split())
if a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0:
    if a == b == c:
        print("tam giac deu")
    elif a == b or a == c or b == c:
        print("tam giac can")
    else:
        print("tam giac thuong")
    print("chu vi tam giac la: ", f"{a + b + c:.2f}")
    print("dien tich tam giac la: ", f"{((a + b + c) / 2 * ((a + b + c) / 2 - a) * ((a + b + c) / 2 - b) * ((a + b + c) / 2 - c)) ** 0.5:.2f}")
else:
    print("khong phai 3 canh cua 1 tam giac")