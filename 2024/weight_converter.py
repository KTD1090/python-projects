weight=int(input('weight:'))
unit=input('(L)lbs or (K)g:)')

if unit.upper()=="L":
    converted=weight*0.45
    print(f"you are {converted} kilos")
else:
    converted=weight/0.45
    print(f"you are {converted} lbs")