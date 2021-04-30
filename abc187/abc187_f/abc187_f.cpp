#include <bits/stdc++.h>
 
const double pi = 3.141592653589793238462643383279;
 
 
using namespace std;
//typedef
//------------------------------------------
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef pair<long long, long long> PLL;
typedef pair<int, PII> TIII;
typedef long long LL;
typedef unsigned long long ULL;
typedef vector<LL> VLL;
typedef vector<VLL> VVLL;
 
 
//container util
//------------------------------------------
#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define MP make_pair
#define SZ(a) int((a).size())
#define SQ(a) ((a)*(a))
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define SORT(c) sort((c).begin(),(c).end())
 
 
//repetition
//------------------------------------------
#define FOR(i,s,n) for(int i=s;i<(int)n;++i)
#define REP(i,n) FOR(i,0,n)
#define MOD 1000000007
 
 
#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, x) for(auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
 
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
const double EPS = 1E-10;
 
#define chmin(x,y) x=min(x,y)
#define chmax(x,y) x=max(x,y)


//ここから編集
bool match[55][55];
bool dp[1 << 20];

int dp2[1 << 20];
int main() {
  cin.tie(0);
  ios::sync_with_stdio(false);
  cout << fixed << setprecision(10);

  
  int N, M;
  cin >> N  >> M;
  REP(i,N) REP(j,N) match[i][j] = true;
  REP(i,M){
    int a, b; cin >> a >> b;
    a--; b--;
    match[a][b] = false;
  }

  int n1 = N/2;
  int n2 = N-n1;

  //cout << n1 << " " << n2 << endl;

  for(int i=0; i<n2; i++){
    dp2[(1 << i)] = 1;
  }

  for(int bit=0; bit < (1 << n2); bit++){
    for(int i=0; i<n2; i++){
      
      if(bit >> i & 1) continue;

      bool ok = true;
      for(int j=0; j<n2; j++){
        
        if(bit >> j & 1){
          //cout <<  n1 + j << " " << n1 + i << endl;
          if(match[min(n1+j, n1 + i)][max(n1+i,n1 + j)] == false){
            ok = false;
          }
        }
      }
      
      int c = 0;
      if(ok) c++;
      dp2[bit | (1 << i)] = max(dp2[bit | (1 << i)], dp2[bit] + c);
      //cout << bit <<  " " << dp2[bit] << endl;
    }
  }
  int ans = 0;
  for(int bit=0; bit < (1 << n1); bit++){

    vector<int> cand;
    for(int i=0; i<n1; i++){
      if(bit >> i & 1){
        cand.push_back(i);
      }
    }

    bool check = true;
    for(int i=0; i<cand.size(); i++){
      for(int j=i+1; j<cand.size(); j++){
        check &= match[cand[i]][cand[j]];
      }
    }

    if(!check) continue;

    ll bit2 = 0;
    for(int i=0; i<n2; i++){
      bool ok = true;
      for(int j=0; j<cand.size(); j++){
        if(match[cand[j]][n1 + i] == false) ok = false; 
      }

      if(ok) bit2 |= (1 << i);
    }

    ans = max(ans, __builtin_popcount(bit) + dp2[bit2]);
    // cout << bit << " " << bit2 << " " << dp2[bit2] << endl; 
    // cout << __builtin_popcount(bit) + dp2[bit2] << endl;

  }
  cout << ans << endl;
  return 0;
}