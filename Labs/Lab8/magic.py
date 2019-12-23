def is_square(m):
     '''2d-list => bool
     Return True if m is a square matrix, otherwise return False
     (Matrix is square if it has the same number of rows and columns'''
     for i in range(len(m)):
          if len(m[i]) != len(m):
               return False
     return True


def magic(m):
     '''2D list->bool
     Returns True if m forms a magic square
     Precondition: m is a matrix with at least 2 rows and 2 columns '''

     # this tests the condition that is implied by the definition
     # i.e. that m has to be a square matrix
     if(not(is_square(m))): # if matrix is not square
          return False      # return False

     # YOUR CODE GOES HERE

     #CASE 1
     for i in m:
          for j in i:
               if j < 1 and j > n**2:
                    return False

     #CASE 2
     list_row = []
     list_col = []

     for i in range(len(m)):
          sum_row = 0
          for j in range(len(m[0])):
               sum_row += m[i][j]
          list_row.append(sum_row)
     for i in range(len(m[0])):
          sum_col = 0
          for j in range(len(m)):
               sum_col+= m[i][j]
          list_col.append(sum_col)
     sum_left =0
     for i in range(len(m)):
          for j in range(len(m[0])):
               if i == j:
                    sum_left+= m[i][j]
     sum_right =0
     for i in range(len(m)):
          sum_right+= m[i][len(m)-i-1]
     print(list_row)
     print(list_col)
     print(sum_left)
     print(sum_right)
     for i in list_row:
          for j in list_col:
               if i != j or i != sum_left or i!= sum_right:
                    return False
     return True
   
               

# main
# TESTING OF magic functions
276
951
483
# this should print True

m0=[[2,7, 6],[9,5,1],[4,3,8]]
print(magic(m0))
    
# this should print True
m1 = [[16,3,2,13], [5,10,11,8],[9,6,7,12], [4,15,14,1]]
print(magic(m1))
    
# this should print False. Why? Which condition imposed on magic squares is not true for m3
m2 = [[1,2,3,4], [5,6,7,8],[9,10,11,12], [13,14,15,16]]
print(magic(m2))
    
#this should print False. Why? Which condition imposed on magic squares is not true for m3
m3 =  [[1,1],[1,1]]
print(magic(m3))

# #this should print False. Why? Which condition imposed on magic squares is not 
m3 =  [[1,1],[1,1],[1,2]]
print(magic(m3))
