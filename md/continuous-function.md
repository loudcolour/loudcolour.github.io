<!---
title: "연속함수"
category: Mathematics
language: Korean
--->

# 연속함수

## 각점연속의 정의

> **정의**(한 점에서의 연속). $I$를 구간, $f$를 $I$상의 함수라고 하자.
> $f$가 $x=x_0$에서 연속이란, $\lim_{x\to x_0}f(x) = f(x_0)$가 성립하는 것을
> 의미한다.

*주*. 만약 $x_0$가 $I$의 가장자리에 있는 점이라면, 좌극한이나 우극한을 이용하여
이를 정의할 수 있다. 이러한 점을 피하고자 개구간을 정의역으로 제한하는 방법도 고려된다.

> **정의**(각점연속함수). 구간 $I$의 모든 점에서 $f$가 연속이라면,
> $f$는 구간 $I$에서 연속인 함수이다.

여기서 주의해야 할 점은, $f$가 $x=x_0$에서 연속일 때, $f(x_0)$는 항상
정의되어 있어야 한다는 것이다. 이는 극한의 정의에서 $x_0$를 제외하였던 것과는
대비되는 부분으로, 아래와 같은 논리식을 사용하여 함수 $f$가 $I$상에서 연속임을
정의할 수 있다.

$$
\forall x_0\in I,
\forall \varepsilon>0, \exists \delta > 0, \forall x\in I
\left[ x\in N(x_0,\delta) \implies f(x)\in N(f(x_0), \varepsilon) \right]
$$

각점연속함수는 보통 아래의 균등연속함수와 구분할 필요가 없다면,
연속함수로 부른다.

> **명제**. $f$를 구간 $I$상의 함수라고 할 때, 다음 두 조건은 동치이다.
>
> 1. $f$가 $x_0\in I$에서 연속
> 1. $\lim_{n\to\infty}x_n = x_0$인 임의의 수열 $\left\{ x_n \right\}$에 대하여,
>    $ \lim_{n \to \infty}f(x_n) = f(x_0)$가 성립한다.

*증명*. [함수의 극한](./limit-function.html)에서 보인 명제를
$\lim_{x\to x_0} f(x) = f(x_0)$에 적용하면 된다.

> **명제**. $f(x), g(x)$가 $I$상의 연속함수이면,
> 다음 역시 연속함수이다.
>
> 1. $f(x) + g(x)$
> 1. $f(x)g(x)$
> 1. 임의의 $x\in I$에 대하여 $g(x)\neq 0$이라면, $\frac{f(x)}{g(x)}$

## 균등연속의 정의

> **정의**(균등연속함수). $I$를 구간, $f: I\to \R$이라고 할 때,
> $f$가 균등연속인(uniformly continuous) 함수라는 것은 다음을 의미한다.
>
$$
\forall \varepsilon>0, \exists\delta>0, \forall x\in I, \forall y\in I
\left[ x\in N(y, \delta) \implies f(x)\in N(f(y), \varepsilon) \right]
$$

> **명제**. 연속함수인 $f: [a,b]\to \R$은 균등연속함수이다.

## 중간값정리

> **정리**(최대최소치의 정리). $f: [a,b]\to\R$이 연속함수라면,
> 최대치 $\max \left\{ f(x) \,|\, x\in [a,b] \right\}$와
> 최소치 $\min \left\{ f(x) \,|\, x\in [a,b] \right\}$가 존재한다.

*증명*.

## 최대최소치의 정리


> **정리**(중간값정리). $f: [a,b]\to \R$이 연속함수라고 하자.
> 이 때, $f(a)\neq f(b)$라면, $f(a)$와 $f(b)$사이의 임의의 값 $\mu$에
> 대하여 $f(c) = \mu$를 만족하는 $c\in (a,b)$가 존재한다.

*증명*.
