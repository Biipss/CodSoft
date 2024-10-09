num1 = (float(input("Enter a number\t")))
num2 = (float(input("Enter another number\t")))

print(
    "Enter 1 for 'addition' \nEnter 2 for 'subtraction' \nEnter 3 for 'multiplication' \nEnter 4 for 'division' \nEnter 5 for 'modulous' \nEnter 6 for 'floor division' \nEnter 7 for 'exponent' "
)

enter_num = int(input("Enter your choice\t"))

if enter_num == 1:
  print("Addition =", num1 + num2)
elif enter_num == 2:
  print("Subtraction =", num1 - num2)
elif enter_num == 3:
  print("Multiplication =", num1 * num2)
elif enter_num == 4:
  print("Division =", num1 / num2)
elif enter_num == 5:
  print("Modulus =", num1 % num2)
elif enter_num == 6:
  print("Floor Division =", num1 // num2)
elif enter_num == 7:
  print("Exponent =", num1**num2)
else:
  print("Invalid Input")