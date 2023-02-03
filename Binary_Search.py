number=int(input("Enter your number: "))
my_list1=[1,2,3,4,5]
low=0
high=len(my_list1)-1
flag=True
while flag:
    if (number>my_list1[high]) or (number<my_list1[low]):
        number=int(input("Enter again number!!!: "))
    else:
        flag=False
    
while low<=high:
    mid=(low+high)//2
    if my_list1[mid]==number:
            print(mid)
            break
    elif my_list1[mid]>number:
            high=mid-1
    elif my_list1[mid]<number:
            low=mid+1
           


    
                