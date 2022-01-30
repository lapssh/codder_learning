# sign(x)=1, если x>0,
#
# sign(x)=-1, если x<0,
#
# sign(x)=0, если x=0.

x = int(input())
if x > 0:
    sign_x = 1
elif x < 0:
    sign_x = -1
else:
    sign_x = 0
print(sign_x)
