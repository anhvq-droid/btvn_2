s = int(input("nhap so giay: "))
h = s // 3600
m = (s % 3600) // 60
print(h, "gio", m, "phut", s % 60, "giay")
