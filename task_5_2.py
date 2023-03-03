sl = input()
gl = 0
sgl = 0
count = 0
cnt_a = sl.count("a")
cnt_e = sl.count("e")
cnt_i = sl.count("i")
cnt_o = sl.count("o")
cnt_u = sl.count("u")
gl = cnt_a + cnt_e + cnt_i + cnt_o + cnt_u
sgl = len(sl) - gl
print("Total gl: " + str(gl))
print("Total sgl: " + str(sgl))
if cnt_a:
    print("a:" + str(cnt_a))
else:
    print("a - false")
if cnt_e:
    print("e:" + str(cnt_e))
else:
    print("e - false")
if cnt_i:
    print("i:" + str(cnt_i))
else:
    print("i - false")
if cnt_o:
    print("o:" + str(cnt_o))
else:
    print("o - false")
if cnt_u:
    print("u:" + str(cnt_u))
else:
    print("u - false")