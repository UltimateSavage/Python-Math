import time
# m = int(input("how many rows?"))
# n = int(input("how many columns?"))
# matrix=[]
# for i in range(n+1):
#     row=(input("what are the values in your rows")).split(" ")
#     if(len(row)!=n):
#         print("wrong input")
#     for j in range(len(row)):
#         row[j]=float(row[j])
#     if i==n-1:
#         matrix.append(row)
#         break
#     else:
#         matrix.append(row)
matrix=[
    # [2,4,1,-3],
    # [7,2,2,-2],
    # [3,3,2,2],
    # [0,5,1,0]
    # [1, 0,  0,  0,  0],
    # [0, 0,  1,  0,  0],
    # [1, -7, 0,  4,  2],
    # [0, 4,  2,  -7  ,1],
    # [0, 2,  0,  1,  -7]
    [3, 8, 8, 6, 3, 4, 2, 5, 2, 2], 
    [4, 5, 3, 7, 2, 4, 8, 7, 3, 9], 
    [1, 7, 3, 5, 9, 3, 3, 8, 7, 8], 
    [9, 6, 0, 8, 6, 3, 9, 5, 3, 2], 
    [0, 9, 7, 0, 4, 7, 5, 6, 5, 9], 
    [7, 6, 9, 5, 8, 8, 7, 9, 6, 4], 
    [9, 9, 5, 7, 8, 3, 8, 8, 1, 0], 
    [4, 7, 6, 7, 4, 9, 8, 6, 9, 9], 
    [7, 4, 5, 2, 4, 9, 7, 1, 9, 7], 
    [8, 7, 6, 7, 2, 3, 6, 2, 5, 2]
    # [0,-1,3,4],
    # [-2,-6,-10,-4],
    # [-3,-2,-4,-8],
    # [2,1,9,6]
    ]

def determinant(matrix):
    sum=0.0
    sign=0
    zcount=0
    zeros=[]
    boolean = False
    if (len(matrix)==1):
        return matrix[0][0]
    if (len(matrix)==2):
        return (matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0])
    if (len(matrix)==3):
        aei=matrix[0][0]*matrix[1][1]*matrix[2][2]
        dhc=matrix[1][0]*matrix[2][1]*matrix[0][2]
        gbf=matrix[2][0]*matrix[0][1]*matrix[1][2]
        gec=matrix[2][0]*matrix[1][1]*matrix[0][2]
        ahf=matrix[0][0]*matrix[2][1]*matrix[1][2]
        dbi=matrix[1][0]*matrix[0][1]*matrix[2][2]
        return(aei+dhc+gbf-gec-ahf-dbi)
    for rows in matrix:
        for cols in rows:
            if cols==0.0:
                zcount+=1
        zeros.append(zcount)
        zcount = 0
    swap = zeros.index(max(zeros))
    if swap!=0:
        matrix[0],matrix[swap]=matrix[swap],matrix[0]
        boolean=True
    for i in range(len(matrix)):
        n=len(matrix)-1
        if matrix[0][i]==0:
            sum+=0
        else:
            smaller=[[0 for k in range(n)] for j in range(n)]
            for row in range(1,len(matrix)):
                for col in range(len(matrix[0])):
                    if(col<i):
                        smaller[row-1][col]=matrix[row][col]
                    elif(col>i):
                        smaller[row-1][col-1]=matrix[row][col]
                    elif(col==i):
                        continue
            if(i%2==0):
                sign=1
            else:
                sign=-1
            sum+=sign*matrix[0][i]*determinant(smaller)
    if boolean:
        sum*=-1
    return sum
start=time.time()
print(determinant(matrix),"\n"+str(time.time()-start))
# print(letters)
# print(matrix)