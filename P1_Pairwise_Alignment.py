
Write a Python Code to perform pairwise alignment.Take 2 sequences from user and calculate the score .

Source Code : -

se1=input("Enter the first sequence::")
se2=input("Enter the second sequence::")
seq1=list(se1)
seq2=list(se2)
score=[]
def Pairwise_alignment(a,b):
    gap(a,b)
    print(a)
    print(b)
    value=0
    length=len(a)
    for i in range(0,length):
        if(a[i]==b[i]):
            score.append('1')
            value=value+1
        else:
            score.append('0')
    print(score)
    print(value)
    
def gap(a,b):
    if(len(a)==len(b)):
        print()
    else:
        k=int(input("Enter the position to insert::"))
        if(len(a)<len(b)):
            a.insert(k,'-')
        else:
            b.insert(k,'-')
    return(a,b)

Pairwise_alignment(seq1,seq2)


OUTPUT : -

Enter the first sequence::ABCVFC
Enter the second sequence::ABBCV
Enter the position to insert::2
['A', 'B', 'C', 'V', 'F', 'C']
['A', 'B', '-', 'B', 'C', 'V']
['1', '1', '0', '0', '0', '0']

2
