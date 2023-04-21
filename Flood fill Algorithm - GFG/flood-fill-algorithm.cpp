//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
private:
    void dfs(int row,int col,vector<vector<int>> &image,vector<vector<int>> &ans,int newColor,int ini,int deltaRow[],int deltaCol[]){
        ans[row][col] = newColor;
        int n = image.size();
        int m = image[0].size();
        for(int i = 0;i<4;i++){
            int nRow = row + deltaRow[i];
            int nCol = col + deltaCol[i];
            if(nRow >= 0 && nRow < n && nCol >= 0 && nCol < m && image[nRow][nCol] == ini && ans[nRow][nCol] != newColor){
                dfs(nRow,nCol,image,ans,newColor,ini,deltaRow,deltaCol);
            }
        }
    }
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        
        // Code here 
        vector<vector<int>> ans = image;
        int iniColor = image[sr][sc];
        int deltaRow[] = {-1,0,1,0};
        int deltaCol[] = {0,1,0,-1};
        dfs(sr,sc,image,ans,newColor,iniColor,deltaRow,deltaCol);
        return ans;

    }
};

//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int n, m;
		cin >> n >> m;
		vector<vector<int>>image(n, vector<int>(m,0));
		for(int i = 0; i < n; i++){
			for(int j = 0; j < m; j++)
				cin >> image[i][j];
		}
		int sr, sc, newColor;
		cin >> sr >> sc >> newColor;
		Solution obj;
		vector<vector<int>> ans = obj.floodFill(image, sr, sc, newColor);
		for(auto i: ans){
			for(auto j: i)
				cout << j << " ";
			cout << "\n";
		}
	}
	return 0;
}
// } Driver Code Ends