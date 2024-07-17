# 2007년 1924
x,y = map(int, input().split())
d = 0
x_list = [31,28,31,30,31,30,31,31,30,31,30,31]
w_list = ['SUN','MON','TUE','WED','THU','FRI','SAT']

for i in range(x-1):
    d = d + x_list[i]
d = (d+y) % 7
print(w_list[d])