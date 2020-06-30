<!---
title: '$n!>\left( \frac{n}{e} \right)^n$'
language: Korean
category: Analysis
--->

# $n!>\left( \frac{n}{e} \right)^n$


> **명제**. 위로 유계인(upperly bounded) 단조증가열은 수렴한다.
> 또한, 실수의 연속성을 적용하면, 수렴하는 값은 그 수열의 상한(superemum)이다.

*증명*. 단조증가열 $\{a_n\}_{n\in\N}$에 대하여 $A = \{a_n|n\in\N\}$이라고 하자.
실수의 연속성을 적용하면, $\exists S = \sup A$이다. $\forall\varepsilon\in\R^{+}$에 대해,
$S-\varepsilon$은 상한의 정의상 상계(upper bound)이지 않으므로, $\exists n_0, a_{n_0}>S-\varepsilon$이다.
$a_n$은 단조증가열이므로, $n\geq n_0$에 대해 $S-\varepsilon<a_{n_0} \leq a_{n}\leq S$,
즉 $|a_{n} - S| < \varepsilon$ 임을 알 수 있다. 따라서 $a_n$은 $S$로 수렴한다. □

이 명제를 이용하여 수열 $\left( 1 + \frac{1}{n} \right)^n$이 $e$라는 특정한 값에
수렴하는 것을 보일 수 있다. 이 수열이 단조증가라는 것은 인접항의 비를 통하여
쉽게 알아낼 수 있다.
상계가 존재함을 보이기 위해, 구체적인 값으로 $3$을 제시하여 $\left( 1+\frac{1}{n} \right)^n<3$이
$n\geq 2$에서 성립함을 보이면 증명의 나머지 부분이 완성된다.
우선, $\left( 1+\frac{1}{n} \right)^n$ 을 이항 정리에 의해 전개하면,

$$
\begin{aligned}
\left( 1+\frac{1}{n} \right)^n &=
\sum_{k=0}^{n}\binom{n}{k}\left( \frac{1}{n} \right)^{k} \\
&= 2 + \sum_{k=2}^{n}\binom{n}{k}\left( \frac{1}{n} \right)^{k} \\
\end{aligned}
$$

이므로, $\sum_{k=2}^{n}\binom{n}{k}\left( \frac{1}{n} \right)^{k} < 1$
임을 보이기만 하면 된다.

$$
\begin{aligned}
\sum_{k=2}^{n}\binom{n}{k}\left( \frac{1}{n} \right)^{k}
&= \sum_{k=2}^{n}\frac{1}{k!}\cdot\frac{n(n-1)\cdots(n-(k-1))}{n^k} \\
&< \sum_{k=2}^{n}\frac{1}{k!} < \sum_{k=2}^{n}\frac{1}{2^{k-1}} < 1
\end{aligned}
$$

따라서, $\left( 1+\frac{1}{n} \right)^n$은 $3$보다 작거나 같은 어떤 실수 $e$로 수렴한다는 것을
알 수 있다. 또한, 강한 단조증가열이 $e$로 수렴하는 것으로부터 임의의 $n\in\N$에 대하여
$\left( 1+\frac{1}{n} \right)^n<e$이 성립한다는 사실을 알 수 있고,
다시 이로부터, 계승에 관한 부등식
$n!>\left( \frac{n}{e} \right)^n$ 를 수학적 귀납법으로 유도할 수 있다.

$n=1$인 경우에는
$1!>\frac{1}{e}$ 이 성립한다. $n=k$인 경우에 $k!>\left( \frac{k}{e} \right)^k$이 성립한다면
$\left( 1+\frac{1}{k} \right)^k<e$로부터 $k+1> \frac{\left( k+1 \right)^{k+1}}{ek^k}$이 성립하므로,

$$
(k+1)! = k!\cdot(k+1) > \left( \frac{k}{e} \right)^k\cdot
\frac{\left( k+1 \right)^{k+1}}{ek^k}= \left( \frac{k+1}{e} \right)^{k+1}
$$

와 같이 $n=k+1$일 때에도 성립하는 것을 알 수 있다. 따라서 부등식
$n!>\left( \frac{n}{e} \right)^n$이 성립한다.
