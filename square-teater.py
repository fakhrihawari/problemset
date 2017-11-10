def flag(a,b,c):

    if (a%c==0):
        x=a/c
    else:
        x = a / c
        x=x+1
    if (b % c == 0):
        x = a / c
    else:
        y = b / c
        y = y + 1
    j=x*y
    # print j
    return j
# print flag(6,6,4)

# n,m,a = map(int,raw_input().split())
#
# if (n % a == 0):
#     x = n / a
# else:
#     x = n / a
#     x = x + 1
# if (m % a == 0):
#     x = m /a
# else:
#     y = m / a
#     y = y + 1
# j = x * y
# print j

n,m,a = map(int,raw_input().split())
if n%a == 0:
    k = 0
else:
    k = 1
if m%a == 0:
    p = 0
else:
    p = 1
x = (n/a)+k
y = (m/a)+p
print x*y

