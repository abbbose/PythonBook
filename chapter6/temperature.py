cel=float(input("Enter a temperature in degrees C: "))

def convert_cel_to_far(cel):

    f = cel * 9/5 + 32
    return f
f=convert_cel_to_far(cel)

print(f"{round(cel)} degrees C = {convert_cel_to_far(cel):.2f} degrees F")



# cel=float(input("Enter a temperature in degrees F:"))

# def convert_far_to_cel(cel):
#     c1 = (fah - 32) * 5/9
#     return c1



# print(convert_far_to_cel(cel))



    

























