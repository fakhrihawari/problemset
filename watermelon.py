##x= input("");
# x= int(x);
# if (x%2!=0):
#     print "NO";
# elif(x<=2):
#     print "NO";
# else:
#     print "YES"
##if x%2==0 and x>2:
##    print "YES";
##else:
##    print "NO";

def solution(a,x):
    n=len(a)
    if n==0:
        return -1
    l=0
    r=n-1;
    while l<r :
        m =(l+r)//2
        if a[m] != x:
            r=m-1
        else:
            l=m

    if a[l]==x:
        return l
    return -1
a=[1,2,5,9,9]
print solution(a,1)



