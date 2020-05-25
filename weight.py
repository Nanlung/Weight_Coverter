weight = int(input("Weight: "))
category = input("(L)bs or (K)g: ")
final_category = category.upper()

if final_category == "L":
    conversion = weight * 0.45
    print(f"Your weight is: {round(conversion)} kg")
else:
    conversion = weight / 0.45
    print(f"Your weight is: {round(conversion,2)} lbs")


