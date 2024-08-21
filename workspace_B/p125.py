def sum(*numbers):
    sum_value=0
    for number in numbers:
        sum_value=sum_value+number
    return sum_value
result=sum(1,3,5,7,9,11)
print(result)