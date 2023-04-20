//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  private:
  void dfs(int row,int col,vector<vector<char>> grid,vector<vector<int>>&visited){
      queue<pair<int,int>> q;
      visited[row][col] = 1;
      q.push({row,col});
      int n = grid.size();
      int m = grid[0].size();
      while(!q.empty()){
          int r = q.front().first;
          int c = q.front().second;
          q.pop();
          
          for(int deltaRow = -1;deltaRow <= 1;deltaRow++){
              for(int deltaCol = -1;deltaCol<=1;deltaCol++){
                  int numRow = r + deltaRow;
                  int numCol = c + deltaCol;
                  if(numRow >= 0 && numRow < n && numCol >= 0 && numCol < m && grid[numRow][numCol]=='1' && !visited[numRow][numCol]){
                      visited[numRow][numCol] = 1;
                      q.push({numRow,numCol});
                  }
              }
          }
      }
  }
  public:
    // Function to find the number of islands.
    int numIslands(vector<vector<char>>& grid) {
        // Code here
        int n = grid.size();
        int m = grid[0].size();
        vector<vector<int>> vis(n,vector<int>(m,0));
        int count = 0;
        for(int i = 0;i < n; i ++){
            for(int j = 0;j < m; j ++ ){
                if(!vis[i][j] and grid[i][j] == '1'){
                    count++;
                    dfs(i,j,grid,vis);
                }
            }
        }
        return count;
    }
};

//{ Driver Code Starts.
int main() {
    int tc;
    cin >> tc;
    while (tc--) {
        int n, m;
        cin >> n >> m;
        vector<vector<char>> grid(n, vector<char>(m, '#'));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> grid[i][j];
            }
        }
        Solution obj;
        int ans = obj.numIslands(grid);
        cout << ans << '\n';
    }
    return 0;
}
// } Driver Code Ends