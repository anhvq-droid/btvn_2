print("nhap he so a b m c d n theo thu tu cua he phuong trinh ax + by = m va cx + dy = n: ")
a, b, m, c, d, n = map(float, input().split())
if a * d - b * c == 0:
    if a * n - m * c == 0 and b * n - m * d == 0:
        print("he phuong trinh co vo so nghiem")
    else:
        print("he phuong trinh vo nghiem")
else:
    x = (m * d - b * n) / (a * d - b * c)
    y = (a * n - m * c) / (a * d - b * c)
    print("he phuong trinh co nghiem duy nhat la: ", f"x = {x:.2f}, y = {y:.2f}")