string1 = "EAT"
string2 = "TEA"

def analyse_ananogram(string1, string2):    #
    if len(string1) != len(string2):        # 1
        return False                        # a
    for i in string1:                       # n + 1
        matched = False                     # n 
        for a in string2:                   # n x (n+1)
            if i == a:                      # n x n
                matched = True              # b
                break                       # b
        if matched == False:                # n
            return False                    # c
    return True                             # 1

print(analyse_ananogram(string1, string2))

#1 + a + (n+1) + n + n x (n+1) + 1 + b + b + n + c + 1
#= 1 + a + n+1 + n + n^2 + n + 1 + b + b + n + c + 1
#= n^2 + 4 + 4n + a + 2b + c 
#= 2n^2 + 4n + a + 2b + c + 3

#Let's assume that a = 0, b = n, c = 0.

#T(n) = 2n^2 + 6n + 3