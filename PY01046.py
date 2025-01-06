def thap_ha_noi(n, a, b, c):
  if n == 1:
    print(f"{a} -> {c}")
  else:
    thap_ha_noi(n-1, a, c, b)
    print(f"{a} -> {c}")
    thap_ha_noi(n-1, b, a, c)

n = int(input()) # số lượng đĩa
thap_ha_noi(n, 'A', 'B', 'C')