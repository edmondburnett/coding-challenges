# Challenge #116 [easy] Permutation of a string
# http://redd.it/164zvs

def permute(s):
    if len(s) == 1:
        return set([s])

    perms = set()

    for seed in permute(s[:-1]):
        for position in range(len(s)):
            perms.add(seed[:position] + s[-1] + seed[position:])

    return perms

print permute('bank')
