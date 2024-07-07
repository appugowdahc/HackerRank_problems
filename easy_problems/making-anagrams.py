from collections import Counter
def makingAnagrams(s1, s2):
    s11 = Counter(s1)
    s22 = Counter(s2)
    count =0
    for key,val in s11.items():
        if key not in s22:
            count += s11[key]
        else:
            count+= abs(s11[key]-s22[key])
    for key,val in s22.items():

        if key not in s11:
            print(count)
            count += s22[key]
    return count

s1 = "abc"
s2 = "amnop"
print(makingAnagrams(s1,s2))