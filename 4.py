def check_first_last_same(number):
    return numbers[0]== numbers[-1]
    
x= [10, 20, 30, 40, 10]
y= [75, 65, 35, 75, 30]
result_x=check_first_last_same(x)
result_y=check_first_last_same(y)

print(f"for list x: {result_x}")
print(f"for list y: {result_y}")