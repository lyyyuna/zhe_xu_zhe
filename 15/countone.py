def count(num):
    cnt = 0
    print '{0:b}'.format(num)
    while num:
        cnt +=1 
        num = num & (num-1)
    return cnt


print count(15)