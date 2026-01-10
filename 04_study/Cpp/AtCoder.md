# AtCoder 挑戦メモ

## アルゴリズムと数学(https://atcoder.jp/contests/math-and-algorithm)
後で振り返りたい問題
- 007 Aの倍数 and Bの倍数
- 009 総当たり(動的計画法)
- 011 素数
- 013 約数
- 014 素因数分解
- 015 GCD(最大公約数)
- 017 LCM(最小公倍数)
- 020 DP(動的計画法)
- 026 コレクター問題
- 027 マージソート
- 028 Frog1
- 029 dp問題
- 030 ナップザック
- 031 dp問題
- 042 約数の和(←よくわからん)
- 043 DFS(深さ優先探索)
- 046 BFS(幅優先探索)
- 047 二部グラフ判定
- 048 ダイクストラ法
- 049 フィボナッチ数列(というよりはMODの性質)
- 050 繰り返し二乗法

### 振り返り問題
#### 007 Aの倍数 and Bの倍数
```cpp=
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long N, X, Y;
    cin >> N >> X >> Y;
    long long g = std::gcd(X, Y);
    long long l = X / g * Y;
    cout << (N / X) + (N / Y) - (N / l) << "\n";
}
```
包除原理$(N/X) + (N/Y) - (N/lcm(X, Y))$ を利用する問題
またLCM(最小公倍数)を求める際に$X * Y / gcd(X, Y)$で行うとオーバーフローの可能性が高まるので$X / gcd(X, Y) * Y$のように割り算を先に行っている
#### 009 総当たり(動的計画法)
```cpp=
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, S;
    cin >> N >> S;

    vector<int> A(N);
    for (int i = 0; i < N; ++i)
        cin >> A[i];

    vector<bool> dp(S + 1);
    dp[0] = true;

    for (int i = 0; i < N; ++i)
    {
        for (int j = S; j >= A[i]; --j)
        {
            if (dp[j - A[i]])
                dp[j] = true;
        }
    }

    if (dp[S])
        cout << "Yes" << "\n";
    else
        cout << "No" << "\n";
}
```
総当たり問題を動的計画法で解く問題
- 配列Aの中から要素をいくつか選んで、その合計がSになるかを確認する問題

大きさが$S+1$の配列dpを作成し、各インデックスのbool値でその合計値になるかどうか判断する
2段目のループでdp配列を最後から走査し、$dp[j-[A[i]]]$が$true$であるところを見つけ出す
組み合わせであることが重要
#### 011 素数
```cpp=
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<int> prime;
    if (N >= 2)
    {
        cout << 2;
        if (N >= 3)
            cout << " " << 3;
    }

    for (int i = 5; i <= N; i += 2)
    {
        bool prime_judge = true;
        // 2〜√i の範囲に割り切れる数が存在しない
        // j*j<=i ⇔ j <= sqrt(i)
        for (int j = 3; j * j <= i; j += 2)
        {
            if (i % j == 0)
            {
                prime_judge = false;
                break;
            }
        }
        if (prime_judge)
            prime.push_back(i);
    }

    for (int p : prime)
        cout << " " << p;
    cout << "\n";
}
```
奇数であるかを判定する問題
素数は奇数なので1段目のループのループ変数は2ずつ増やす
約数の性質から探索する範囲は$2～sqrt(i)$で良い 
また$j*j<=i ⇔ j <= sqrt(i)$である

#### 013 約数
```cpp=
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long N;
    cin >> N;

    for (long i = 1; i * i <= N; ++i)
    {
        if (N % i == 0)
        {
            cout << i << "\n";
            if (i != N / i)
                cout << N / i << "\n";
        }
    }
}
```
ある数の約数を列挙する問題
約数の性質から探索する範囲は$2～sqrt(i)$で良い 
また$j*j<=i ⇔ j <= sqrt(i)$である
またループの数の中である数の約数のペアも約数であるため、同時に出力している

#### 014 素因数分解
```cpp=
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long N;
    cin >> N;

    vector<long> factors;

    for (long i = 2; i * i <= N; ++i)
    {
        if (N % i == 0)
        {
            while (N % i == 0)
            {
                N /= i;
                factors.push_back(i);
            }
        }
    }
    if (N > 1)
        factors.push_back(N);

    for (int i = 0; i < factors.size() - 1; ++i)
        cout << factors[i] << " ";
    cout << factors.back() << "\n";
}
```
ある数を素因数分解する問題
探索すべき範囲は$2～sqrt(i)$でよい
割り切れる因数を発見した時18行目のループで、それで割り切れる間は割り続ける
最後に残った$N$も因数であるため出力する
#### 015 GCD(最大公約数)
```cpp=
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int A, B, C, D;
    cin >> A >> B;

    if (A <= B)
    {
        C = A;
        D = B;
    }
    else
    {
        C = B;
        D = A;
    }

    cout << gcd(D, C) << "\n";
}

long long gcd(long long a, long long b)
{
    if (b == 0)
        return a;
    return gcd(b, a % b);
}
```
最大公約数$GCD$を求める問題
ユークリッドの互除法を再帰関数で実装
#### 017 LCM(最小公倍数)
```cpp=
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<long long> A(N);
    for (int i = 0; i < N; ++i)
        cin >> A[i];

    long long answer = A[0];
    for (int i = 1; i < N; ++i)
        answer = lcm(answer, A[i]);
    cout << answer << "\n";
}

long long lcm(long long a, long long b)
{
    long long C = 0, D = 0;
    if (a <= b)
        C = a, D = b;
    else
        C = b, D = a;
    return D * C / gcd(D, C);
}

long long gcd(long long a, long long b)
{
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

```
最小公倍数LCMを求める問題
$LCM = A * B / GCD(A, B)$
#### 020 DP(動的計画法)
```cpp=
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<int> A(N);
    for (int i=0; i<N; ++i)
        cin >> A[i];

    int K = 5, S = 1000;
    vector<vector<int>> dp(K+1, vector<int>(S+1, 0));
    dp[0][0] = 1;

    for(int p : A)
    {
        for(int t=K; t>=1; --t)
        {
            for(int s=0; s+p<=S; ++s)
            {
                if(dp[t-1][s] != 0)
                    dp[t][s+p] += dp[t-1][s];
            }
        }
    }
    cout << dp[K][S] << "\n";
}
```
動的計画法dpを使って解く問題
- カードを5枚選ぶ方法のうち、選んだカードに書かれた整数の和がちょうど1000となるものが何通りあるかを探す問題

DP配列の各要素は、カードをK枚選んだ時に値の合計がSになるカードの組み合わせの数を表す
カードをK枚目からループするのは、同じカードを取らないようにするため
#### 026 コレクター問題
```cpp=
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    size_t N;
    cin >> N;

    double ans = 0.0;
    for (size_t i = 1; i <= N; ++i)
        ans += 1.0 * (1.0 / static_cast<double>(i));
    cout << fixed << setprecision(12) << ans * static_cast<double>(N) << "\n";
}
```
コレクター問題
既にk種類集まっている時、まだ持っていない種類が出る確率は$p=\frac{N-k}{N}$
新種が1枚出るまでの試行回数の期待値は
$E[X_k]=\frac{1}{p}=\frac{N}{N-k}$
全種類そろうまでの期待試行回数(期待支払い額)は段階ごとの和であるので
$E[T]=\sum_{k=0}^{N-1}\frac{N}{N-k}=N\sum_{i=1}^{N}\frac{1}{i}$
#### 027 マージソート
```cpp=
#include <bits/stdc++.h>
using namespace std;

// プロトタイプ宣言
// vector配列を直接操作するため，参照渡しする必要あり
void MergeSort(vector<long> &a, int left, int right);
void Merge(vector<long> &a, int left, int mid, int right);

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long N;
    cin >> N;

    vector<long> A(N);
    for (long i = 0; i < N; ++i)
        cin >> A[i];

    MergeSort(A, 0, static_cast<int>(A.size()) - 1);
    for (int i = 0; i < N; ++i)
    {
        if (i < N - 1)
            cout << A[i] << " ";
        else
            cout << A[i] << "\n";
    }
}

void MergeSort(vector<long> &a, int left, int right)
{
    // 再帰の終了条件，左と右が同じ(=要素が1個以下)
    if (left >= right)
        return;
    int mid = left + (right - left) / 2;
    MergeSort(a, left, mid);
    MergeSort(a, mid + 1, right);
    Merge(a, left, mid, right);
}

void Merge(vector<long> &a, int left, int mid, int right)
{
    int n1 = mid - left + 1;
    int n2 = right - mid;

    // 一時的な配列L,R
    vector<long> L(n1), R(n2);
    for (int i = 0; i < n1; ++i)
        L[i] = a[left + i];
    for (int j = 0; j < n2; ++j)
        R[j] = a[mid + 1 + j];

    int i = 0, j = 0, k = left;
    // LとRの両方に要素が残っている場合，小さいほうをaに書き戻す
    while (i < n1 && j < n2)
        // 三項演算子 ?:
        a[k++] = (L[i] <= R[j]) ? L[i++] : R[j++];
    // 残りをaにコピー
    while (i < n1)
        a[k++] = L[i++];
    while (j < n2)
        a[k++] = R[j++];
}
```
マージソートを実装する問題
対称を参照渡しすることで直接操作している
#### 028 Frog1
```cpp=
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<int> H(N);
    for (int i = 0; i < N; ++i)
        cin >> H[i];

    vector<int> dp(N, INT32_MAX);
    dp[0] = 0;

    for (int i = 0; i < N; ++i)
    {
        if (i + 1 < N)
            dp[i + 1] = min(dp[i + 1], dp[i] + abs(H[i] - H[i + 1]));
        if (i + 2 < N)
            dp[i + 2] = min(dp[i + 2], dp[i] + abs(H[i] - H[i + 2]));
    }

    cout << dp[N - 1] << "\n";
}
```
動的計画法dpを用いて解く問題
DP配列に足場$i$にたどり着くまでの最小コストを格納
そのためDP配列の初期値は```INT32_MAX```で初期化
#### 029 DP問題
```cpp=
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<int> dp(N+1, 0);
    dp[0] = 1;

    for (int i=0; i<N+1; ++i)
    {
        if(i+1<N+1)
            dp[i+1] += dp[i];
        if(i+2<N+1)
            dp[i+2] += dp[i];
    }
    cout << dp[N] << "\n";
}
```
動的計画法dpを用いて解く問題
DP配列に足場$i$に到達する方法の数を格納
#### 030 ナップザック
```cpp=
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, W;
    cin >> N >> W;

    vector<long long> w(N), v(N);
    for (int i=0; i<N; ++i)
        cin >> w[i] >> v[i];

    // 品物の数(N) * 重量制限(W) のdp配列
    vector<vector<long long>> dp(N + 1, vector<long long>(W + 1, 0));

    for (int i = 0; i < N; ++i)
    {
        // 全てのアイテムに対して取る場合と取らない場合どちらのケースもdp配列に保存する
        for (int j = 0; j <= W; ++j)
        {
            // アイテムiを取らない場合(重さが足されない)(maxは他の方法でdp配列が埋められている可能性を考慮している)
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j]);

            // アイテムiを取る場合(重さが足されている)
            if (j + w[i] <= W)
            {
                dp[i + 1][j + w[i]] = max(dp[i + 1][j + w[i]], dp[i][j] + v[i]);
            }
        }
    }

    long long ans = 0;
    for (int j = 0; j <= W; ++j)
    {
        // 最後までアイテムを見終わった後，全ての重さを見て最大価値を取り出す
        ans = max(ans, dp[N][j]);
    }

    cout << ans << "\n";
}
```
ナップザック問題
難しンゴ
#### 031 DP問題
```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<int> A(N);
    for (int i=0; i<N; ++i)
        cin >> A[i];

    long prev2 = 0, prev1=0;
    for (int i=0; i<N; ++i)
    {
        long cur =  (max(prev1, prev2+A[i]));
        prev2 = prev1;
        prev1 = cur;
    }

    cout << prev1 << endl;
}
```
動的計画法dpを使って解く問題

#### 042 約数の和
```cpp=
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long N, ans = 0;
    cin >> N;

    for (long i = 1; i <= N; ++i)
    {
        long a = N / i;
        ans += i * a * (a + 1) / 2;
    }
    cout << ans << endl;
}
```
約数の和を$O(\sqrt{N})$で計算する問題
ある整数Nに対して
$\sum_{i=1}^{N} i \times \left( 1 + 2 + \cdots + \left\lfloor \frac{N}{i} \right\rfloor \right)$
を計算している
$a=N/i$は「$N$以下にある$i$の倍数の個数」を表し、その$1$から$a$までの和を15行目のコードで求めている
#### 043 深さ優先探索
```cpp=
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> adj;
vector<bool> visited;

void dfs(int v)
{
    // 訪れたことのあるノードをtrueに
    visited[v] = true;
    // あるノードに繋がっているノードの集合でループを回す
    for (int u : adj[v])
    {
        // 訪れたことが無いノードならば
        if (!visited[u])
        {
            // そのノードの中で探索を開始
            dfs(u);
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    adj.resize(N + 1);
    visited.resize(N + 1, false);

    // 要素数が1個以下なら接続済
    if (N <= 1)
    {
        cout << "The graph is connected." << endl;
        return 0;
    }

    for (int i = 0; i <= M; ++i)
    {
        int a, b;
        cin >> a >> b;
        // ノードごとに繋がっているノードを記憶
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    // DFS実行
    dfs(1);
    // ノード数が合っているか確認
    int cnt = 0;
    for (int i = 1; i <= N; ++i)
    {
        if (visited[i])
        {
            cnt++;
        }
    }
    if (cnt == N)
        cout << "The graph is connected." << endl;
    else
        cout << "The graph is not connected." << endl;
    return 0;
}
```
深さ優先探索を実装して、連結グラフであるかを判断する問題
#### 046 幅優先探索
```cpp=
#include <bits/stdc++.h>
using namespace std;

// マスの4方向を指定するための配列
const int dx[4] = {1, 0, -1, 0};
const int dy[4] = {0, 1, 0, -1};

int main()
{
    int R, C;
    cin >> R >> C;

    int sy, sx;
    cin >> sy >> sx;
    sy--;
    sx--;

    int gy, gx;
    cin >> gy >> gx;
    gy--;
    gx--;

    // cinは空白で区切る
    vector<string> maze(R);
    for (int i = 0; i < R; i++)
    {
        cin >> maze[i];
    }
    // 距離を測るための2次元配列(mazeと同じ大きさ)
    vector<vector<int>> dist(R, vector<int>(C, -1));
    // 2値ならばvectorよりもpairのほうがおススメ
    queue<pair<int, int>> q;
    // スタートまでの距離はゼロ
    dist[sy][sx] = 0;
    q.push({sy, sx});

    while (!q.empty())
    {
        // autoはコンパイラに型推論をさせる(右辺をみて型を自動で決める)
        auto [y, x] = q.front();
        q.pop();
        for (int d = 0; d < 4; d++)
        {
            // 参照するマス目
            int ny = y + dy[d];
            int nx = x + dx[d];
            // マス目がmazeの範囲内かつ，壁でなく，未探索ならば
            if (0 <= ny && ny < R && 0 <= nx && nx < C && maze[ny][nx] == '.' && dist[ny][nx] == -1)
            {
                // 現在地までの距離に+1する
                dist[ny][nx] = dist[y][x] + 1;
                // 探索拠点候補のキューへ入れる
                q.push({ny, nx});
            }
        }
    }

    cout << dist[gy][gx] << endl;
    return 0;
}
```
幅優先探索を実装して、連結グラフであるかを判断する問題
迷路のマス目を近いところから順に探索していく
#### 047 二部グラフ
```cpp=
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> graph;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    graph.resize(N + 1);

    for (int i = 0; i <= M; ++i)
    {
        int a, b;
        cin >> a >> b;
        // ノードごとに繋がっているノードを記憶
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    // 色付けでグラフの二部を表現
    // -1が未訪問
    // 0,1の二値で判別
    vector<int> color(N + 1, -1);
    // グラフが連結でない可能性を考慮している
    for (int start = 1; start <= N; start++)
    {
        if (color[start] != -1)
            continue;

        queue<int> q;
        q.push(start);
        color[start] = 0;

        while (!q.empty())
        {
            int v = q.front();
            q.pop();
            // vに隣接するノードを全て見る
            for (int u : graph[v])
            {
                // まだ色がついていなければ
                if (color[u] == -1)
                {
                    // vの色と反対の色を塗る
                    color[u] = 1 - color[v];
                    q.push(u);
                }
                // 既に色が付いていてそれがvと同じなら二部グラフではないので"No"を出力
                else if (color[u] == color[v])
                {
                    cout << "No" << endl;
                    return 0;
                }
            }
        }
    }
    cout << "Yes" << endl;
    return 0;
}
```
幅優先探索で二部グラフであるかを判定する問題
#### 048 ダイクストラ法
```cpp=

```
ダイクストラ法を実装する問題
(よく分らんので後で復習)

#### 049 フィボナッチ数列
```cpp=
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
// よく使われる
const ll MOD = 1e9 + 7;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll N;
    cin >> N;

    vector<ll> a(N + 2, 0);
    a[1] = 1;
    a[2] = 1;
    // フィボナッチ計算(再帰でやっても良いかも)
    for (int i = 3; i <= N; ++i)
    {
        a[i] += a[i - 1] + a[i - 2];
        // 数値が大きくなり過ぎないように途中でMODを取る(modは途中でとっても最終結果は変わらない)
        a[i] %= MOD;
    }

    cout << a[N] << endl;
    return 0;
}
```
余りの性質を利用して数値がオーバーフローしないようにする問題
$(A+B)modM=((AmodM)+(BmodM))modM$
#### 050 繰り返し二乗法
```cpp=
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll MOD = 1e9 + 7;

// 繰り返し2乗法
// a^b mod MOD を高速に計算
ll modpow(ll a, ll b, ll mod)
{
    ll res = 1;
    while (b > 0)
    {
        // b が奇数なら res に a を掛ける
        // 「b&1」はビット演算で最下位ビットが1かどうかを調べている
        if (b & 1)
            res = (res * a) % mod;
        // a を二乗
        a = (a * a) % mod;
        // b を右シフト（b /= 2 と同じ）
        b >>= 1;
    }
    return res;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll a, b;
    cin >> a >> b;
    cout << modpow(a, b, MOD) << '\n';
}
```
指数計算を繰り返し二乗法で高速に解く問題
繰り返し二乗法は「指数$b$を2進数で分解して、必要な時にだけ$a$のべき乗を掛ける」ことで計算量を$O(\log N)$に抑える


## C++の記法
### 参考
- [python2cpp](https://github.com/kaityo256/python2cpp?tab=readme-ov-file)

### AtCoderよく使う記法
テンプレート
```cpp
// 標準ライブラリを全て取得
#include <bits/stdc++.h>
// 記法省略
using namespace std;
using ll = long long;

int main()
{
    ios::sync_with_stdio(false);
    // cinとcoutの接続を切る(なんか早くなるらしい)
    cin.tie(nullptr);
}
```
入出力(I/O)の操作
```cpp
// cinは空白で一区切りにする
vector<string> A(N);
// → 入力に空白が無い限り一行取得する
cin >> A[1];
```
ベクトルの操作
```cpp
// サイズ変更(要素は範囲を超えるものに対して削除or補完)
dp.resize(N);
// サイズ変更(要素を全て削除or置換)
dp.assign(N);
```
2次元ベクトル
```cpp
// 宣言
vector<vector<int>> dp;
// 要素数を指定して宣言
vector<vector<int>> dp(N, vector<int>(M,0));
// 要素アクセス
dp[A][B];
```