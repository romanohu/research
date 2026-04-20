# overleaf
クラウドベースのLaTeX専用のエディタ． \
日本語を打ち込む場合は[この記事](https://qiita.com/fujino-fpu/items/d92d185da730e25743cb)を参考にする．\

## テンプレート
```
\documentclass[a4paper,11pt]{article}

% ===== パッケージ =====
\usepackage{graphicx}   % 図の挿入
\usepackage{amsmath,amssymb} % 数式
\usepackage{listings}   % コードブロック
\usepackage{xcolor}     % コードの色付け
\usepackage{fancyhdr}   % ヘッダー・フッター
\usepackage{geometry}   % 余白調整
\usepackage{comment}    % コメントアウト用
\usepackage{caption}    % キャプション調整

% ===== 余白設定 =====
\geometry{margin=25mm}

% ===== ヘッダー・フッター設定 =====
\pagestyle{fancy}
\fancyhf{} % 一旦クリア
\fancyhead[L]{レポート・論文タイトル}
\fancyhead[R]{著者名}
\fancyfoot[C]{\thepage}

% ===== コードブロック設定 =====
\lstset{
  basicstyle=\ttfamily\small,
  keywordstyle=\color{blue},
  commentstyle=\color{green!50!black},
  stringstyle=\color{red},
  frame=single,
  breaklines=true,
  showstringspaces=false,
  numbers=left,
  numberstyle=\tiny,
  tabsize=2
}

\title{レポート・論文タイトル}
\author{著者名}
\date{\today}

\begin{document}

\maketitle

\newpage
改ページ

\section{Introduction}
ここに導入を書く．

\section{文章の例}
これは通常の文章です．  
\LaTeX{} では，段落を空行で区切ることで新しい段落になります．

これは次の段落の例です．
強調したいときは \textbf{太字} や \textit{斜体} を使えます．

\subsection{箇条書きの例}
\begin{itemize}
  \item 項目1
  \item 項目2
  \item 項目3
\end{itemize}

\subsection{番号付き箇条書きの例}
\begin{enumerate}
  \item 手順1
  \item 手順2
  \item 手順3
\end{enumerate}

\section{コードブロックを載せる機能とテンプレ}
\begin{lstlisting}[language=Python, caption=Pythonコード例]
def hello():
    print("Hello, LaTeX!")

hello()
\end{lstlisting}

\section{数式を書く機能とテンプレ}

\subsection{本文中の数式}
例えば，$a^2 + b^2 = c^2$ のように本文中に数式を書けます．

\subsection{独立した数式}
\begin{equation}
E = mc^2
\end{equation}

\subsection{複数行の数式}
\begin{align}
f(x) &= x^2 + 2x + 1 \\
     &= (x+1)^2
\end{align}

\section{図を載せる機能とテンプレ}
図を挿入する例です．

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.6\linewidth]{example-image}
  \caption{図のキャプション例}
  \label{fig:example}
\end{figure}

図\ref{fig:example} のように参照できます．

\section{表を載せる機能とテンプレ}
表を挿入する例です．

\begin{table}[htbp]
  \centering
  \caption{表のキャプション例}
  \label{tab:example}
  \begin{tabular}{|c|c|c|}
    \hline
    列1 & 列2 & 列3 \\ \hline
    A   & B   & C   \\ \hline
    1   & 2   & 3   \\ \hline
  \end{tabular}
\end{table}

表\ref{tab:example} のように参照できます．


\section{Conclusion}
ここに結論を書く．

\end{document}
```

### 日本語のコンパイルを通すには
latexmkrcというファイルを作り、以下を書き込む．texの設定はLatex．

```
$latex = 'uplatex';
$bibtex = 'upbibtex';
$dvipdf = 'dvipdfmx %O -o %D %S';
$makeindex = 'mendex -U %O -o %D %S';
$pdf_mode = 3; 
```

### 2段組
2列組にしたい場合は，documentclass を以下のように変更する

```
\documentclass[a4paper,11pt,twocolumn]{article}
```

または、

```
\usepackage{multicol}

\begin{multicols}{2}
(文章)
\end{multicols}
```

### ヘッダーとフッターの設定変更
```
設定を書き換える例：
\begin{lstlisting}[language=TeX, caption=ヘッダー・フッター設定例]
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{左ヘッダー}
\fancyhead[C]{中央ヘッダー}
\fancyhead[R]{右ヘッダー}
\fancyfoot[L]{左フッター}
\fancyfoot[C]{\thepage}
\fancyfoot[R]{右フッター}
\end{lstlisting}
```
