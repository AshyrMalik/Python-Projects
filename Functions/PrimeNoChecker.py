def primeChecker(n):
    count=2
    while(count<n):
        if n%count==0:
            return False
        count+=1

    return True



check=int(input("Enter the number: "))
print("Is the number prime? " , primeChecker(check))