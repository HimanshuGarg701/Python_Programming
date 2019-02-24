# some unique lists 
# ==================make ["1a","2a","3a","4a"] =============================================================
x = []
for i in range(1,5):
    i = str(i)
    i = i + "a"
    x.append(i)
print(x)


# ================= make ["ab", "ac", "ad", "bb", "bc", "bd"] ================================================
y = []
for j in range(97,99):
    for k in range(98,101):
        if j == 97:
            z = chr(j) + chr(k)
            y.append(z)
        elif j ==98:
            m = chr(j) + chr(k)
            y.append(m)
print(y)


# =======================print even numbered elements of above list =========================================
for i in range(1,6,2):
    print(y[i], end=", ")
