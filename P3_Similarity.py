sequence_one=input("Enter the first sequence: ")
sequence_two=input("Enter the second sequence: ")
how_many=int(input("How many elements for similarity condition?"))
similarities=[]
for i in range(0,how_many):
    a=input("Enter an element: ")
    c=int(input("How many elements is it similar to? "))
    similarities.append([])
    similarities[i].append(a)

    for j in range(0,c):
        b=input("What is it similar to? ")
        similarities[i].append(b)

def compare(o,t,s):
    print(o)
    print(t)
    print(s)
    #checking if similar
    score=0
    for i in range(len(o)):
        for j in range(len(s)):
            if o[i] in s[j] and t[i] in s[j] and o[i] != t[i]:
                score+=1
    #calculating similarity
    similarity= (score*100)/len(o)
    return similarity

print(compare(list(sequence_one),list(sequence_two),similarities),"%") 


OUTPUT : -

Enter the first sequence: ABCVDGFHIJK
Enter the second sequence: ABGCVFGHJI
How many elements for similarity condition?2
Enter an element: A
How many elements is it similar to? 2
What is it similar to? J
What is it similar to? I
Enter an element: C
How many elements is it similar to? 3
What is it similar to? V
What is it similar to? F
What is it similar to? G
['A', 'B', 'C', 'V', 'D', 'G', 'F', 'H', 'I', 'J', 'K']
['A', 'B', 'G', 'C', 'V', 'F', 'G', 'H', 'J', 'I']
[['A', 'J', 'I'], ['C', 'V', 'F', 'G']]
54.54545454545455 %
