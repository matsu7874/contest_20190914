#include <bits/stdc++.h>

using namespace std;

// 01:06 -> 01:13

vector<long long> A, B;

int main() {
    int N;
    cin >> N;
    A.push_back(0);
    B.push_back(0);
    for (int i = 0; i < N; i++) {
        long long a;
        cin >> a;
        A.push_back(A.back() + a);
    }
    for (int i = 0; i < N; i++) {
        long long b;
        cin >> b;
        B.push_back(B.back() + b);
    }

    int p = 0;
    int Q;
    cin >> Q;
    for (int i = 0; i < Q; i++) {
        long long q;
        cin >> q;
        while (p + 1 < A.size() && A[p + 1] <= q) {
            p++;
        }
        if( B[p] < q ){
            cout << "kame" << endl;
        }else if( B[p] > q ){
            cout << "usagi" << endl;
        }else{
            cout << "draw" << endl;
        }
    }
}
