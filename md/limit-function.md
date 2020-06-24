<!---
title: "함수의 극한"
category: Mathematics
language: Korean
--->

# 함수의 극한

## 극한의 정의, $\varepsilon$-$\delta$ 논법

> **정의**(근방). $x=x_0\in\R$을 중심으로 하는 반경 $R$의 근방 $N(x_0, R)$을
> $N(x_0, R):= \left\{ x\in \R \,|\, \left|x-x_0\right| < R \right\}$과 같이 정의한다.

> **정의**(함수의 극한). $x_0\in \R$이 주어졌을 때,
> 어떤 $R\in\R$이 존재하여, 함수 $f$가 $N(x_0, R)\setminus \left\{ x_0 \right\}$
> 에서 정의되어 있다고 하자. 이 때, $\lim_{x\to x_0}f(x) = \alpha$란, 다음이 성립하는
> 것을 의미한다.
$$
\forall \varepsilon>0, \exists\delta > 0, \forall x\left[ x\in N(x_0, \delta)\setminus
\left\{x_0\right\} \implies f(x) \in N(\alpha, \varepsilon)
\right]
$$

> **정의**(함수의 극한, 무한의 경우). 어떤 $a\in\R$에 대하여
> $f: \left( a,\infty \right) \to \R$이 주어졌을 때,
> $\lim_{x\to\infty} f(x) =\alpha$란, 다음이 성립하는 것을 의미한다.
$$
\forall \varepsilon>0, \exists M>0, \forall x\left[ x> M \implies f(x)\in N(\alpha, \varepsilon) \right]
$$

*주*. 마찬가지로 $\lim_{x\to -\infty}f(x) = \alpha$를 정의할 수 있다.

> **명제**. $\lim_{x\to x_0} f(x) = \alpha$, $\lim_{x\to x_0} g(x) = \beta$라고 하면
> 다음이 성립한다.
>
> 1. $\lim_{x\to x_0} \left\{ f(x) + g(x) \right\} = \alpha + \beta$
> 1. $\lim_{x\to x_0} \left\{ f(x)g(x) \right\} = \alpha\beta$
> 1. $\beta \neq 0$이고, $\frac{f(x)}{g(x)}$가 함수로서 정의된다면, $\lim_{x\to x_0} \frac{f(x)}{g(x)} = \frac{\alpha}{\beta}$

*증명*. [수열의 극한](./limit-sequence.html)에서와 비슷한 방법으로 증명할 수 있다. □

> **명제**. 다음 두 조건은 동치이다.
>
> 1. $\lim_{x\to x_0} f(x) = \alpha$
> 1. $\lim_{n\to\infty} x_n = x_0$, $x_n\neq x_0$인 임의의 수열 $ \left\{ x_n \right\}$
>    에 대하여 $\lim_{n\to\infty} f(x_n) = \alpha$

*증명*.

**1에서 2를 유도**  
$\lim_{x\to x_0} f(x) = \alpha$가 성립한다고 하자.
이 때, $ \left\{ x_n \right\}$을 $x_n\neq x_0$, $\lim_{n\to\infty}x_n = x_0$인
수열이라고 하자. $\lim_{x\to x_0} f(x) = \alpha$에 의하여

$$
\forall \varepsilon > 0, \exists\delta >0, \forall x\left[ x\in N(x_0, \delta)\setminus
\left\{ x_0 \right\}\implies f(x)\in N(\alpha, \varepsilon) \right]
$$

한편, $x_n$에 주어진 조건에 의하여

$$
\begin{aligned}
\exists N\in\N, \forall n\in N: n \geq N &\implies x_n\in N(x_0, \delta)\setminus \left\{ x_0 \right\} \\
&\implies f(x_n)\in N(\alpha, \varepsilon)
\end{aligned}
$$

가 성립하는 것을 알 수 있다. 수열의 극한의 정의에 따라서 $\lim_{n\to\infty} f(x_n) =\alpha$

**2에서 1을 유도**  
$\lim_{x\to x_0}f(x)=\alpha$가 성립하지 않는다고 가정하자.
이를 논리식으로 쓰면

$$
\exists \varepsilon_0 >0, \forall \delta >0, \exists x_\delta
\left[ x\in N(x_0, \delta)\setminus \left\{ x_0 \right\} \land
f(x)\notin N(\alpha, \varepsilon)\right]
$$

과 같다. $\delta$는 임의이므로, $\delta = \frac{1}{n}$일 때의 $x_\delta$를
하나 뽑아, 이를 $a_n$으로 두자. 그렇다면
$a_n\in N(x_0, \frac{1}{n})\setminus \left\{ x_0 \right\}$이 성립하므로,
$\lim_{n\to\infty}a_n = x_0$인 동시에 $a_n\neq x_0$임을 알 수 있다.
그러나 $f(a_n) \notin N(\alpha, \varepsilon_0)$이므로, 이는
$\lim_{n\to\infty}f(a_n)=\alpha$가 성립하지 않음을 의미한다. 따라서 이는 모순. □

> **명제**. 다음 두 조건은 동치이다.
>
> 1. $\lim_{x\to x_0} f(x)$가 존재한다.
> 1. $\varepsilon>0, \delta>0, \forall x_1, \forall x_2 \left[ x_1,x_2\in N(x_0, \delta)\setminus \left\{ x_0 \right\} \implies \left|f(x_1)-f(x_2)\right|<\varepsilon \right]$

*증명*.

**1에서 2를 유도**  
$\lim_{x\to x_0}f(x) = \alpha$라고 하자.
그렇다면

$$
\forall\varepsilon>0, \exists\delta>0, \forall x\left[ x\in N(x_0, \delta)\setminus \left\{ x_0 \right\}
\implies f(x)\in N\left(\alpha, \frac{\varepsilon}{2}\right)\right]
$$

이므로, $x_1, x_2\in N(x_0, \delta)\setminus \left\{ x_0 \right\}$가 성립할 때,

$$
\left|f(x_1) - f(x_2)\right| \leq \left|f(x_1)-f(x_0)\right|
+\left|f(x_2) - f(x_0)\right| <
\frac{\varepsilon}{2}
+\frac{\varepsilon}{2} = \varepsilon
$$

이다.

**2에서 1을 유도**  
2가 성립한다고 하자. 여기서
$ \left\{ x_n \right\}$을 $\lim_{n\to\infty} x_n = x_0$, $x_n\neq x_0$인 수열이라고 하면,
$\exists N\in\N, \forall n\in\N \left[ n\geq N\implies x_n\in N\left( x_0, \delta \right)\setminus \left\{ x_0 \right\} \right]$
이다.
따라서 $m,n\in\N$이 $m,n\geq N$을 만족하면
$x_m, x_n\in N(x_0,\delta)\setminus \left\{ x_0 \right\}$
이고,
$|f(x_m) - f(x_n)| < \varepsilon$이다.
이는 새로 얻은 수열 $ \left\{ f(x_n) \right\}$이 Cauchy열이라는 것을 의미한다.
따라서 $ \left\{ f(x_n) \right\}$은 수렴하고, $\lim_{n\to\infty} f(x_n) =\alpha$로
둘 수 있다.

여기서, 임의의 $y_n\neq x_0$, $ \lim_{n \to \infty}y_n = x_0$인
수열 $ \left\{ y_n \right\}$에 대하여 $ \left\{ f(y_n) \right\}$ 또한
$ \left\{ f(x_n) \right\}$과 마찬가지로 수렴한다는 것을 알 수 있으므로,
$ \lim_{n \to \infty}f(y_n) = \alpha$라는 것을 보이면,
위의 정리에 의하여 $\lim_{x\to x_0}f(x) = \alpha$, 1이 보여진다.

만약, 새로운 수열 $ \left\{ z_n \right\}$을 $z_{2n-1} = x_n$, $z_{2n} = y_n$과
같이 구성하면, 간단한 증명에 의하여 $ \lim_{n \to \infty}z_n = x_0$임을 알 수 있다.
또한 $z_n \neq x_0$. 따라서 $ \left\{ f(z_n) \right\}$은 수렴할 것이고,
그 부분열 $ \left\{ f(x_n) \right\}$이 $ \lim_{n \to \infty}f(x_n) = \alpha$으로 수렴하므로
$ \lim_{n \to \infty}f(z_n) = \alpha$, $ \left\{ f(y_n) \right\}$ 역시
$ \left\{ f(z_n) \right\}$의 부분열이므로 $ \lim_{n \to \infty}f(y_n) = \alpha$라는
것을 알 수 있다. 따라서 1이 성립. □
