#include <bits/stdc++.h>

static const int MOD = 1000000007;
using namespace std;

// 02:47 -> 02:55
// TODO MOD 2^64 ハッシュをおとす?
// TODO Aho
typedef long long Hash;

vector<Hash> H;

int main() {
    string S;
    cin >> S;
    for (int i = 0; i < S.size(); i++) {
        Hash h = 0;
        for (int j = i; j < S.size(); j++) {
            h = h * 8999 + S[j];
            H.push_back(h);
        }
    }
    sort(H.begin(), H.end());

    int Q;
    cin >> Q;
    for (int i = 0; i < Q; i++) {
        string q;
        cin >> q;
        Hash h = 0;
        for( auto c : q ){
            h = h * 8999 + c;
        }
        if( binary_search(H.begin(), H.end(), h)){
            cout << "YES" << endl;
        }else{
            cout << "NO" << endl;
        }
    }


}