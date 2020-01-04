def colshift(matrix):
     dp = [[0 for i in range(len(matrix[0]))]for j in range(len(matrix))]
     for i in range(len(matrix[0])):
          dp[0][i] = matrix[0][i]
     for i in range(len(matrix)):
          for j in range(len(matrix[0])):
               if matrix[i][j]==1:
                    dp[i][j] = 1+dp[i-1][j]
     m=0
     for i in range(len(matrix)):
          dp[i].sort(reverse=True)
          for j in range(len(matrix[0])):
               curarea = (j+1)*dp[i][j]
               if dp[i][j] and m<curarea:
                    m = curarea
     return m
matrix = [[1,0,1,1,0,1],
          [1,1,0,1,0,1],
          [1,0,0,1,0,1],
          [0,1,1,1,0,0]]
print(colshift(matrix))
          
