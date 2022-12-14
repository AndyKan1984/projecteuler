def findDivisbles(max_range,divisibles):
    list_numbers = list()
    for i in range(2, max_range):
        for d in divisibles:
            if i%d==0:
                list_numbers.append(i)
                break
    return list_numbers

def sumList(array_list):
    sum=0
    for i in array_list:
        sum+=i
    return sum

if 233168 == sumList(findDivisbles(1000,[3,5])):
    print('test passed!')
else:
    print('test failed!!')
