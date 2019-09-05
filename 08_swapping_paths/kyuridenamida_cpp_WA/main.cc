#include <bits/stdc++.h>

static const int MOD = 1000000007;
using namespace std;

// 01:30 -> 02:18 WA


int N, M;
int A, B;
// TODO: 負mod

int dfs(int a, int T, int n, map<tuple<int, int>, int> &memo) {
    if (n == 0) return a == T;
    if (a <= 0 || a > M) return 0;
    if (abs(a - T) > N) return 0;
    auto key = make_tuple(a, n);
    if (memo.count(key)) return memo[key];
    long long ans = 0;
    for (int i = -1; i <= 1; i++) {
        ans += dfs(a + i, T, n - 1, memo);
    }
    return memo[key] = (int) (ans % MOD);
}

long long calc(int from, int to, int step) {
    map<tuple<int, int>, int> memo;
    return 1ll * dfs(to, from, step, memo) * dfs(to, from, step, memo) % MOD;
}

long long calc_bad(int from, int to, int step) {
    map<tuple<int, int>, int> memo1, memo2;
    long long ans = 0;
    for (int i = 1; i <= M; i++) {
        long long t = 1;
        t *= 1ll * dfs(i, from, step , memo1) * dfs(i, from, step , memo1);
        t %= MOD;
        t *= 1ll * dfs(i, to, step, memo2) * dfs(i, to, step, memo2);
        t %= MOD;
        ans += t;
        ans %= MOD;
    }
    return ans;
}


int main() {
    cin >> N >> M;
    cin >> A >> B;
    long long r = calc(A, B, N - 1);
    long long u = calc_bad(A, B, N / 2);
    cout << ((r - u) % MOD + MOD) % MOD << endl;
}