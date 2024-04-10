#include <bits/stdc++.h>
using namespace std;

int main() {
    string S1, S2, S3;
    cin >> S1 >> S2 >> S3;

    set<char> chars;
    for (char c : S1) chars.insert(c);
    for (char c : S2) chars.insert(c);
    for (char c : S3) chars.insert(c);

    if (chars.size() > 10) {
        cout << "UNSOLVABLE" << endl;
        return 0;
    }

    vector<int> candidates(10);
    iota(candidates.begin(), candidates.end(), 0);

    do {
        map<char, int> char_to_num;
        auto it = candidates.begin();
        for (char c : chars) char_to_num[c] = *it++;

        if (char_to_num[S1[0]] == 0 || char_to_num[S2[0]] == 0 || char_to_num[S3[0]] == 0)
            continue;

        long long num1 = 0, num2 = 0, num3 = 0;
        for (char c : S1) num1 = num1 * 10 + char_to_num[c];
        for (char c : S2) num2 = num2 * 10 + char_to_num[c];
        for (char c : S3) num3 = num3 * 10 + char_to_num[c];

        if (num1 == 0 || num2 == 0 || num3 == 0)
            continue;

        if (num1 + num2 == num3) {
            cout << num1 << endl;
            cout << num2 << endl;
            cout << num3 << endl;
            return 0;
        }
    } while (next_permutation(candidates.begin(), candidates.end()));

    cout << "UNSOLVABLE" << endl;
    return 0;
}