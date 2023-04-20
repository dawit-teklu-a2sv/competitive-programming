//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function Template for C++

class Solution {
  private:
  void dfs(int node,vector<int> adj[],int visited[]){
      visited[node] = 1;
      for(auto it:adj[node]){
          if(!visited[it]){
              dfs(it,adj,visited);
          }
      }
  }
  public:
    int numProvinces(vector<vector<int>> adj, int V) {
        // code here
        vector<int> adjL[V];
        for(int i=0;i<V;i++){
            for(int j=0;j<V;j++){
                if(adj[i][j] && i != j){
                    adjL[i].push_back(j);
                    adjL[j].push_back(i);
                }
            }
        }
        int count = 0;
        int visited[V] = {0};
        for(int i=0;i<V;i++){
            if(!visited[i]){
                count++;
                dfs(i,adjL,visited);
            }
        }
        return count;
        
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int V,x;
        cin>>V;
        
        vector<vector<int>> adj;
        
        for(int i=0; i<V; i++)
        {
            vector<int> temp;
            for(int j=0; j<V; j++)
            {
                cin>>x;
                temp.push_back(x);
            }
            adj.push_back(temp);
        }
        

        Solution ob;
        cout << ob.numProvinces(adj,V) << endl;
    }
    return 0;
}
// } Driver Code Ends