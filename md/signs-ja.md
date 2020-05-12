<!---
title: '記号に関して'
category: Mathematics
language: Japanese
--->

# 記号に関して

混乱を防ぐために，ノートに遣われる幾つかの記号の定義を纏めて置く．

## 集合，写像

### 特殊な集合

- $\emptyset$：空集合，つまり何の元も含んでいない集合．
- $\N$：自然数全体の集合．此処では$0$も自然数であることにする．
  - $n\N$：$n\N = \{nx|x\in\N\}$
- $\Z$：整数全体の集合．
  - $n\Z$：$n\Z = \{nx|x\in\Z\}$
- $\mathbb{Q}$：有理数全体の集合．
- $\R$：実数全体の集合．
  - $\R^{+}$：正の実数全体の集合．
  - $\R^{-}$：負の実数全体の集合．
- $\Complex$：複素数全体の集合．

### 集合と元に対する関係

- $a\in A$：$a$が集合$A$に属する．
- $A\subset B$：集合$A$は$B$の部分集合である．
- $\forall x \in X$：「集合$X$に属する総ての$x$は…」
- $\exists x \in X$：「集合$X$に属するとある$x$は…」

### 集合の演算

- $A\cup B$：集合$A$と集合$B$の和集合．
- $A\cap B$：集合$A$と集合$B$の共通部分集合．
- $A\setminus B$：集合$A$の集合$B$に対する差集合．
- $A^{C}$：集合$A$の補集合．
- $\mathscr{P}(A)$又は$2^A$：集合$A$の部分集合全体の集合．冪集合．
- $A/\sim$：同値関係$\sim$に依る集合$A$の同値類全体の集合．
- $A\times B$：集合$A$と集合$B$の直積．即ち$A\times B=\{(a,b)|a\in A, b\in B\}$．

### 写像又は関数

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
- $a\perp b$：$a$と$b$は互いに素である．
- $n!$：$n$の階乗．
- $\log x$：別途の表示がない限り，底を$e$とする．
- $\Re(z)$：複素数$z\in\Complex$の実数部.
- $\Im(z)$：複素数$z\in\Complex$の虚数部.

## 代数構造

- $1_G$：乗法が与えられた群$G$の乗法に対する単位元．
- $0_G$: 加法が与えられた群$G$の加法に対する単位元．
- $A^{\times}$：$A$の可逆元全体の集合．
- $\langle S\rangle$：ある群に準ずる代数構造$G$が与えられた時，$S\subset G$に依り生成された部分群.
- $\text{Ker}(\phi)$：準同型写像$\phi$の核．即ち，$\phi:G_1\to G_2$とすると，$\text{Ker}(\phi) = \left\{x\in G_1 | \phi(x) = 1_{G_2}\right\}$．
- $\text{Im}(\phi)$：準同型写像$\phi$の像．即ち，$\phi:G_1\to G_2$とすると，$\text{Im}(\phi) = \left\{\phi(x)|x\in G_1\right\}$．
- $\text{Aut}\,G$：群に準ずる代数構造$G$の自己同型群.
- $G/H$：群$G$と其の部分群$H$に対し，$x\sim y \iff x^{-1}y\in H$を同値関係とする$G$の左剰余類全体の集合．
- $H\backslash G$：群$G$と其の部分群$H$に対し，$x\sim y \iff yx^{-1}\in H$を同値関係とする $G$の右剰余類全体の集合．

### 特殊な群

- $\mathfrak{S}_n$：$n$次対称群．即ち，$n$次置換全体の集合．
- $\text{GL}_{n}(K)$：$K$に対する$n$次一般線形群．
- $\text{SL}_{n}(K)$：$K$に対する$n$次特殊線形群．
- $\text{O}(n)$：$n$次直交群．
- $\text{SO}(n)$：$n$次特殊直交群．

## 近似

- $a(x) \sim b(x)$：$\lim_{x\to\infty}\frac{a(x)}{b(x)}=1$．
混乱がない限り，$x$を省く場合もある．
- $f(x)\in O(g(x))$：Landauの記号，
$\lim_{x\to\infty}\left|\frac{f(x)}{g(x)}\right|<\infty$．
- $f(x)\in o(g(x))$：同様にLandauの記号，
$\lim_{x\to\infty}\frac{f(x)}{g(x)}=0$．

## 其の他

- □：証明終了．

## 外部リンク

- [Supported Functions](https://katex.org/docs/supported.html):
上記の記号を$\KaTeX$から入力する時の参考文献．
