<!---
title: "평균값정리"
category: Analysis
language: Korean
--->

# 평균값정리

> **정리**(Rolle의 정리). $f: [a,b]\to\R$이 연속함수이고, $(a,b)$에서 미분가능이라고 하자.
> $f(a) = f(b)$라면, $\exists c\in (a,b) \left[ f'(c) = 0 \right]$이다.

*증명*.

1. $f(x) = C$인 경우: $f$가 상수함수라면 어느 지점 $x\in (a,b)$에서나 $f'(x) = 0$.
2. $f(x)> f(a) = f(b)$인 $x\in (a,b)$가 존재하는 경우:
$f$는 연속함수이므로, 최대최소치의 정리가 성립한다.
따라서 명백하게 $f(c)$가 구간내최고치가 되는 $c\in (a,b)$가 존재한다.
여기서 $f'(c) = \lim_{x\to c} \frac{f(x) - f(c)}{x-c}$가 존재하는 동시에
모든 $f(x)-f(c) \leq 0$이고, $x>c$에서는 $\frac{f(x) - f(c)}{x-c} \leq 0$이므로
$f'(c)\leq 0$,
$x<c$에서는 $\frac{f(x) - f(c)}{x-c} \geq 0$이므로 $f'(c)\geq 0$, 따라서
$f'(c) = 0$임을 알 수 있다.
3. $f(x) < f(a) = f(b)$인 $x\in (a,b)$가 존재하는 경우: 2와 마찬가지. □

> **정리**(Cauchy의 평균값정리). $f: [a,b]\to\R$과 $g: [a,b]\to\R$이 모두
> 연속함수이고, $(a,b)$에서 미분가능이라고 하자.
> $\forall x\in (a,b) \left[ g'(x)\neq 0 \right]$라고 하면,
> $\exists c\in (a,b) \left[ \frac{f(b)-f(a)}{g(b)-g(a)} = \frac{f'(c)}{g'(c)} \right]$
> 이다.

*증명*. $h(x) := (f(b) - f(a))(g(x) - g(a)) - (g(b)-g(a))(f(x) - f(a))$로 두자.
그렇다면, $h$는 $(a,b)$에서 미분가능, $[a,b]$에서 연속이다.
또한 $h(a) = 0 = h(b)$이므로, Rolle의 정리에 따라, $h'(c) = 0$인 $c\in (a,b)$가 존재한다.
$h'(x) = (f(b) - f(a))\cdot g'(x) - (g(b)-g(a))\cdot f'(x)$,
$0=h'(c) = (f(b) - f(a))\cdot g'(c) - (g(b)-g(a))\cdot f'(c)$,
$\frac{f(b) - f(a)}{g(b)-g(a)} = \frac{f'(c)}{g'(c)}$이다.
(여기서 $g(b) - g(a) \neq 0$인 이유는, Rolle의 정리의 대우로부터 알 수 있다.) □

> **따름정리**(평균값정리). 연속함수 $f: [a,b]\to\R$가 $(a,b)$에서 미분가능이라고 하자.
> 그렇다면, $\exists c\in (a,b) \left[ \frac{f(b) - f(a)}{b-a} = f'(c) \right]$이다.

*증명*. $g(x) = x$로 두면, $g'(x) = 1\neq 0$이므로, Cauchy의 평균값정리를 적용하여
일반의 평균값정리를 이용할 수 있다. □
