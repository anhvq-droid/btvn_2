a,b,c = map(float,input("nhap 3 he so a, b, c theo thu tu cua phuong trinh ax2 + bx + c = 0: ").split())
delta = b**2 - 4*a*c
if delta > 0:
    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)
    print("phuong trinh co hai nghiem phan biet la: ", f"{x1:.2f} va {x2:.2f}")
elif delta == 0:
    x = -b / (2*a)
    print("phuong trinh co nghiem kep la: ", f"{x:.2f}")
else:
    print("phuong trinh vo nghiem")