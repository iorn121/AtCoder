#include <bits/stdc++.h>
// #include <atcoder/all>
#define REP(i, n) for(ll i = 0; i < (n); i++)
#define REP1(i, n) for(ll i = 1; i <= (n); i++)
#define REPD(i,a,b) for (ll i=(a);i<=(b);i++)
#define ALL(v) (v).begin(), (v).end()
using namespace std;
// using namespace atcoder;
typedef long long ll;
typedef double d;
typedef long double ld;
typedef vector<string> vs;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<d> vd;
typedef vector<ld> vld;
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
typedef map<int, int> mii;
const int MOD = 1000000007;
const int INF = 1001001001;
// 小数点 << fixed << setprecision(10) <<
// sort降順 sort(ALL(),greater<int>());
// 円周率 M_PI
// 文字判定 isupper islower
// 順列 do {} while(next_permutation(ALL(X)));
// 最大値 LLONG_MAX
// a内でx以上 auto iter = lower_bound(ALL(a), x);
// a内でxより大きい auto iter = upper_bound(ALL(a), x);
int dx[8] = {1, 0, -1, 0, 1, 1, -1, -1};
int dy[8] = {0, 1, 0, -1, 1, -1, 1, -1};
// struct edge {
//     int from; //出発点
//     int to;   //到達点
//     int cost; //移動コスト
// };
// typedef struct edge se;
// typedef vector<edge> ve;

// SegTree用
ll op(ll x, ll y) {return x^y;}
ll e() {return 0;}

// 重複した要素を取り除いて返す
vll deleteDuplication(vll &numberlist) {
  sort(ALL(numberlist));
  numberlist.erase(unique(ALL(numberlist)),numberlist.end());
  return numberlist;
}

// 2つの数の最大公約数を求める
ll Euclidean_gcd(ll a, ll b) {
  if(a < b) return Euclidean_gcd(b, a);
  ll r;
  while ((r=a%b)) {
    a = b;
    b = r;
  }
  return b;
}

// 各桁の数を合計
int digit_sum(int n) {
  int sum=n%10;
  while(n!=0) {
    n/=10;
    sum+=n%10;
  }
  return sum;
}

// 素因数分解してペアのリストを返す
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

// a^n mod を計算する
long long modpow(long long a, long long n, long long mod) {
    long long res = 1;
    while (n > 0) {
        if (n & 1) res = res * a % mod;
        a = a * a % mod;
        n >>= 1;
    }
    return res;
}

ll combination(ll n, ll r) {
  if ( r * 2 > n ) r = n - r;
  ll x = 1;
  for ( ll i = 1; i <= r; ++i ) {
    x *= (n-i+1);
    x  /= i;
  }
  return x;
}

// Union-Find
struct UnionFind {
  vector<int> d;
  UnionFind(int n=0): d(n,-1) {}
  int find(int x) {
    if (d[x] < 0) return x;
    return d[x] = find(d[x]);
  }
  bool unite(int x, int y) {
    x = find(x); y = find(y);
    if (x == y) return false;
    if (d[x] > d[y]) swap(x,y);
    d[x] += d[y];
    d[y] = x;
    return true;
  }
  bool same(int x, int y) { return find(x) == find(y);}
  int size(int x) { return -d[find(x)];}
};
// mod. m での a の逆元 a^{-1} を計算する
ll modinv(ll a, ll m) {
    ll b = m, u = 1, v = 0;
    while (b) {
        ll t = a / b;
        a -= t * b; swap(a, b);
        u -= t * v; swap(u, v);
    }
    u %= m;
    if (u < 0) u += m;
    return u;
}

int main() {
  int a,b;
  cin >> a >> b;
  int aa=digit_sum(a);
  int bb=digit_sum(b);
  int ans=max(aa,bb);
  cout << ans << endl;
  return 0;
}
