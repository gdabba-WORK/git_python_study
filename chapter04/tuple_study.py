tuple1 = (1, 2, 3, 4)
print("tuple1 {} type : {}".format(tuple1, type(tuple)))
tuple2 = 5, 6, 7, 8
print("tuple2 {} type : {}".format(tuple2, type(tuple2)))
tuple3 = (9,)
print("tuple3 {} type : {}".format(tuple3, type(tuple3)))
tuple4 = 10,
print("tuple {} type : {}".format(tuple4, type(tuple4)))

t_list = [tuple1, tuple2]
t_list.extend([tuple3, tuple4])
print(t_list)

i = 1
for t in t_list:
    print("{} item : {}".format(i, t))
    i += 1
