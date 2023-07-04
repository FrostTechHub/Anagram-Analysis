import time

string1 = "EAT"
string2 = "TEA"

start_time = time.time()
def analyse_ananogram(string1, string2):
    if len(string1) != len(string2):
        return print("LENGTH DOESN'T MATCH")
    for i in string1:
        matched = False
        print("i = "+ i)
        for a in string2:
            print("a = " + a)
            if i == a:
                matched = True
                break
        if matched == False:
            return print("NOT AN ANAGRAM")
    return print("IT IS AN ANAGRAM")

                
    

analyse_ananogram(string1, string2)
print("------%s seconds-------"%(time.time() - start_time))