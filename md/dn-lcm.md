<!---
title: '$1,\ldots,n$의 최소공배수'
category: Analysis
language: Korean
--->

# $1,\ldots,n$의 최소공배수

자연수 $1,\ldots,n$의 최소공배수를 $d_n$이라고 하자.
그리고, $2$ 이상의 자연수 $n$에 대하여 $n$이하의 소수의 개수를 $\pi(n)$이라고 하자.
최소공배수의 정의에 따라,

$$
d_n = \prod_{p\leq n}p^{\lfloor{\log_{p}n\rfloor}}
$$

이다. (단, $p$는 소수.)

> **명제**. $n$이 충분히 크다면, $d_n\sim e^n$이다.

*증명*. 위에서 $\pi(n)$을 정의하였으므로,

$$
d_n = \prod_{p\leq n}p^{\lfloor{\log_{p}n\rfloor}} \sim \prod_{p\leq n}p^{\log_{p}n} = \prod_{p\leq n}n = n^{\pi(n)}
$$

가 성립한다. 이 때, 소수정리에 의하여,

$$
n^{\pi(n)} \sim n^{\frac{n}{\log n}} = e^n
$$

이다. 따라서, $d_n\sim e^n$가 성립한다. □

위 명제를 이용하여, $e$ 이상의 실수인 $e'$를 정하여 $e'^n$을 $d_n$에
대한 유효한 평가로 사용할 수 있다.
