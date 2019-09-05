#include <bits/stdc++.h>

using namespace std;

// 00:48 -> 00:51

int to(char c){
    return c - 'A' + 1;
}
int main() {
    long long ans = 1;
    string S;
    cin >> S;
    for(int i = 0 ; i + 1 < S.size() ; i++){
        ans *= to(S[i]) + to(S[i+1]);
    }
    cout << ans << endl;
}
