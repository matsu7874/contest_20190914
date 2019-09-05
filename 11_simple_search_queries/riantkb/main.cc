#include<bits/stdc++.h>
using namespace std;

class suffix_array {
    // compare (rank[i], rank[i + k]) and (rank[j], rank[j + k])
    static bool compare_sa(int n, const vector<int>& rank, int i, int j, int k) {
        if (rank[i] != rank[j]) return rank[i] < rank[j];
        int ri = i + k <= n ? rank[i + k] : -1;
        int rj = j + k <= n ? rank[j + k] : -1;
        return ri < rj;
    }
public:
    static vector<int> construct_sa(const string& s) {
        int n = s.length();
        vector<int> sa(n + 1), rank(n + 1);
        for (int i = 0; i <= n; ++i) {
            sa[i] = i;
            rank[i] = i < n ? s[i] : -1;
        }
        for (int k = 1; k <= n; k <<= 1) {
            sort(sa.begin(), sa.end(), [&n, &k, &rank](const int& a, const int& b){ return compare_sa(n, rank, a, b, k); });

            vector<int> tmp(n + 1);
            for (int i = 1; i <= n; ++i)
                tmp[sa[i]] = tmp[sa[i - 1]] + compare_sa(n, rank, sa[i - 1], sa[i], k);
            for (int i = 0; i <= n; ++i)
                rank[i] = tmp[i];
        }
        return sa;
    }
    static vector<int> construct_lcp(const string& s, const vector<int>& sa) {
        int n = s.length();
        vector<int> rank(n + 1), lcp(n + 1);
        for (int i = 0; i <= n; ++i) rank[sa[i]] = i;

        int h = 0;
        for (int i = 0; i < n; ++i) {
            if (h > 0) --h;
            for (int j = sa[rank[i] - 1]; j + h < n && i + h < n; ++h)
                if (s[j + h] != s[i + h]) break;

            lcp[rank[i] - 1] = h;
        }
        return lcp;
    }
};

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);
    string s;
    int q;
    cin >> s >> q;
    const char* sc = s.c_str();
    vector<int> sa = suffix_array::construct_sa(s);
    for (int i = 0; i < q; ++i) {
        string t;
        cin >> t;
        const char* tc = t.c_str();
        int l = -1, re = s.length();
        while (l + 1 < re) {
            int m = (l + re) / 2;
            if (strcmp(sc + sa[m], tc) < 0)
                l = m;
            else
                re = m;
        }
        bool ok = true;
        for (int j = 0; j < (int)t.length(); ++j) {
            if (s[sa[re] + j] != t[j]) {
                ok = false;
                break;
            }
        }
        cout << (ok ? "YES" : "NO") << '\n';
    }
    return 0;
}
