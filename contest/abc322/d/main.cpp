#include <iostream>
#include <string>
#include <vector>
using namespace std;

#define rep(i, n) for (int i = 0; i < (n); i++)

// s を出力してプログラムを終了
void Print(const string& s) {
  cout << s << "\n";
  exit(0);
}

// 右に 90 度回転
void Rotate(vector<string>& v) {
  vector<string> w = v;
  rep(i, 4) rep(j, 4) w[3 - j][i] = v[i][j];
  v = w;
}

// (i, j) がグリッド内部かを判定する
bool in(int i, int j) { return 0 <= i and i < 4 and 0 <= j and j < 4; }

// p を (di, dj) を左上の位置として配置できるか？
bool can_put(vector<vector<int>>& exist, const vector<string>& p, int di,
             int dj) {
  rep(i, 4) rep(j, 4) {
    if (p[i][j] == '#') {
      int ni = i + di;
      int nj = j + dj;
      if (!in(ni, nj)) return false;
      if (exist[ni][nj] == 1) return false;
      exist[ni][nj] = 1;
    }
  }
  return true;
}

// ポリオミノを再帰で置いていく関数
void dfs(int i, const vector<vector<int>>& exist,
         const vector<vector<string>>& ps) {
  if (i == 3) {
    int ok = 1;
    rep(u, 4) rep(v, 4) ok &= exist[u][v];
    if (ok) Print("Yes");
    return;
  }
  for (int di = -3; di <= 3; di++) {
    for (int dj = -3; dj <= 3; dj++) {
      auto ex2 = exist;
      bool flag = can_put(ex2, ps[i], di, dj);
      if (flag) dfs(i + 1, ex2, ps);
    }
  }
}

int main() {
  vector<vector<string>> ps(3);
  rep(i, 3) {
    ps[i].resize(4);
    for (auto& s : ps[i]) cin >> s;
  }
  rep(t, 4) {
    rep(u, 4) {
        dfs(0, std::vector<std::vector<int>>(4, std::vector<int>(4, 0)), ps);
      Rotate(ps[2]);
    }
    Rotate(ps[1]);
  }
  Print("No");
}
