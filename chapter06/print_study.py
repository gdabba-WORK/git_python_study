print("test", "test1", sep="")
print("%s %d" %('test', 10))

a = 0.123456789
print("{0:.2f}, {0:.5f}".format(a))

# lists = [100, 200, 300]
# print("{0} {1} {2}".format(lists))

print("{0:2d}, {0:02d}, {0:<5d}, {0:>5d}".format(3))
print("{0:,d}, {1:.1%}".format(1234567, 0.5))
print("16진수 : {0:#x}, 8진수 : {0:#o}, 2진수 : {0:#b}".format(32))
print("16진수 : {0:x}, 8진수 : {0:o}, 2진수 : {0:b}".format(32))