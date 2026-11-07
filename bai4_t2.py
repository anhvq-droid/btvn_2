a,b = map(float,input("nhap 2 he so a b theo thu tu cua phuong trinh ax + b = 0: ").split())
if a == 0:
    if b == 0:
        print("phuong trinh co vo so nghiem")
    else:
        print("phuong trinh vo nghiem")
else:
    x = -b/a
    print("phuong trinh co nghiem duy nhat la: ", f"{x:.2f}")