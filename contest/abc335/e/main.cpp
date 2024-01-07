#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    vector<int> A(N);
    for(int i = 0; i < N; i++) cin >> A[i];
    set<int> A_set(A.begin(), A.end());
    vector<int> A_sorted(A_set.begin(), A_set.end());
    int cvt_N = A_sorted.size();
    map<int, int> A_cvt;
    for(int i = 0; i < cvt_N; i++) A_cvt[A_sorted[i]] = i;
    vector<set<int>> G(cvt_N);
    for(int i = 0; i < M; i++) {
        int U, V;
        cin >> U >> V;
        U--; V--;
        if(A[V] > A[U]) swap(U, V);
        else if(A[U] == A[V]) continue;
        G[A_cvt[A[V]]].insert(A_cvt[A[U]]);
    }
    int start = A_cvt[A[0]];
    int end = A_cvt[A[N-1]];
    vector<int> ans(cvt_N, 0);
    deque<int> q;
    q.push_back(start);
    ans[start] = 1;
    while(!q.empty()) {
        int now = q.front(); q.pop_front();
        for(int nxt : G[now]) {
            if(nxt > end) continue;
            ans[nxt] = max(ans[nxt], ans[now] + 1);
            q.push_back(nxt);
        }
    }
    cout << ans[end] << endl;
    return 0;
}