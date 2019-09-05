#include <bits/stdc++.h>
#include<ext/pb_ds/assoc_container.hpp>
#include<ext/pb_ds/tree_policy.hpp>
#include<ext/pb_ds/tag_and_trait.hpp>

using namespace std;
using namespace __gnu_pbds;
typedef tree<pair<int, int>, null_type, less<pair<int,int>>, rb_tree_tag, tree_order_statistics_node_update> BST;



// 03:25 -> 03:50

int DEL = 1;
int QUERY = 0;

struct Event {
    int a, b, c;
    int type;

    int pos() {
        if (type == QUERY) return b;
        return c + 1;
    }
};

BST bst;
map<int, vector<pair<int, int>>> X;

int counter = 0;

void add_key(int x) {
    auto key = make_pair(x, counter++);
    bst.insert(key);
    X[x].push_back(key);
}

void delete_key(int x) {
    bst.erase(X[x].back());
    X[x].pop_back();
}

int count_more_than_or_equal_to(int x) {
    return bst.size() - bst.order_of_key({x, -1});
}

int main() {
    int N;
    cin >> N;
    vector<Event> es;
    for (int i = 0; i < N; i++) {
        int P, L, R;
        cin >> P >> L >> R;
        es.push_back({L, P, R, QUERY});
        es.push_back({L, P, R, DEL});
    }
    sort(es.begin(), es.end(), [&](Event a, Event b) {
        if( a.pos() != b.pos() ) return  a.pos() < b.pos();
        return a.type > b.type;
    });


    long long ans = 0;
    for (auto e : es) {
        if (e.type == QUERY) {
            ans += count_more_than_or_equal_to(e.a);
            add_key(e.b);
        } else {
            delete_key(e.b);
        }
    }
    cout << ans << endl;


}