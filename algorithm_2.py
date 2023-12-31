string1 = "FAIRY TALES"
string2 = "RAIL SAFETY"

def analyse_ananogram(string1, string2):
    if len(string1) != len(string2):
        return False
    character_counter = {"A": 0, "B": 0, "C": 0, "D": 0, 
                     "E": 0, "F": 0, "G": 0, "H": 0, 
                     "I": 0, "J": 0, "K": 0, "L": 0, 
                     "M": 0, "N": 0, "O": 0, "P": 0, 
                     "Q": 0, "R": 0, "S": 0, "T": 0, 
                     "U": 0, "V": 0, "W": 0, "X": 0, 
                     "Y": 0, "Z": 0, " ": 0}
    for i in string1:
        if (i == character_counter[i]):
            character_counter[i] = character_counter[i] + 1
    for a in string2:
        if (a == character_counter[i]):
            character_counter[a] = character_counter[a] - 1
    values = list(character_counter.values())
    for g in range(0, len(values)):
        if values[g] != 0:
            return False
            break
    return True

analyse_ananogram(string1, string2)