#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n, e, i;
    cin >> n >> e;
    vector<pair<int, int>> v;

    while(e--){
        int a, b;
        cin >> a >> b;

        v.push_back({a, b});
    }

    for(i=0; i<v.size(); i++){
        cout << v[i].first << " " << v[i].second << endl;
    }
    
    return 0;
}