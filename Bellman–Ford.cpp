#include <bits/stdc++.h>
#define REP(i, n) for(int i = 0; i < (n); i++)
#define ALL(v) (v).begin(), (v).end()
using namespace std;
typedef long long ll;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vi> vivi;
typedef vector<ll> vll;
typedef vector<vll> vllvll;
typedef pair<int, int> P;
typedef queue<P> QP;
using Graph = vector<vector<int>>;
const int INF = 1001001001;
const int mINF = -1001001001;
const int mod = 1000000007;
// 小数点　<< fixed << setprecision(0) <<
// sort降順　sort(ALL(),greater<int>());
// 文字判定　isupper islower
// 順列　do {} while(next_permutation(ALL(X)));
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
struct edge {
    int from; //出発点
    int to;   //到達点
    int cost; //移動コスト
};
typedef struct edge se;
typedef vector<edge> ve;

int main() {
  int v,side,s,g;
  vi d(v,INF);
  cin >> v >> side >> s >> g;
  d[s]=0;
  ve edges;
  REP(i,side) {
    se add;
    int x,y,z;
    cin >> x >> y >> z;
    add.from = x-1;
    add.to = y-1;
    add.cost = z;
    edges.push_back(add);
  }
  REP(i,v) {
    REP(j,edges.size()) {
      se e = edges[j];
      if(d[e.to] > d[e.from] + e.cost) {
        d[e.to] = d[e.from] + e.cost;
        if(i==v-1) break;
      }
    }
  }
  cout << d[g] << endl;
  return 0;
}
