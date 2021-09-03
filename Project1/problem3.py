# (Problem 3 Solution)
# globals
size = 8

# Utility function to generate the possible 0 locations <- from problem 2
def zeroLocation(length):
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

# brute force permutation utility function
def permuteHelper(options, r):
    if r <= 0:
        return [[]]

    permutes = []
    for i in range(0, len(options)):
        temp = options[i]
        tempOptions = options[:i] + options[i+1:]
            
        for pwd in permuteHelper(tempOptions, r-1):
            permutes.append([temp] + pwd)
    return permutes

# Uses 3 integer rep of 0 locations to generate other strings
def passCombos(zeros):
    possibilties = []
    othernums = permuteHelper([1, 2, 3, 4, 5, 6, 7], 5)
    print (str(len(othernums)))
    for pwd in zeros:
        temppwd = '11111111'
        temppwd = temppwd[0:int(pwd[0])-1] + '0' + temppwd[int(pwd[0]):]
        temppwd = temppwd[0:int(pwd[1])-1] + '0' + temppwd[int(pwd[1]):] 
        temppwd = temppwd[0:int(pwd[2])-1] + '0' + temppwd[int(pwd[2]):]  
        for combo in othernums:
            combopwd = temppwd
            for i in range(0, size):
                if (combopwd[i] != '0' and len(combo) > 0):
                    combopwd = combopwd[0:i] + str(combo[0]) + combopwd[i+1:]
                    combo = combo[1:]
            possibilties.append(combopwd)
    return possibilties
  
pwds = passCombos(zeroLocation(size))
print ('There are ' + str(len(pwds)) + ' possible passwords. \n')
print ('The first 100 passwords are... \n')
print (pwds[:100])