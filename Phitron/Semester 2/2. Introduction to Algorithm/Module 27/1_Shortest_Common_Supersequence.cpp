#include<bits/stdc++.h>
using namespace std;
int main()
{
    string a;
    string b;
    cin >> a; 
    cin >> b;
    int n = a.size();
    int m = b.size();
    int i, j;

    int dp[n+1][m+1];

    for(i=0; i<=n; i++){
        for(j=0; j<=m; j++){
            if(i == 0 || j == 0){
                dp[i][j] = 0;
            }
        }
    }

    for(i=1; i<=n; i++){
        for(j=1; j<=m; j++){

            if(a[i-1] == b[j-1]){
                dp[i][j] = dp[i-1][j-1] + 1;
            }
            else{
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
    }

    // Shortest Common Supersequence = (size of first array + size of second array) - LCS // 

    cout << "Shortest Common Supersequence: " << (n+m) - dp[n][m] << endl;
    
    return 0;
}