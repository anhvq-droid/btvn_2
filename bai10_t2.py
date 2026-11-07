ox, oy = map(int, input("nhap toa do tam O, xO yO lan luot la : ").split())
r = int(input("nhap ban kinh duong tron tam O: "))
xa, ya = map(int, input("nhap toa do diem A, xA yA lan luot la: ").split())
o_a = ((ox-xa)**2 + (oy-ya)**2)**0.5
if o_a == r:
    print("diem A nam tren duong tron")
else:
    print("diem A ko thuoc duong tron")