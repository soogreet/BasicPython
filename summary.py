print("-------------------")
print("Summation Program")
print("Type 'exit' to end the program")
print("-------------------")

sumdata = 0
count = 1

while True:
    data = input(f"Enter number {count}: ")
    if data == "exit":
        break
    sumdata += float(data)
    count = count + 1
    print(f"Sumdata= {sumdata}")
