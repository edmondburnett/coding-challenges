# Challenge #122 [easy] Sum Them Digits (digital root)
# http://redd.it/1berjh


def dr_congruence(number):
    """ Find the Digital Root using Congruence Formula sorcery """
    return 1+(number-1)%9

def dr_modulo(number):
    """ Find the Digital Root using maths w/modulo """
    if number < 10:
        return number
    total = 0
    while number != 0:
        lastdigit = number%10
        number = number/10
        total = total+lastdigit
        if number == 0 and total > 9:
            number = total
            total = 0
    return total

def dr_recur(number):
    """ Find the Digital Root using recursion and strings """
    return number if number<10 else dr_recur(sum(int(n) for n in str(number)))


print dr_congruence(1073741824)
print dr_modulo(1073741824)
print dr_recur(1073741824)
