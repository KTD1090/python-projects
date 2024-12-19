numbers=[1,2,5,7,4,1,2,7]
uniques=[]
for number in numbers:
    if number not in uniques:
       uniques.append(number)
print(uniques)
