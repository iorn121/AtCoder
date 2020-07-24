#include <bits/stdc++.h>
#define REP(i, n) for(int i = 0; i < (n); i++)
#define ALL(v) (v).begin(), (v).end()
using namespace std;
typedef long long ll;
typedef pair<int, int> P;
using Graph = vector<vector<int>>;
const int INF = 1001001001;
// << fixed << setprecision(0) <<
// sort(ALL(),greater<int>());

int main() {
  int n,q;
  cin >> n;
  vi s(n);
  REP(i,n) cin >> s[i];
  cin >> q;
  vi t(q);
  REP(i,q) cin >> t[i];
  sort(ALL(s));
  sort(ALL(t));
  int ans=0;
  REP(i,q) {
    if(binary_search(ALL(s),t[i])) ans++;
  }
  cout << ans << endl;
  return 0;
}
