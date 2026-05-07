def PrintPathHelper(x,y,maze,sol,n):
    if (x==n-1 and y==n-1):
        sol[x][y]=1
        print(sol)
        return
    if (x<0 or y<0 or x>=n or y>=n or maze[x][y]==0 or sol[x][y]==1):
        return 
    sol[x][y]=1
    PrintPathHelper(x+1,y,maze,sol,n)
    PrintPathHelper(x-1,y,maze,sol,n)
    PrintPathHelper(x,y+1,maze,sol,n)
    PrintPathHelper(x,y-1,maze,sol,n)
    sol[x][y]=0


def PrintPath(maze):
    n=len(maze)
    sol = [[0 for i in range(n)] for j in range(n)]
    PrintPathHelper(0,0,maze,sol,n)


n=int(input())
maze=[]
for i in range(n):
    row =  list(map(int, input().split()))
    maze.append(row)
PrintPath(maze)