#include<bits/stdc++.h>
using namespace std;

const int N = 1e3+5;
const int INF = 1e9+5;
int d[N][N];
int n, m;

void print_matrix(){
    for(int i=1; i<=n; i++){
        for(int j=1; j<=n; j++){
            if(d[i][j] == INF) cout << "X "; 
            else cout << d[i][j] << " ";
        }
        cout << endl;
    }
}

void dist_initialize(){
    for(int i=1; i<=n; i++){
        for(int j=1; j<=n; j++){
            if(i != j){
                d[i][j] = INF;
            }
        }
    }
}


int main()
{
    cin >> n >> m;

    dist_initialize();

    while(m--){
        int u, v, w;
        cin >> u >> v >> w;

        d[u][v] = w;
        //d[v][u] = w;         // Undirected hole ei line dite hoy //
    }

    print_matrix();

    for(int k=1; k<=n; k++){
        for(int i=1; i<=n; i++){
            for(int j=1; j<=n; j++){
                d[i][j] = min(d[i][j], d[i][k]+d[k][j]);
            }
        }
    }

    cout << "\nAfter applying Floyd Warshall Algorithm\n\n";

    print_matrix();
    
    return 0;
}