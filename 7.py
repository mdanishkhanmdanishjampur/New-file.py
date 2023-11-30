def is_palindrome(number):
    # Convert the number to a string for easy reversal
    num_str = str(number)
    
    # Compare the original string with its reverse
    return num_str == num_str[::-1]

# Example usage:
number_to_check = 545
if is_palindrome(545):
    print(f"{545} is a palindrome.")
else:
    print(f"{545} is not a palindrome.")
   
   