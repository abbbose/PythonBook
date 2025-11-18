# amount = float(input("How much mony you want to invest? "))
# rate = float(input("Enter rate of your stock: "))
# years = float(input("How long do you wont hold your  stock? "))
def invest(amount, rate, years):
    per = (amount/amount) * rate
    invst = 0
    for y in range(1 , years+1 ):
     invst += per + amount
     
     print(f"Year {y}: ${invst:.2f}")

  



invest(100, 5, 5)