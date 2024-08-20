def fibonacci(n):
    assert n>=0 and int(n)==n,"negative or non integer value is not allowed"
    if n in [0,1]:
        return n
    return fibonacci(n-1)+ fibonacci(n-2)

# print(fibonacci(6))
def sumOfDigit(n):
    assert n >=0 and int(n)==n,"assertion error"
    if n in range(0,10):
        return n
    return sumOfDigit(n//10)+sumOfDigit(n%10)


# print(sumOfDigit(2309))

 
def powOfNum(n,ex):
    if ex==0:
        return 1
    elif ex==1:
        return n  
    else:
        return n*powOfNum(n,ex-1)
    
# print(powOfNum(5,2))
    
def GreatestCommonInteger(num1,num2):
    assert  int(num1)==num1 and int(num2)==num2,"Assetion Error"
    if num1<0:
        num1=-1*num1
    if num2<0:
        num2=-1*num2
    result=num1%num2
    if result==0:
        return num2
    return GreatestCommonInteger(num2,result)
    
# print(GreatestCommonInteger(140,12))



def  DecimalToBinary(num):
    if num==1 or num==0:
        return num  
    # remainder=num%2
    return num%2+10*DecimalToBinary(num//2)
# print(DecimalToBinary(5))



myList=[1,2,3,4]
def ReverseOrder(list,length):
    if(length>0):
        ReverseOrder(list,length-1)
        print(myList[length-1])
ReverseOrder(myList,len(myList))