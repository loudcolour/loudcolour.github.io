<!---
title: 벡터공간의 기저
language: Korean
category: Mathematics
--->

# 벡터공간의 기저

## 정의

> **정의**. 체 $K$ 상의 벡터공간 $V$가 주어졌을 때, 집합 $X\subset V$가 $V$의
> 기저(basis)라는 것은, 다음을 동시에 만족하는 것을 의미한다.
>
> 1. $X$의 각 원소가 선형독립 ($X=\emptyset$인 경우도 이를 만족하는 것으로 본다.)
> 2. $\langle X \rangle = V$

## 벡터공간의 기저의 존재

> **정리**(벡터공간상의 기저의 존재). 체 $K$ 상의 임의의 벡터공간 $V$에는
> 항상 기저(basis)가 존재한다.

*증명*. $X$를 각 원소가 선형독립인 $V$의 부분집합 전체의 집합으로 두자.
그렇다면, $X$는 정의상 공집합이 선형독립힌 $V$의 부분집합이므로 공집합이 아님을 알 수 있다.
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

## 참고문헌

- [Wikipedia, Basis(linear algebra)](https://en.wikipedia.org/wiki/Basis_(linear_algebra))

