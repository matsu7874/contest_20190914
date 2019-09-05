#include <bits/stdc++.h>

using namespace std;

// 01:16 -> 01:20
// TODO 問題文指摘

vector<long long> memo;

long long calc(long long n) {
    return n - *--upper_bound(memo.begin(), memo.end(), n);
}

int main() {
    int n;
    cin >> n;
    for (int i = 0; i <= n; i++)
        memo.push_back(1ll * i*(i+1)/2);
    string s;
    cin >> s;
    int Q;
    cin >> Q;
    for(int i = 0 ; i < Q ; i++){
        long long q;
        cin >> q;
        --q;
        cout << s[calc(q)] << endl;
    }
}
