weight = int(input("Enter the weight"))
if weight > 100:
    print("overweight")
elif weight < 100 :
    print("average")
elif weight < 50:
    print("Thinner")
else:
    print("Invalid choice!")