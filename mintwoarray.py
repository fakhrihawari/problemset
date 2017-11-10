


def mintwoarray(A,B):
    # mencari minimum dari dua array
    x=len(A);
    y=len(B);
    A=sorted(A);
    B=sorted(B);
    i=0;
    j=0;
    while i<x and j<y:

        if A[i]== B[j]:
            return A[i];
            break
        else:
            if A[i]> B[j]:
                j=j+1;
            else:
                i=i+1;


    return


B=[1,9,5,10,11,12];
A=[4,2,9,3,2];
print duamin(A,B);