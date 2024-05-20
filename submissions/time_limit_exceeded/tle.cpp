#include <iostream>
#include <set>
#include <map>
#include <string>

using namespace std;

int sol(map<string, pair<string, string>> &rec, string curr) {
    if (rec.find(curr) == rec.end()) {
        return 1;
    } else {
        string a = rec[curr].first;
        string b = rec[curr].second;
        return sol(rec, a) + sol(rec, b);
    }
}

int main() {
    int amountgroundelms;
    cin >> amountgroundelms;
    set<string> groundelms;
    for (int i = 0; i < amountgroundelms; i++) {
        string elm;
        cin >> elm;
        groundelms.insert(elm);
    }

    int combinations;
    cin >> combinations;
    map<string, pair<string, string>> revrecipies;
    for (int i = 0; i < combinations; i++) {
        string a, b, c;
        cin >> a >> b >> c;
        revrecipies[c] = make_pair(min(a, b), max(a, b));
    }

    string elm;
    cin >> elm;
    cout << sol(revrecipies, elm) - 1 << endl;

    return 0;
}
