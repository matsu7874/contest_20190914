#include <bits/stdc++.h>

static const int MOD = 1000000007;
using namespace std;

typedef long long Hash;

vector<Hash> H;

int dp[1 << 10][5][5];
vector<pair<int, int>> g[5][5][9];
int banana[5][5];
int bid[5][5];
vector<int> C;

// TODO バナナを食べると消失する?
// 03:00 -> 03:16

int dfs(int bit, int r, int c) {
    if( bit == 0 ) return 0;
    if (dp[bit][r][c] != -1) return dp[bit][r][c];
    int di = C[C.size() - __builtin_popcount(bit) ];
    int ans = 0;
    for (auto p : g[r][c][di]) {
        if (bit >> bid[p.first][p.second] & 1) {
            if (!dfs(bit - (1 << bid[p.first][p.second]), p.first, p.second)) {
                ans = 1;
            }
        }
    }

    return dp[bit][r][c] = ans;

}

int main() {
    memset(dp, -1, sizeof(dp));
    int N;
    cin >> N;
    int sr, sc;
    int k = 0;
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            char c;
            cin >> c;
            if (c == 'G') {
                sr = i;
                sc = j;
            } else if (c == 'B') {
                banana[i][j] = true;
                bid[i][j] = k++;
            }
        }
    }
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            for (int k = 0; k < 5; k++) {
                for (int l = 0; l < 5; l++) {
                    if (banana[k][l]) {
                        g[i][j][abs(i - k) + abs(j - l)].push_back({k, l});
                    }
                }
            }
        }
    }
    for (int i = 0; i < N; i++) {
        int c;
        cin >> c;
        C.push_back(c);
    }
    if(dfs((1 << N) - 1, sr, sc) ){
        cout << "gori" << endl;
    }else {
        cout << "uho" << endl;
    }


}