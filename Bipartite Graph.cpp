#include <iostream>
#include <queue>
#include <vector>
#include <cstring>
using namespace std;
bool dfs(vector<int> adj[], int color[], int n)
{
    for (int i = 0; i < n; i++)
    {
        if (color[i] == -1)
        {
            color[i] = 0;
        }
        for (auto it : adj[i])
        {
            if (color[it] == color[i])
                return false;
            color[it] = 1 - color[i];
        }
    }
    return true;
}

int main()
{
    while (true)
    {
        int n, m;
        cin >> n;
        if (n == 0)
            break;
        cin >> m;
        vector<int> adj[n];

        for (int i = 0; i < m; i++)
        {
            int u, v;
            cin >> u >> v;
            adj[u - 1].push_back(v - 1);
            adj[v - 1].push_back(u - 1);
        }
        int color[n];
        memset(color, -1, sizeof color);
        if (dfs(adj, color, n))
        {
            cout << "BICOLOURABLE." << endl;
        }
        else
        {
            cout << "NOT BICOLOURABLE." << endl;
        }
    }
}
