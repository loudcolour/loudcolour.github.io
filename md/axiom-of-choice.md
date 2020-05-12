<!---
title: '선택 공리'
category: Mathematics
language: Korean
--->

# 선택 공리

> **공리**(선택 공리). 공집합이 아닌 집합 $A$의 모든 원소는
> 공집합이 아닌 집합이라고 하자.
> 이 때, 모든 $x\in A$에 대하여 $f(x) \in x$인 사상 $f:A\to\bigcup A$가 존재한다.

> **명제**. 다음은 모두 동치이다.
> 
> 1. 선택 공리
> 2. $A$가 공집합이 아닌 집합일 때,
> 모든 $x\in\mathscr{P}(A)\setminus\{\emptyset\}$에 대하여
> $f(x)\in x$인 사상 $f:\mathscr{P}(A)\setminus\{\emptyset\}\to A$가
> 존재한다.
> 3. 공집합이 아닌 집합 $I$를 첨자역으로 하는 집합족 $\langle A_i | i\in I\rangle$에
> 대하여, $\forall i\in I, A_i \not=\emptyset$이라면, 곱집합
> $\prod_{i\in I}A_i$또한 공집합이 아니다.
> 즉, 모든 $i\in I$에 대해 $g(i)\in A_i$인 사상
> $g:I\to\bigcup_{i\in I}A_i$가 존재한다.

*증명*. ($1\implies2$) 선택 공리를 가정한다.
이 때, $X = \mathscr{P}(A)\setminus\left\{\emptyset\right\}$로 두면, $X$의 모든 원소는
공집합이 아니므로, 선택 공리에 의하여
$\forall x\in X$에 대해, $f(x)\in x$인 사상 $f:X\to A$가 존재한다.
($\because\,\bigcup\mathscr{P}(A) = A$)  
($2\implies3$) $X=\bigcup_{i\in I} A_i$ 라고 두면,
$X\not=\emptyset$이다.
따라서 $\forall x\in \mathscr{P}(X)\setminus\left\{\emptyset\right\}$에 대하여,
$f(x)\in x$인 사상 $f:\mathscr{P}(X)\setminus\left\{\emptyset\right\}\to X$가
존재한다.
$\forall i\in I$에 대해 $A_i\in \mathscr{P}(X)\setminus\left\{\emptyset\right\}$이므로,
$f(A_i)\in A_i$가 성립한다. 여기서 $g:I\to X$, $i\mapsto f(A_i)$와 같은 사상을 정의하면,
$g(i)\in A_i$이므로 각 $i\in I$에 대해 해당하는 $g(i)$를 선택하여
$g(i)$로 순서쌍 $o(g)$을 만들면 $o(g)\in\prod_{i\in I}A_i$, 따라서 $\prod_{i\in I}A_i\not=\emptyset$  
($3\implies1$)
$A$ 그 자체는 $A$를 첨자역으로하는 집합족 $\langle x | x\in A\rangle$와 같다.
따라서, 모든 $x\in A$에 대해 $g(x)\in x$를 만족하는 사상 $g:A\to\bigcup A$가 존재하고,
이는 선택 공리의 진술과 같다. □
