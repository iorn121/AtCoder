#include <bits/stdc++.h>
#define REP(i, n) for(int i = 0; i < (n); i++)
#define REP1(i, n) for(int i = 1; i <= (n); i++)
#define REPD(i,a,b) for (int i=(a);i<=(b);i++)
#define ALL(v) (v).begin(), (v).end()
using namespace std;
typedef long long ll;
typedef vector<string> vs;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef set<int> si;
typedef vector<si> vsi;
typedef vector<ll> vll;
typedef vector<vll> vvll;
typedef pair<int, int> pi;
typedef queue<int> qi;
typedef queue<pi> qpi;
typedef pair<ll, ll> pll;
typedef queue<pll> qpll;
typedef vector<pi> vpi;
typedef vector<pll> vpll;
const int mod = 1000000007;
const int INF = 1001001001;
// 小数点　<< fixed << setprecision(0) <<
// sort降順　sort(ALL(),greater<int>());
// 円周率　M_PI
// 文字判定　isupper islower
// 文字変換　
// 順列　do {} while(next_permutation(ALL(X)));
// 最大値　LLONG_MAX
// a内でx以上　auto iter = lower_bound(ALL(a), x);
// a内でxより大きい　auto iter = upper_bound(ALL(a), x);
int dx[8] = {1, 0, -1, 0, 1, 1, -1, -1};
int dy[8] = {0, 1, 0, -1, 1, -1, 1, -1};
struct edge {
    int from; //出発点
    int to;   //到達点
    int cost; //移動コスト
};
typedef struct edge se;
typedef vector<edge> ve;
unsigned Euclidean_gcd(unsigned a, unsigned b) {
  if(a < b) return Euclidean_gcd(b, a);
  unsigned r;
  while ((r=a%b)) {
    a = b;
    b = r;
  }
  return b;
}

vpll PrimeFactorization(ll n) {
  vpll res;
  for (ll i=2; i*i<=n; i++) {
    if(n%i!=0) continue;
    ll ex=0;
    while(n%i==0) {
      ex++;
      n/=i;
    }
    res.push_back(pll(i,ex));
  }
  if(n!=1) res.push_back(pll(n,1));
  return res;
}

int main() {
  int n,k;
  cin >> n >> k;
  vi even,odd;
  REP(i,n) {
    int x;
    cin >> x;
    if(abs(x)==x&&x!=0) {
      even.push_back(x);
    } else if(abs(x)!=x||x==0) {
      odd.push_back(-1*x);
    }
  }
  sort(ALL(even),greater<int>());
  sort(ALL(odd),greater<int>());
  int od_n=odd.size();
  int ev_n=even.size();
  ll ans=1,t,c_t;
  if(n==k&&od_n%2==1) {
    REP(i,od_n) {
      ans*=odd[od_n-1-i]*-1;
      ans%=mod;
    }
    REP(i,ev_n) {
      ans*=even[ev_n-1-i];
      ans%=mod;
    }
  } else if(ev_n==0&&k%2==1) {
    REP(i,k) {
      ans*=odd[od_n-1-i]*-1;
      ans%=mod;
    }
  }else {
  if(ev_n>=k) {
    t=0;
  } else {
    t=(k-ev_n+1)/2;
  }
  c_t=t;
  double temp=1;
  while(1) {
    if(k-2*t<=0) break;
    if(2*t>=od_n) break;
    temp*=(odd[2*t]*odd[2*t+1])/(even[k-2*t-1]*even[k-2*t-2]);
    t++;
    if(temp>1) {
      c_t=t;
    }
  }
  REP(i,k-2*c_t) {
    cout << even[i] << endl;
    ans*=even[i];
    ans%=mod;
  }
  REP(i,2*c_t) {
    cout << odd[i] << endl;
    ans*=odd[i];
    ans%=mod;
  }}
  if(ans<0) ans+=mod;
  cout << ans << endl;
  return 0;
}
