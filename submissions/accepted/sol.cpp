#include <iostream>
#include <set>
#include <map>
#include <string>

using namespace std;

int sol(map<string, pair<string, string>> &rec, map<string, int> &mem, string curr) {
    if (mem.find(curr) != mem.end()) {
        return mem[curr];
    } else {
        string a = rec[curr].first;
        string b = rec[curr].second;
        mem[curr] = sol(rec, mem, a) + sol(rec, mem, b);
    }
    return mem[curr];
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

    map<string, int> mem;
    for (const string& elm : groundelms) {
        mem[elm] = 1;
    }

    string elm;
    cin >> elm;
    cout << sol(revrecipies, mem, elm) - 1 << endl;

    return 0;
}
