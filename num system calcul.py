base = int(input("Enter base of your number (10,2,8,16): "))
num_str = input("Eter your number: ")
choice = input("Convert Decimal to (Binary / Octal / Hexadecimal / Decimal): ").lower()

#list ta3 les valeur autorise
valid = []
if base==2:
    valid = ['0','1']
elif base==8:
    valid = ['0','1','2','3','4','5','6','7']
elif base==10:
    valid = ['0','1','2','3','4','5','6','7','8','9']
elif base==16:
    valid = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

#cheking pour iput num 
for ch in num_str.upper():
    if ch not in valid:
        print("Erro! '"+ch+"' مش مسموح في القاعده "+str(base))
        exit()


#transfer any num to deciaml
def n_to_decimal(n_str, base):
    letters = ['A','B','C','D','E','F']
    values  = [10,11,12,13,14,15]
    total = 0
    for ch in n_str.upper():
        if ch.isdigit():
            digit = int(ch)
        else:
            for i in range(len(letters)):
                if ch == letters[i]:
                    digit = values[i]
                    break
        total = total * base + digit
    return total


#les conditions ta3 transfert
if base == 10:
    decimal_value = int(num_str) 
else:
    decimal_value = n_to_decimal(num_str, base)  
if decimal_value == 0:
    print("Result: 0")




else:
    if choice == "binary":
        bits = []
        num = decimal_value
        while num >0:
            bits.append(str(num %2))
            num //=2
        bits.reverse()
        print("Binnary:", "".join(bits))






    elif choice == "octal":
        bits = []
        num = decimal_value
        while num>0:
            bits.append(str(num%8))
            num//=8
        bits.reverse()
        print("Octal:", "".join(bits))





    elif choice == "hexadecimal":
        bits = []
        letters = ['A','B','C','D','E','F']
        num = decimal_value
        while num>0:
            rem = num %16
            if rem<10:
                bits.append(str(rem))
            else:
                bits.append(letters[rem-10])
            num//=16
        bits.reverse()
        print("Hexadceimal:", "".join(bits))




    elif choice == "decimal":
        print("Deciml:", decimal_value)


    else:
        print("Invalid chice!")
