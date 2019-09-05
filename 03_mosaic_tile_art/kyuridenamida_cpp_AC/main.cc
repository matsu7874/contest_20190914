#include <bits/stdc++.h>

using namespace std;

// 00:57 -> 00:58

int main() {
    long long ans = 1;
    long long n;
    cin >> n;
    for(int i = 1 ; i <= n ; i++){
        ans *= i;
        ans %= 1000000007;
    }
    cout << ans << endl;
}
