<!---
title: '記号に関して'
category: Mathematics
language: Japanese
--->

# 記号に関して

混乱を防ぐために，ノートに使われる幾つかの記号の定義をまとめておく．

## 集合，写像

特集な集合の記号は以下の通りである．

- $\emptyset$：空集合，つまり何の元も含んでいない集合．
- $\N$：自然数全体の集合．此処で，$0$も自然数であることにする．
  - $n\N$：$n\N = \{nx|x\in\N\}$
- $\Z$：整数全体の集合．
  - $n\Z$：$n\Z = \{nx|x\in\Z\}$
- $\mathbb{Q}$：有理数全体の集合．
- $\R$：実数全体の集合．
  - $\R^{+}$：正の実数全体の集合．
  - $\R^{-}$：負の実数全体の集合．
- $\Complex$：複素数全体の集合．

集合と元の関係を表す記号は以下の通りである．

- $a\in A$：$a$が集合$A$に属する．
- $A\subset B$：集合$A$は$B$の部分集合である．
- $\mathscr{P}(A)$または$2^A$：集合$A$の部分集合全体の集合．
- $\forall x \in X$：「集合$X$に属する総ての$x$は…」
- $\exists x \in X$：「集合$X$に属するとある$x$は…」

写像または関数に関する記号は以下の通りである．

- $f:A\to B$：$f$は$A$を定義域，$B$を値域とする写像である．
- $f:x\mapsto y$：写像$f$により，$x$は$y$に対応される．

## 論理記号

- $\lnot p$：条件$p$の否定．
- $p\land q$：条件$p$且つ条件$q$．
- $p\lor q$：条件$p$又は条件$q$.
- $p\longrightarrow q$：条件$p$ならば条件$q$．$\neg p\lor q$と相同．
- $p\implies q$：条件$p$が条件$q$の十分条件である．（条件$q$が条件$p$の必要条件である．）
- $p\iff q$：条件$p$と条件$q$は互いに必要十分条件である．（条件$p$と条件$q$は同値である．）

## 演算子，関数

- $a\mid b$：$a$は$b$の約数．（$b$は$a$の倍数．）
- $n!$：$n$の階乗．
- $\log x$：別途の表示がない限り，底を$e$とする．
- $\Re(z)$：複素数$z\in\Complex$の実数部.
- $\Im(z)$：複素数$z\in\Complex$の虚数部.

## 近似

- $a(x) \sim b(x)$：$\lim_{x\to\infty}\frac{a(x)}{b(x)}=1$
混乱がない限り，$x$を省く場合もある．
- $f(x)\in O(g(x))$：Landauの記号，
$\lim_{x\to\infty}\left|\frac{f(x)}{g(x)}\right|<\infty$
- $f(x)\in o(g(x))$：同様にLandauの記号,
$\lim_{x\to\infty}\frac{f(x)}{g(x)}=0$

## 其の他

- □：証明終了.

## 外部リンク

- [Supported Functions](https://katex.org/docs/supported.html):
上記の記号を$\KaTeX$から入力する時のレファレンス．
