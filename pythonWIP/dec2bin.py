def dec2bin(n):
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

# Test the function
num = -1
while True:
  num = int(input("Enter a decimal number (enter 0 to exit): "))
  if num == 0:
    break
  print(dec2bin(num))