<!---
title: '자연상수 $e$'
category: Mathematics
language: Korean
--->

# 자연상수 $e$

자연상수, 혹은 Napier 상수로 불리는 $e$는 $2.71828\ldots$와 같이 나타나는 초월수인 무리수이다.
간혹, Euler 수로 불리는 경우도 있는 듯 하다. 실제로 이 수의 존재를 발견한 것은
Bernoulli의 업적으로 알려져 있으며, 이 수에 $e$라는 문자를 붙여 사용하기 시작하기 시작한 사람은
Euler로 알려져 있다.
일반적으로는 자연로그 $\ln$의 밑이며, 미분방정식 $y'=y$의 일반해에 해당하는 지수함수의 밑이다.

## $e$의 정의

**정의**.
$e$는 다음과 같은 수열의 극한에 의해 정의된다.

$$
e = \lim_{n\to\infty}\left(1+\frac{1}{n}\right)^{n}
$$

여기서 의문을 품을 수 있는 사항은, 이 급수가 정말로 수렴하냐는 것이다.
(물론 수렴하므로 이러한 정의를 내린 것이다.)
이에 대해서는 해석학적인 방법을 통해 답할 수 있다.

**명제**. 위로 유계인(upperly bounded) 단조증가열은 수렴한다.
또한, 실수의 연속성을 적용하면, 수렴하는 값은 그 수열의 상한(superemum)이다.

*증명*. 단조증가열 $\{a_n\}_{n\in\N}$에 대하여 $A = \{a_n|n\in\N\}$이라고 하자.
실수의 연속성을 적용하면, $\exists S = \sup A$이다. $\forall\varepsilon\in\R^{+}$에 대해,
$S-\varepsilon$은 상한의 정의상 상계(upper bound)이지 않으므로, $\exists n_0, a_{n_0}>S-\varepsilon$이다.
$a_n$은 단조증가열이므로, $n\geq n_0$에 대해 $S-\varepsilon<a_{n_0} \leq a_{n}\leq S$,
즉 $|a_{n} - S| < \varepsilon$ 임을 알 수 있다. 따라서 $a_n$은 $S$로 수렴한다. □

그렇다면, 위의 정의에 등장하는 수열이 위로 유계인 동시에 단조증가열인 것을 보이기만 하면,
이 극한이 수렴한다는 것을 보일 수 있을 것이다.
이를 위해, 먼저 위의 수열이 단조증가열임을 보이자.
이는 간단하다. $f(x) = \left(1+\frac{1}{x}\right)^x$ 인 함수가 단조증가함수임을 보이는
것으로, 위의 수열 또한 단조증가열임을 보일 수 있다.
$\log\left( f(x) \right) = x\left( \log(x+1) - \log(x) \right)$를 미분하면,

$$
\begin{aligned}
\frac{d}{dx} \log\left( f(x) \right) &= \log(x+1)-\log(x)+x\left( \frac{1}{x+1}-\frac{1}{x} \right) \\
&=-\log\left( \frac{x}{x+1} \right) + \frac{x}{x+1} - 1
\end{aligned}
$$

여기서 $\frac{x}{x+1}=k$로 두면, $\frac{d}{dx}\log f(x) = k - \left( \log\left( k \right)+1 \right)$
이고, $0<k<1$에서는 $k > \log(k) + 1$이므로, $\frac{d}{dx}\log\left( f(x) \right)>0$임을 알 수 있다.
즉, $\log\left( f(x) \right)$는 단조증가함수이며, $\log$또한 단조증가함수이므로,
$f(x)$또한 단조증가함수이다. 따라서, $a_n$이 단조증가열임을 보였다.

이제 위의 수열이 위로 유계임을 보이자.
여기서는 구체적인 상계로, $3$을 제시하여 $\left( 1+\frac{1}{n} \right)^n<3$이
$n\geq 2$에서 성립함을 보일 것이다.
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
알 수 있다.

## $e$에 관한 부등식

위 정의의 단계에서 단조증가열 $\left( 1+\frac{1}{n} \right)^n$을 평가한 결과는
$\left( 1+\frac{1}{n} \right)^n<e$라는 것을 상한의 정의로부터 알 수 있다.
이 결과를 이용하여, 계승에 관한 부등식 $n!>\left( \frac{n}{e} \right)^n$
를 수학적 귀납법으로 유도할 수 있다.

$n=1$인 경우에는
$1!>\frac{1}{e}$ 이 성립한다. $n=k$인 경우에 $k!>\left( \frac{k}{e} \right)^k$이 성립한다면
$\left( 1+\frac{1}{k} \right)^k<e$로부터 $k+1> \frac{\left( k+1 \right)^{k+1}}{ek^k}$이 성립하므로,

$$
(k+1)! = k!\cdot(k+1) > \left( \frac{k}{e} \right)^k\cdot
\frac{\left( k+1 \right)^{k+1}}{ek^k}= \left( \frac{k+1}{e} \right)^{k+1}
$$

와 같이 $n=k+1$일 때에도 성립하는 것을 알 수 있다. 따라서 부등식
$n!>\left( \frac{n}{e} \right)^n$이 성립한다.

