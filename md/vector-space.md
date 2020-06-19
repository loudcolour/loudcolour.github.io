<!---
title: "벡터공간"
category: Mathematics
language: Korean
--->

# 벡터공간

## 정의

> **정의**(벡터공간). 공집합이 아닌 집합 $V$가 체 $K$상의 벡터공간이란, 다음 조건을
> 만족하는 것을 의미한다.
>
> - 가법에 해당하는 연산이 존재하여, 가환군을 이룬다. 즉, $x,y,z\in V$로 하여
> 	- $(x+y)+z = x+(y+z)$
> 	- $\exists! 0\in V \left[ x+0 = x \right]$
> 	- $\exists! (-x)\in V \left[ x+(-x) = 0 \right]$
> 	- $x+y = y+x$
> - 스칼라배의 연산이 존재한다. 즉 $\alpha, \beta\in K$, $x,y\in V$에 대하여
> 	- $\alpha(x+y) = \alpha x + \alpha y$
> 	- $(\alpha+\beta)x=\alpha x + \beta x$
> 	- $\alpha(\beta x)=(\alpha\beta)x$
> 	- $1_K\cdot x = x$ ($1_K$는 $K$의 승법에 관한 항등원)

> **명제**. $V$를 $K$ 상의 벡터공간이라고 하자.
>
> 1. 임의의 $x\in V$에 대하여 $0_K\cdot x = 0$ ($0_K$는 $K$의 가법에 관한 항등원)
> 1. 임의의 $\alpha \in K$에 대하여 $\alpha\cdot 0=0$
> 1. 임의의 $(-1_K)x = -x$

위에서는 벡터와 스칼라를 구분짓기 위해 $1_K, 0_K$를 체 $K$ 상의 스칼라 값으로 사용했지만,
일반적으로 혼동이 없는 한, $1, 0$으로 각각 승법과 가법의 항등원을 표기하도록 하자.

## 예시

- $ \left\{ 0 \right\}$은 벡터공간이라는 것을 쉽게 확인할 수 있다. 이를 자명한 벡터공간이라고 한다.
- $K^n$은 $K$상의 벡터공간이다. 당연히 $K$ 또한 $K$상의 벡터공간이다.
- $K$계수 일차다항식 전체의 집합 $K[x]$은 $K$상의 벡터공간이다.
- 복소수 전체의 집합 $\Complex$는 실수 전체의 집합 $\R$상의 벡터공간이다.
- 구간 $(a,b)$상의 연속인 실함수 전체의 집합 $C(a,b):= \left\{ f: (a,b)\to \R \,|\, f: \text{continuous} \right\}$
  는 $\R$ 상의 벡터공간이다.

## 선형결합, 선형독립

> **정의**. $K$상의 벡터공간 $V$에 대하여 $x_1, \ldots, x_k \in V$라고 할 때,
>
> - $c_i\in K$, $ \sum_{i=1}^{k}c_ix_i = c_1x_1 + \cdots c_kx_k$를 $x_1, \ldots, x_k$의 선형결합(linear combination)이라고 한다.
> - $c_i\in K$, $ \sum_{i=1}^{k}c_ix_i = c_1x_1 + \cdots c_kx_k=0$를 $x_1, \ldots, x_k$에 관한 선형관계식(linear relation)이라고 한다.

만약 임의의 $i$에 대해 $c_i = 0$라면 $ \sum_{i=1}^{k}c_ix_i=0$가 성립하는 것은 자명하다. 이를 자명한 선형관계식이라고 한다.

> **정의**. $K$상의 벡터공간 $V$에 대하여 $x_1,\ldots,x_k\in V$에 관한 자명하지 않은 선형관계식이 존재하지 않는다면,
> $x_1, \ldots, x_k$ 혹은 그 집합 $\{x_1, \ldots, x_k\}$는 **선형독립(linearly independent)** 이라고 한다. 즉,
$$
c_i\in K, \sum_{i=1}^{k}c_ix_i \implies \forall i [ c_i = 0]
$$
> 이라면 $\{x_1, \ldots, x_k\}$는 선형독립이다.

> **명제**. 체 $K$에 대하여 $x_1, \ldots, x_n\in K^n$일 때, 다음 두 조건은 동치이다.
>
> 1. $X = {x_1, \ldots, x_n}$이 선형독립
> 1. $\det \left[ x_1\,\cdots\,x_n \right]\not=0$

