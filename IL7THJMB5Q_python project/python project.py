while True:
    try:
        income = int(input("The tax  for your amount is:"))
    except ValueError:
        print("Sorry, We didn't understand that please enter taxable income as a number")
        continue
    else:
        break
    #in this projrect we don't calculate tax in decimals
tax_dedcution=income-50000
#income-50000 because of 50000 is the  discount given by government
no_tax=250000
if income<=250000:
    print("No Tax")
    #tax is not applicable for amount below or equal to 2.5Lakh
if income>250000 and income<=500000:
   second_slab=(tax_dedcution-no_tax)*5/100
   #for the amount b/w 2.5Lakh and 5Lakh 5% tax is applicable
   print(int(second_slab))
if income>500000 and income<=750000:
    #for the amount b/w 5Lakh and 7lakh 10% tax is applicable and we should add 5% of 2.5Lakh 
    # because for the previous slab remaining amount should add to the next slab to calculate the total tax
    third_slab=((tax_dedcution-500000)*10/100)+(no_tax*(5/100))
    print(int(third_slab))
if income>750000 and income<=1000000:
      #for the amount b/w 7.5Lakh and 10lakh 15% tax is applicable and we should add 5% of 2.5Lakh and 10% of 2.5Lakh
     # because for the firstslab remaining amount should add to the next slab to calculate the total tax
    fourth_slab=((tax_dedcution-750000)*15/100)+(no_tax*(5/100))+((no_tax)*(10/100))
    print(int(fourth_slab))
if income>1000000 and income<=1250000:
    #for the amount b/w 10Lakh and 12.5lakh 20% tax is applicable and we should add 5% of 2.5Lakh and 10% of 2.5Lakh and 15% of 2.5lakh
    # because for the firstslab remaining amount should add to the next slab to calculate the total tax
    fifth_slab=((tax_dedcution-1000000)*20/100)+(no_tax*(5/100))+((no_tax)*(10/100))+(no_tax*(15/100))
    print(int(fifth_slab))
if income>1250000 and income<=1500000:
    #for the amount b/w 12.5Lakh and 15lakh 25% tax is applicable and we should add 5% of 2.5Lakh and 10% of 2.5Lakh and 15% of 2.5lakh and 20%of 2.5lakh
    # because for the firstslab remaining amount should add to the next slab to calculate the total tax
    sixth_slab=((tax_dedcution-1250000)*25/100)+(no_tax*(5/100))+(no_tax*(10/100))+(no_tax*(15/100))+(no_tax*(20/100))
    print(int(sixth_slab))
if income>1500000:
    #for the amount more 15lakh 25% tax is applicable and we should add 5% of 2.5Lakh and 10% of 2.5Lakh and 15% of 2.5lakh and 25% of 2.5lakh
    # because for the firstslab remaining amount should add to the next slab to calculate the total tax
    last_slab=((tax_dedcution-1500000)*30/100)+(no_tax*(5/100))+(no_tax*(10/100))+(no_tax*(15/100))+(no_tax*(20/100))+(no_tax*(25/100))
    print(int(last_slab))