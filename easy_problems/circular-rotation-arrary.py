def circularArrayRotation(a, k, queries):
    # Write your code here
    res = []
    #find all values of queries
    for i in range(len(queries)):
        
        #find index in rotation method 
        idx = (queries[i]-k)%n
        res.append(a[idx])
    return res

n = 5
a = [1,2,3,4,5]
k =3
queries = [1,4]
circularArrayRotation(a, k, queries)