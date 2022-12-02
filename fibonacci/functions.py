def fibonacci(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        num += 1
        arr = []
        arr.append(0)
        arr.append(1)
        for i in range(2,num):
            arr.append(arr[i-1]+arr[i-2])
        return arr[num-1]

