def find_selfNumber():
    n=1 #초기값
    notSelf=[] #셀프넘버가아닌 숫자 리스트 
    while n<10001:
        result=n
        for i in str(n):
            result+=int(i)
        notSelf.append(result)
        n+=1

    nums=[i for i in range(1,10001)]
    result_list= list(sorted((set(nums)-set(notSelf))))

    for i in result_list:
        print(i)

find_selfNumber()

        
