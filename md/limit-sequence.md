<!---
title: "수열의 극한"
category: Mathematics
language: Korean
--->

# 수열의 극한

> **정의**(근방). $x=x_0\in\R$을 중심으로 하는 반경 $R$의 근방 $N(x_0, R)$을
> $N(x_0, R):= \left\{ x\in \R \,|\, \left|x-x_0\right| < R \right\}$과 같이 정의한다.

> **정의**(수열). $\N$에서 $\R$으로의 사상 $a$를 수열이라고 하며, $a(n)$을 $a_n$과 같이 쓴다.

> **정의**($\varepsilon$-$N$ 논법에 의한 수열의 극한). $\lim_{n\to\infty} a_n = \alpha$는 다음을 의미한다.
$$
\forall\varepsilon>0, \exists N\in\N, \forall n\in\N \left[ n\geq N \implies a_n\in N(\alpha, \varepsilon) \right]
$$

만약, $\lim_{n\to\infty} a_n $가 실수로 존재한다면, $ \left\{ a_n \right\}$은 수렴,
존재하지 않는다면, 발산한다고 한다.

> **명제**. $\lim_{a_n} = \alpha$인 동시에 $\lim_{a_n} = \beta$이면 $\alpha = \beta$이다.

> **정의**(수열의 유계). 수열 $ \left\{ a_n \right\}$이 유계라는 것은 다음을 의미한다.
$$
\exists M>0, \forall n\in\N \left[ |a_n| \leq M \right]
$$

> **명제**. 수렴하는 수열은 유계이다.

> **정리**. $\lim_{n\to\infty} a_n = \alpha$, $\lim_{n\to\infty} b_n = \beta$라고 하면
> 다음이 성립한다.
>
> 1. $\lim_{n\to\infty} \left\{ f(x) + g(x) \right\} = \alpha + \beta$
> 1. $\lim_{n\to\infty} \left\{ f(x)g(x) \right\} = \alpha\beta$
> 1. $\beta \neq 0$이고, $\frac{a_n}{b_n}$이 수열로서 정의된다면, $\lim_{n\to\infty} \frac{a_n}{b_n} = \frac{\alpha}{\beta}$

> **명제**. $ \lim_{n \to \infty} a_n = \alpha$, $ \lim_{n \to \infty} b_n = \beta$라고 하자. 임의의 $n\in\N$에 대하여
> $a_n \leq b_n$이 성립한다면, $a\leq b$이다.

> **명제**. $ \lim_{n \to \infty} a_n = \lim_{n \to \infty} b_n = \alpha$이고, 임의의 $n\in\N$에 대하여
> $a_n \leq c_n \leq b_n$이 성립한다고 하면, $ \lim_{n \to \infty} c_n = \alpha$이다.

## Bolzano-Weierstrass 정리

## Cauchy열

