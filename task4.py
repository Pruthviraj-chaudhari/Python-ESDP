def is_palindrome(x):

    num = x
    rev = 0
    
    while number > 0:
     
        last_digit = number % 10
        
        rev = rev * 10 + last_digit
        
        number = number // 10

    return num == rev



num = int(input("Enter a number: "))
    
    
if is_palindrome(num):
    print(f"{num} is a palindrome!")
else:
    print(f"{num} is not a palindrome.")

