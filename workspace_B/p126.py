def min_max(*numbers):
    min_value=numbers[0]
    max_value=numbers[0]
    for number in numbers:
        if min_value>number:
            min_value=number
        if max_value<number:
            max_value=number
    return min_value,max_value

result=min_max(10,2,3,4,5,6,7,8,9)
print(result)
a,b=min_max(234,456,678,123)
print("최솟값:",a,"최댓값",b)