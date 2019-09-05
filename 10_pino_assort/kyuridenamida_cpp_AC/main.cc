#include <bits/stdc++.h>

static const int MOD = 1000000007;
using namespace std;

// 02:30 -> 02:45
// TODO 問題文の制約に死ぬほど重要なことが書かれているように見える
int main() {
    int N;
    long long K;
    cin >> N >> K;
    vector<int> A[3];

    for (int i = 0; i < N; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        --a, --b, --c;
        if (a) A[0].push_back(a);
        else if (b) A[1].push_back(b);
        else A[2].push_back(c);
    }
    for (int i = 0; i < 3; i++) {
        sort(A[i].begin(), A[i].end());
    }

    auto f = [&](long long x) {
        long long B[3] = {10 * x - K, 7 * x - K, 7 * x - K};
        if (B[0] < 0 || B[1] < 0 || B[2] < 0) return false;

        int ans = 0;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < A[i].size(); j++) {
                if (B[i] < A[i][j]) {
                    break;
                } else {
                    B[i] -= A[i][j];
                    ans++;
                }
            }
        }
        return ans >= K;
    };
    long long l = 1, r = 20 * K;

    while (l != r) {
        long long m = (l + r) / 2;
        if (f(m)) {
            r = m;
        } else {
            l = m + 1;
        }
    }
    cout << l << endl;
}