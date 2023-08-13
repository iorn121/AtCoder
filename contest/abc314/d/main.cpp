    // N = I()
    // S = list(ST())
    // Q = I()
    // all_big = False
    // all_small = False
    // check = 0
    // for _ in range(Q):
    //     t, x, c = input().split()
    //     t = int(t)
    //     x = int(x)
    //     if t == 1:
    //         S[x-1] = c
    //         check |= 1 << (x-1)
    //     elif t == 2:
    //         all_small = True
    //         all_big = False
    //         check = 0
    //     else:
    //         all_small = False
    //         all_big = True
    //         check = 0
    // ans = S[:]
    // # print(ans)
    // for i in range(N):
    //     if check & (1 << i):
    //         continue
    //     if all_small:
    //         if S[i].isupper():
    //             ans[i] = chr(ord(S[i])+32)
    //     elif all_big:
    //         if S[i].islower():
    //             ans[i] = chr(ord(S[i])-32)
    // print("".join(ans))

// 上記のPythonをC++に書き換える

#include <bits/stdc++.h>
using namespace std;


int main() {
    int N;
    cin >> N;
    char S[N];
    for (int i = 0; i < N; ++i) {
        cin >> S[i];
    }
    int Q;
    cin >> Q;
    bool all_big = false;
    bool all_small = false;
    unsigned long long int check = 0;
    for (int i = 0; i < Q; ++i) {
        int t, x;
        char c;
        cin >> t >> x >> c;
        if (t == 1) {
            S[x-1] = c;
            check |= 1 << (x-1);
        } else if (t == 2) {
            all_small = true;
            all_big = false;
            check = 0;
        } else {
            all_small = false;
            all_big = true;
            check = 0;
        }
    }
    string ans;
    for (int i = 0; i < N; ++i)
    {
        if (check & (1 << i)) {
            ans+= S[i];
            continue;
        }
        if (all_small) {
            if (isupper(S[i])) {
                ans+= tolower(S[i]);
            } else {
                ans+= S[i];
            }
        } else if (all_big) {
            if (islower(S[i])) {
                ans+= toupper(S[i]);
            } else {
                ans+= S[i];
            }
        } else {
            ans+= S[i];
        }
    }
    cout << ans << endl;
    return 0;
}