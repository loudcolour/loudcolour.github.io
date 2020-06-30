<!---
title: 벡터공간의 기저
language: Korean
category: Linear Algebra
--->

# 벡터공간의 기저

## 정의

> **정의**. 체 $K$ 상의 벡터공간 $V$가 주어졌을 때, 집합 $X\subset V$가 $V$의
> 기저(basis)라는 것은, 다음을 동시에 만족하는 것을 의미한다.
>
> 1. $X$가 선형독립
> 2. $\langle X \rangle = V$

만약 $X = \left\{ x_1, x_2, \ldots x_n \right\} $이 $V$의 기저라면,
$X' = \left\{ x_1+x_2, x_2, \ldots x_n \right\}$도 $V$의 기저이다.
($\because$ $c_i\in K$, $i = 1,2,\ldots, n$이라고 하여
$c_1(x_1 + x_2) + c_2x_2 + \ldots + c_nx_n=0$라고 하자.
$c_1x_1 + (c_1+c_2)x_2+ \ldots + c_nx_n$이므로, 이는 $X$의 선형독립성에 의하여
$c_1=c_1+c_2=\ldots=c_n=0$, $c_1=c_2=\ldots=c_n=0$, 따라서 $X'$는 선형독립이고,
같은 원리로 $X$상의 선형결합으로 나타내어진 $V$의 원소를 $X'$상의 선형결합으로 나타내는 것이
가능하다.)

> **명제**. $X = {x_1, \ldots, x_n}$을 벡터공간 $V$의 기저라고 하자. 이 때,
> $$ \forall x\in V \left[  \exists! c_i \in K \left[ x=\sum_{i=1}^{n}c_ix_i \right]\right] $$

*증명*. $X$는 벡터공간 $V$의 기저이므로, $c_i$의 존재는 분명하다.
$c_i$ 이외에 $d_i$가 $x\in V$에 대하여 $x= \sum_{i=1}^{n}d_ix_i$를 만족한다고 하자.
이 때, $0 = x-x = \sum_{i=1}^{n}c_ix_i- \sum_{i=1}^{n}d_ix_i = \sum_{i=1}^{n}(c_i-d_i)x_i$이고,
$X$의 선형독립성에 의하여, 임의의 $i$에 대하여 $c_i-d_i=0$. 따라서 $c_i$는 unique하게 존재. □

## 예시

- $i=1,\ldots,n$으로 하여
$\mathbf{e}_i = \,^t\left[ 0, \ldots, 1, \ldots, 0 \right]$ (왼쪽으로부터 $i$번째만이 $1$)로 정의하면,
이들이 이루는 집합이 체 $K$에 대하여 $K^n$의 기저임을 확인할 수 있다.
- $\Complex$를 $\R$상의 벡터공간으로 보면 $\left\{1, \sqrt{-1}\right\}$은 기저이다.
- $ \left\{ 1, x, \ldots, x^n \right\}$은 $K[x]_n = \left\{ f(x)\in K[x] \,|\, \deg(f(x)) \leq n \right\}$의 기저이다.

기저는 유한집합일 수도, 무한집합일 수도 있다. 특히 $V$의 기저 $X$가 유한집합일 경우
$X$를 유한기저, $V$를 유한생성인 벡터공간이라고 한다.

## 벡터공간의 기저의 존재

> **정리**(벡터공간상의 기저의 존재). 체 $K$ 상의 임의의 벡터공간 $V$에는
> 항상 기저(basis)가 존재한다.

*증명*. $X$를 각 원소가 선형독립인 $V$의 부분집합 전체의 집합으로 두자.
그렇다면, $X$는 정의상 공집합이 선형독립인 $V$의 부분집합이므로 공집합이 아님을 알 수 있다.
따라서, $X$는 $\subset$을 순서로 하여 순서집합을 이루고 있는 것 또한 알 수 있다.

$Y$가 $X$상의 사슬(chain, 즉 전순서인 부분집합)이라고 하자.
$Y$는 전순서이므로, 모든 $\bigcup Y$의 유한부분집합은 어떤 $Y$의 원소의 부분집합이 될 것이다.
이 때, $Y$의 모든 원소는 그것의 원소들이 선형독립이므로, $\bigcup Y$의 원소들 또한
선형독립임을 알 수 있다. 따라서 $\bigcup Y \in X$이고, 임의의 $y\in Y$에 대하여
$y\subset \bigcup Y$이므로, $\bigcup Y$는 $Y$의 상계가 된다.
따라서 $X$의 임의의 사슬은 유계이므로, [Zorn의 보조정리](./zorns-lemma.html)에 의하여
$X$는 극대인 원소를 갖는다. 이를 $M\in X$로 두자.

$M$이 $V$의 기저임을 보이자.

- $M\in X$로부터 $M$의 각 원소가 선형독립임을 알 수 있다.
- 귀류법을 이용하여 $\langle M\rangle\subset V$이 $V$와 일치하는 것을 보이자.
$x\not\in\langle M\rangle$인 $x\in V$가 존재한다고 가정하면,
$x\not\in M$일 것이므로, $M_x = M \cup {x}$로 두자.
$x$가 $M$의 원소들과 선형독립이라는 사실은 쉽게 알 수 있으므로,
$M_x$ 또한 $X$의 원소일 것이다. 하지만 $M\subsetneq M_x$인 동시에
$M_x\in X$라는 사실은 $M$이 $X$의 극대원소라는 사실에 모순되므로,
이러한 $x\in V$는 존재하지 않는다.

따라서 $M$은 $V$의 기저이다. □

예를 들어,
$\R$은 $\mathbb{Q}$상의 벡터공간이라는 것을 정의로부터 쉽게 보일 수 있으므로,
기저가 존재하며, 보통 이를 $\mathscr{B}$와 같이 표시한다.

## 기저와 차원

> **보조정리**. $V$를 $K$상의 벡터공간이라고 하자. $x_1, \ldots, x_r \in V$에 대하여
> $X = \langle x_1, \ldots, x_r \rangle$으로 두고, $y_1, \ldots, y_m\in X$인 동시에
> $ \left\{ y_1, \ldots, y_m \right\}$이 선형독립이라면, $m\leq r$이다.

> **정리**. $V$가 유한생성인 벡터공간이라고 하자. 이 때, $V$의 기저의 원소의 개수는
> 항상 일정하다.

## 참고문헌

- [Wikipedia, Basis(linear algebra)](https://en.wikipedia.org/wiki/Basis_(linear_algebra))
- [Andreas Blass, *Existence of bases implies the axiom of choice*](http://www.math.lsa.umich.edu/~ablass/bases-AC.pdf)
- 松坂 和夫, *線型代数入門*

