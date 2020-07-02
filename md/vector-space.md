<!---
title: "벡터공간"
category: Linear Algebra
language: Korean
--->

# 벡터공간

## 정의

> **정의**(벡터공간). 공집합이 아닌 집합 $V$가 체 $K$상의 벡터공간이란, 다음 조건을
> 만족하는 것을 의미한다.
>
> - 가법에 해당하는 연산이 존재하여, 가환군을 이룬다.
> 즉, $\vec x, \vec y, \vec z\in V$로 하여
> 	- $(\vec x+ \vec y)+ \vec z = \vec x+(\vec y+\vec z)$
> 	- $\exists \vec 0\in V \left[ \vec x+\vec 0 =\vec x \right]$
> 	- $\exists (-\vec x)\in V \left[ \vec x+(-\vec x) = \vec 0 \right]$
> 	- $\vec x+\vec y = \vec y+\vec x$
> - 스칼라배의 연산이 존재한다. 즉 $\alpha, \beta\in K$, $\vec x,\vec y\in V$에 대하여
> 	- $\alpha(\vec x+\vec y) = \alpha \vec x + \alpha \vec y$
> 	- $(\alpha+\beta)\vec x=\alpha \vec x + \beta \vec x$
> 	- $\alpha(\beta \vec x)=(\alpha\beta)\vec x$
> 	- $1_K\cdot \vec x = \vec x$ ($1_K$는 $K$의 승법에 관한 항등원)

위에서 조건에서 $\vec 0$와 $-\vec x$가 각각 존재한다면, 이는 unique하다.

> **명제**. $V$를 $K$ 상의 벡터공간이라고 하자.
>
> 1. 임의의 $\vec x\in V$에 대하여 $0_K\cdot \vec x = \vec 0$
> ($0_K$는 $K$의 가법에 관한 항등원)
> 1. 임의의 $\alpha \in K$에 대하여 $\alpha\cdot \vec 0=\vec 0$
> 1. 임의의 $(-1_K)\vec x = -\vec x$

위에서는 벡터와 스칼라를 구분짓기 위해 $1_K, 0_K$를 체 $K$ 상의 스칼라 값으로 사용했지만,
일반적으로 혼동이 없는 한, $1, 0$으로 각각 승법과 가법의 항등원을 표기하도록 하자.

*증명*.

1. $0\cdot \vec x = ( 0 + 0)\cdot \vec x = 0\cdot\vec x + 0\cdot\vec x$,
$0\cdot\vec x = \vec 0$
2. $\alpha\cdot\vec 0 = \alpha\cdot (\vec 0 + \vec 0) = \alpha\cdot\vec 0 + \alpha\cdot\vec 0$,
$\alpha\cdot\vec 0 = \vec 0$
3. $\vec 0 = 0\cdot\vec x = (1 + (-1))\cdot\vec x = 1\cdot\vec x + (-1)\cdot\vec x$,
$-\vec x = (-1)\cdot\vec x$ □

## 예시

- $\{ \vec 0 \}$은 벡터공간이라는 것을 쉽게 확인할 수 있다.
이를 자명한 벡터공간이라고 한다.
- $K^n$은 $K$상의 벡터공간이다. 당연히 $K$ 또한 $K$상의 벡터공간이다.
- $K$계수 일차다항식 전체의 집합 $K[x]$은 $K$상의 벡터공간이다.
- 복소수 전체의 집합 $\Complex$는 실수 전체의 집합 $\R$상의 벡터공간이다.
- 실수 전체의 집합 $\R$는 유리수 전체의 집합 $\mathbb{Q}$상의 벡터공간이다.
- 구간 $(a,b)$상의 연속인 실함수 전체의 집합
$C(a,b):= \left\{ f: (a,b)\to \R \,|\, f: \text{continuous} \right\}$는
$\R$ 상의 벡터공간이다.

## 선형결합, 선형독립

> **정의**. $K$상의 벡터공간 $V$에 대하여 $\vec x_1, \ldots, \vec x_k \in V$라고 할 때,
>
> - $c_i\in K$, $ \sum_{i=1}^{k}c_i\vec x_i = c_1\vec x_1 + \cdots c_k\vec x_k$를
> $\vec x_1, \ldots, \vec x_k$의 **선형결합(linear combination)** 이라고 한다.
> - $c_i\in K$, $ \sum_{i=1}^{k}c_i\vec x_i = c_1\vec x_1 + \cdots c_k\vec x_k=\vec 0$를
> $\vec x_1, \ldots, \vec x_k$에 관한 **선형관계식(linear relation)** 이라고 한다.

만약 임의의 $i$에 대해 $c_i = 0$라면 $ \sum_{i=1}^{k}c_ix_i=\vec 0$가 성립하는
것은 자명하다. 이를 자명한 선형관계식이라고 한다.

> **정의**. $K$상의 벡터공간 $V$에 대하여 $\vec x_1,\ldots,\vec x_k\in V$에 관한
> 자명하지 않은 선형관계식이 존재하지 않는다면,
> $\vec x_1, \ldots, \vec x_k$ 혹은 그 집합 $\{\vec x_1, \ldots, \vec x_k\}$는
> **$K$상 선형독립(linearly independent)** 이라고 한다. 즉,
$$
c_i\in K, \sum_{i=1}^{k}c_i\vec x_i = \vec 0 \implies \forall i [ c_i = 0]
$$
> 이라면 $\{\vec x_1, \ldots, \vec x_k\}$는 선형독립이다.

> **명제**. 체 $K$에 대하여 $\vec x_1, \ldots, \vec x_n\in K^n$일 때,
> 다음 두 조건은 동치이다.
>
> 1. $X = {\vec x_1, \ldots, \vec x_n}$이 $K$상 선형독립.
> 1. $\det \left[ \vec x_1\,\cdots\,\vec x_n \right]\neq 0$.

*증명*. $A = \left[ \vec x_1\,\cdots\,\vec x_n \right]$라고 하자.

$$
\begin{aligned}

\det A \neq 0 &\iff A\in \text{GL}_n(K) \\
&\iff \forall\vec x\in K^n \left[ A\vec x = \vec 0  \implies \vec x = \vec 0 \right]

\end{aligned}
$$

이고, $\vec x = (c_1, \ldots, c_n)$라고 하면, $A\vec x = \sum_{i=1}^{n} c_i\vec x_i$이므로,

$$
\forall\vec x\in K^n \left[ A\vec x = \vec 0  \implies \vec x = \vec 0 \right]
\iff \left[ \sum_{i=1}^{n}c_i\vec x_i 
=\vec 0 \implies \forall i \left[ c_i = 0 \right] \right] 
$$

이는 $ \left\{ \vec x_1, \ldots, \vec x_n \right\}$이 선형독립임을 의미한다. □

## 부분공간

### 정의

### 생성공간

### 부분공간의 연산

> **정리**. $K$상의 벡터공간 $V$의 두 부분공간 $W_1, W_2\subset V$에 대하여,
> $W_1\cap W_2$과
> $W_1+W_2:= \left\{ \vec x_1 + \vec x_2 \,|\, \vec x_1\in W_1, \vec x_2\in W_2 \right\}$
> 은 $V$의 부분공간이다.

*주*. 포함관계의 대소에 따라, $W_1\cap W_2$는 $W_1$와 $W_2$에 동시에 포함되는 최대의
$V$의 부분공간이다. 또한 $W_1+W_2$는 $W_1$와 $W_2$를 동시에 포함하는 최소의 $V$의
부분공간이다.

> **정의**. $W_1, W_2\subset V$가 $K$상의 벡터공간 $V$의 부분공간이라고 하자.
> $\vec x \in W := W_1 + W_2$에 대하여, $\vec x = \vec x_1 + \vec x_2$인
> $\vec x_1\in W_1$과 $\vec x_2\in W_2$가 unique하게 정해진다면,
> $W = W_1\oplus W_2$와 같이 쓴다.

*주*. $W = W_1\oplus W_2$이면, $W = W_1 + W_2$인 동시에 $W_1\cap W_2= \{\vec 0\}$
이다. 역도 성립한다.

> **정의**. $W_i\subset V$ ($i= 1,2,\ldots, m$)가 $K$ 상의 벡터공간 $V$의 부분공간이라고
> 하자. $\vec x \in W := W_1 + \cdots + W_m$에 대하여
> $\vec x = \sum_{i=1}^{m} \vec x_i$ 인 $\vec x_i\in W_i$가 unique하게 정해진다면,
> $W = W_1\oplus \cdots \oplus W_m = \bigoplus_{i=1}^{m}W_m$와 같이 쓴다.

*주*. $W = \bigoplus_{i=1}^{m}W_m$이라고 하면,
모든 $i = 1,\ldots, m$에 대하여 $W_i\cap \left( \sum_{j=1}^{i-1}W_j + \sum_{j=i+1}^{m} W_j \right) = \{\vec 0\}$
이 성립한다. 역도 성립한다.
