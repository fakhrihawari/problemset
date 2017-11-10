def solution(A):
    """
    :param A: non-empty list of integers
    :return: an integer - the smallest positive integer that is missing
    """
    missing = 1
    # for elem in sorted(A):
    #     if elem == missing:
    #         # print missing
    #         missing += 1
    #
    #     if elem > missing:
    #         break
    i=0
    A=sorted(A);
    while i< len(A):
        if A[i]==missing:

            print A[i]
            i=i+1
            missing += 1
        elif A[i]<missing:
           i=i+1
        else:
            if A[i]> missing:
                break

    return missing
A=[1,2,2,3,4,6];
print solution(A);