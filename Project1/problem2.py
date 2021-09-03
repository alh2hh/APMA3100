#stacked for loop solution (Problem 2)
def passCombos(length):
    passwords = []
    #iteration over possibilities
    for i in range(1, length+1):
        pwd = "" + str(i)
        for k in range (i+1, length+1):
            pwdtemp1 = pwd + str(k)
            for j in range (k+1, length+1):
                pwdtemp2 = pwdtemp1 + str(j)
                passwords.append(pwdtemp2)

    return passwords

pwds = passCombos(8)
print ('There are ' + str(len(pwds)) + ' password combinations. \n' +
        'Passwords are represented by a string of 3 integers 1-8 indicating ' 
        + 'the places of the zeros in that password.')
print ('Passwords: ')
print (pwds)
        
