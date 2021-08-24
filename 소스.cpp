#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<cmath>
#include<map>
using namespace std;

int N, ans;
string s;
map<char, int> m;
vector<int> v;

int main()
{
	cin >> N;

	for (int i = 0; i < N; i++)
	{
		cin >> s;

		for (int j = 0; j < s.length(); j++)
			m[s[j]] += (int)pow(10, s.length() - 1 - j);
	}

	for (int i = 0; i < 26; i++)
		if (m['A' + i] != 0)

	sort(v.begin(), v.end(), greater<>());

	for (int i = 0; i < v.size(); i++)
		ans += (9 - i) * v[i];

	cout << ans << '\n';

}