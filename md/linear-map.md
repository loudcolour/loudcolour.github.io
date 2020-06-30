<!---
title: "선형사상"
category: Linear Algebra
language: Korean
--->

# 선형사상

## 정의

> **정의**(선형사상). 체 $K$ 상의 벡터공간 $U, V$에 대하여, $T: U\to V$가
> 선형사상(linear map)이란
> 다음 두 조건을 동시에 만족하는 것을 의미한다.
>
> - $x,y\in U$에 대하여 $T(x+y) = T(x) + T(y)$
> - $x\in U$, $\alpha\in K$에 대하여 $T(\alpha x) = \alpha T(x)$

> **명제**. 다음이 성립한다.
>
> - $0_U$, $0_V$를 각각 $U$, $V$의 영벡터라고 할 때, $T(0_U) = 0_V$
> - 임의의 $x\in U$에 대하여 $T(-x) = -T(x)$

*증명*.

- 어떤 $x\in U$에 대하여 $T(\alpha x) = \alpha T(x)$가 성립하므로, $\alpha=0$로
  두면 된다.
- 역시 $x\in U$에 대하여 $T(\alpha x)= \alpha T(x)$가 성립하므로, $\alpha=-1$로
  두면 된다. □

## 예시

- $A\in M_{m,n}(K)$에 대하여, $T_A: K^n\to K^m, x\mapsto Ax$로 두면, $T_A$는 선형사상이다.
	* $T_A(x+y)=A(x+y)=Ax + Ay = T_A(x)+T_A(y)$
	* $T_A(\alpha x)=A(\alpha x)= \alpha Ax=\alpha T_A(x)$
- $\text{tr}: M_n(K)\to K, (a_{ij})\mapsto \sum_{i=1}^{n}a_{ii}$은 선형사상이다.
- $ \frac{d}{dx}: K[x]_n \to K[x]_n, f(x)\mapsto f'(x)$는 선형사상이다.

## 핵(kernel), 상(image)

> **정의**. $U, V$를 $K$ 상의 벡터공간이라고 하자. 선형사상 $T: U\to V$에 대하여
> 
> - $\text{Im}(T) := \left\{ T(x) \,|\, x\in U \right\}$를 $T$의 **상(image)** 이라고 한다.
> - $\text{Ker}(T) := \left\{ x\in U \,|\, T(x) = 0 \right\}$를 $T$의 **핵(kernel)** 이라고 한다.

> **명제**. $U, V$를 $K$ 상의 벡터공간이라고 하자. 선형사상 $T: U\to V$에 대하여
> $\text{Im}(T)$와 $\text{Ker}(T)$는 각각 $V$와 $U$의 부분공간이다.

> **명제**. $U, V$를 $K$ 상의 벡터공간이라고 하자. 선형사상 $T: U\to V$에 대하여
> $U = \langle a_1, \ldots, a_n \rangle$과 같이 주어졌다면,
> $\text{Im}(T) = \langle T(a_1), \ldots, T(a_n) \rangle$이다.

> **정리**. $U, V$를 $K$ 상의 유한생성인 벡터공간이라고 하자. 선형사상 $T: U\to V$에 대하여
> $\dim U = \dim \text{Ker}(T) + \dim \text{Im}(T)$

> **명제**. $U, V$를 $K$ 상의 벡터공간이라고 하자. 선형사상 $T: U\to V$에 대하여
> 다음 두 조건은 동치이다.
>
> 1. $T$가 단사사상이다.
> 2. $\text{Ker}(T) = \left\{ 0 \right\}$

> **정의**. $U$를 $K$ 상의 벡터공간이라고 하자. 선형사상 $T: U\to U$를
> 선형변환(linear transformation)이라고 한다.

> **따름정리**. $U$를 $K$ 상의 *유한생성* 벡터공간이라고 하자. 선형변환 $T: U\to U$에 대하여
> 다음 두 조건은 동치이다.
>
> 1. $T$가 단사사상이다.
> 2. $T$가 전사사상이다.

*주*. 유한생성인 벡터공간이 아닌 경우에는 이 따름정리가 항상 성립하리라는 보장은 없다.
반례로, $f: \R^{\infty}\to\R^{\infty}, (x_1, x_2, \ldots)\mapsto (0, x_1, x_2, \ldots)$는
단사이지만 전사이지 않다.

## 동형사상, 동형

> **정의**. $U,V$를 $K$ 상의 벡터공간이라고 하자. 선형사상 $T: U\to V$가 전단사인 경우,
> $T$는 동형사상(isomorphism)이라고 한다. 또한 $U$와 $V$는 동형(isomorphic)이라고 하며,
> $U\simeq V$로 이를 나타낸다.

$U\simeq V$라면 $V\simeq U$라는 것은 역사상의 존재로부터 쉽게 알 수 있다.

> **명제**. $V$를 $K$ 상의 벡터공간, $X = \{x_1, \ldots, x_n\}$이 $V$의
> 기저라고 하자.
> $T: K^n\to V, \,^t \left[ c_1, \ldots, c_n \right]\mapsto \sum_{i=1}^{n}c_ix_i$
> 는 동형사상이다. 따라서 $K^n\simeq V$

