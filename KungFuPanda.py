def KFP_slow(n):
    if n==1:
        return 1
        else:
            if n==2:
                return 2
            else:
                if n==3:
                    return 4
                else:
                    return KFP_slow(n-1)+KFP_slow(n-2)+KFP_slow(n-3)

dic={1:1,2:2,3:4}

def KFP_fast(n):
    if n in dic:
        return dic[n]
    ans1=KFP_fast(n-1)
    dic[n-1]=ans1
    ans2=KFP_fast(n-2)
    dic[n-2]=ans2
    ans3=KFP_fast(n-3)
    dic[n-3]=ans3
