def gyorshatvany(alap,exp,mod):
    alap=alap%mod
    if (exp==0):
        return 0
    elif (exp==1):
        return alap
    elif (exp%2==0):
        return gyorshatvany(alap*alap%mod,exp/2,mod)
    else:
        return alap*gyorshatvany(alap,exp-1,mod)%mod


if __name__=="__main__":
    print(gyorshatvany(129,97,171))