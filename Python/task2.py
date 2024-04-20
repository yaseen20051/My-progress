check_1=[]
check_2=[]
a = []
test_cases=0
n=0
while (test_cases>100) or (test_cases<1):
 test_cases = int(input())
for i in range(test_cases):
    while (n>100) or (n<2):
     n = int(input())
    b=list(input().split(' '))
    for nums in b:
      a.append(int(nums))# to add integers in alist in one line seprated by a space tab
    k=n-1
    while(a[k]>0):
        if (a[k]>=a[k-1]):
         a[k]=a[k]-a[k-1]
        else:
         a[k-1] = abs(a[k] - a[k - 1])
        if (a[k]==0) or (a[k]==-1) :
            check_1.append(1)
            k=k-1
        if(a[k]<-1):
            check_2.append("NO")
            break
        if (k==0) :
            break

    if (len(check_1)==n-1):
        check_2.append("YES")
    else:
        check_2.append("NO")
    a=[]
    check_1=[]
    n=0
for counter_2 in check_2:
    print(counter_2)
