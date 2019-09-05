#include <bits/stdc++.h>

using namespace std;

// 01:23 -> 01:28

int s[501][501];
int v[500][500];

// TODO bitset

int main() {
    int R, C;
    cin >> R >> C;
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            cin >> v[i][j];
        }
    }
    int Q;
    cin >> Q;
    for (int i = 0; i < Q; i++) {
        for (int j = 0; j < 2; j++) {
            int a, b, c, d;
            cin >> a >> b >> c >> d;
            --a;
            --c;
            s[a][c]++;
            s[b][c]--;
            s[a][d]--;
            s[b][d]++;
        }
    }
    for (int i = 0; i < R; i++) {
        for (int j = 1; j < C; j++) {
            s[i][j] += s[i][j - 1];
        }
    }
    for (int i = 1; i < R; i++) {
        for (int j = 0; j < C; j++) {
            s[i][j] += s[i - 1][j];
        }
    }

    int ans = 0;
    for(int i = 0 ; i < R ; i++){
        for(int j = 0 ; j < C ; j++){
            ans += s[i][j] % 2 * v[i][j];
        }
    }
    cout << ans << endl;

}
