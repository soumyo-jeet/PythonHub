print("WELCOME TO TIP CALCULATOR!!")
bill=int(input("Entre Your Total Bill: $"))
tip=int(input("Tip You Wish To Pay\n\t10,12,15: "))
total_bill = bill + bill * tip / 100
guests=int(input("Total Number Of Guests?: "))

bill_perhead= total_bill / guests

print(f"Each Of You Have To Pay: {bill_perhead}")