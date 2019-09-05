#include <bits/stdc++.h>

using namespace std;

// 01:00 -> 01:03

int main() {
    string S;
    cin >> S;
    vector<int> r;
    for (int i = 0; i < S.size();) {
        int j = i;
        assert(S[i] == '|');
        j++;
        while (j + 1 < S.size() && S[j] == '#' && S[j + 1] == '|') {
            j += 2;
        }
        r.push_back((j - i + 1) / 2);
        i = j;
    }
    for(int i = 0 ; i < r.size() ; i++){
        cout << r[i] << (i + 1 == r.size() ? "\n" : " ");
    }
}
