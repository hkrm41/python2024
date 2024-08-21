# num=range(2,11,2)
# print(num)
# print(list(num))
# for i in range(10):
#     print(i)
# num=(1,2,3,4,5)
# print(type(num))
# for i in num:
#     print(i)
def p(space,space_num,*args):
    str=args[0]
    for i in range(1, len(args)):
        str=str+(space*space_num)+args[i]
    print(str)
p(',',3,"👍","🙌",'😊')