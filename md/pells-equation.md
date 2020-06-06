<!---
title: 'Pell의 방정식'
category: Mathematics
language: Korean
--->

# Pell의 방정식

Pell의 방정식에 대해 기술하기에 앞서, $\Z\left[\sqrt{2}\right]^{\times}$에 대해 고찰하자.
$\Z\left[\sqrt{2}\right]^{\times}$란, $\Z\left[\sqrt{2}\right]=\left\{ a+b\sqrt{2}\,|\,a,\,b\in\Z \right\}$의
가역원 전체의 집합이다. $\Z\left[\sqrt{2}\right]^{\times}$는 $\R$의 부분환으로, 환에서는 $0$가 아닌 원소 중에서도
곱셈에 대한 역원이 존재하지 않는 원소가 존재한다.
예를 들어, $1+\sqrt{2}\in\Z\left[\sqrt{2}\right]$는 $\left( 1+\sqrt{2} \right)\left( 1-\sqrt{2} \right) = 1$
이므로 역원 $1-\sqrt{2}$가 $\Z\left[\sqrt{2}\right]$ 내에 존재하는 가역원이지만,
$3+\sqrt{2}\in\Z\left[\sqrt{2}\right]$의 경우, $\left( 3+\sqrt{2} \right)x=1$을 만족하는
$x\in\Z\left[\sqrt{2}\right]$가 존재하지 않으므로, 가역원이 아니다.

그렇다면, 이런 가역원 전체의 집합인 $\Z\left[\sqrt{2}\right]^{\times}$에 대하여
$a+b\sqrt{2}\in\Z\left[\sqrt{2}\right]^{\times}$일 필요충분조건을 생각하자.
이를 위해서, $a+b\sqrt{2}$의 켤레를 $\overline{a+b\sqrt{2}}=a-b\sqrt{2}$로 정의하자.
(여기서 각 원소에 대한 켤레가 well-defined이기 위해서는 $\R$을 $\Z$에 대한 벡터 공간으로 하여
$1$과 $\sqrt{2}$가 선형독립임을 보일 필요가 있으나, 여기서는 생략한다.)
또한, $a+b\sqrt{2}$에 대하여, $N\left(a+b\sqrt{2}\right) = \left(a+b\sqrt{2}\right)\overline{\left(a+b\sqrt{2}\right)}=a^2-2b^2$가 되도록 사상 $N$를 정의하자.

여기에서 정의한 사상 $N$에 대해, 다음 성질이 성립한다.
이는 모두 $N$의 정의에 따라 간단히 확인할 수 있다.
($\overline{xy} = \overline{x}\cdot\overline{y}$,
$\overline{x+y} = \overline{x}+\overline{y}$이 성립하는 것을 이용하면 된다.)

- $x\in\Z\left[\sqrt{2}\right]$에 대해 $N(x)\in\Z$
- $x\in\Z\left[\sqrt{2}\right]$에 대해 $N(x)=N(\overline{x})$, $N(-x)=N(x)$
- $x,y\in\Z\left[\sqrt{2}\right]$에 대해 $N(xy)=N(x)N(y)$

여기서 $x=a+b\sqrt{2}\in\Z\left[\sqrt{2}\right]^{\times}$ ($a,b\in\Z$) 라고 한다면, $xy=1$인 $y\in\Z\left[\sqrt{2}\right]$가 존재할 것이다.
따라서, $N(x)N(y)=N(xy)=N(1)=1$이다. $N(x), N(y)\in\Z$ 이므로, $N(x)=\pm 1$이라는 것을 알 수 있고,
이를 $a,b$에 대해서 나타내면 $a^2-2b^2=\pm1$이다. 따라서 $x\in\Z\left[\sqrt{2}\right]^{\times}$일 필요조건은
$a^2-2b^2=\pm1$이다. 역으로, $a^2-2b^2=\pm1$일 경우에는 $\left(a+b\sqrt{2}\right)\left(a-b\sqrt{2}\right)=\pm1$이 성립하므로,
$x=a+b\sqrt{2}\in\Z\left[\sqrt{2}\right]^{\times}$ 인 것을 알 수 있다.
($a+b\sqrt{2}$의 역원은 $a-b\sqrt{2}$ 혹은 $-a+b\sqrt{2}$) 그러므로 $a^2-2b^2=\pm1$은 $x=a+b\sqrt{2}\in\Z\left[\sqrt{2}\right]^{\times}$의
필요충분조건이라는 것을 알 수 있다.
이를 $\Z\left[\sqrt{2}\right]^{\times}=\left\{ a+b\sqrt{2}\,|\,a,b\in\Z, a^2-2b^2=\pm1 \right\}$과
같이 집합의 형태로 쓸 수도 있다.

필요충분조건을 사용하여 집합을 나타내는 것에는 성공했지만,
$\Z\left[\sqrt{2}\right]^{\times}$의 원소들을 외연적 방법으로 나타내려 한다면,
$a^2-2b^2=\pm1$ 이라는 방정식의 정수해를 찾아내는 방법이 요구된다.
여기서 다루게 될 방정식이 바로 Pell의 방정식이다.

## Pell의 방정식이란

### 일반적인 Pell의 방정식

일반적인 Pell의 방정식은 두 정수 $x,y\in\Z$
와, 자연수의 제곱꼴로 나타내어지지 않는 2 이상의 자연수
$D$에 대하여 $x^2-Dy^2 = 1$과 같이 주어진다. ($\pm 1$이 아님에 주의.)

> **명제**. Pell의 방정식의 $x,y\geq 1$인 해 중에서 $x$가 최소인 것을 $(x,y) = (x_1,y_1)$이라고 두면,
> $x_n+y_n\sqrt{D} = \pm\left(x_1+y_1\sqrt{D}\right)^n$ ($n,x_n,y_n\in\Z$)으로 얻어지는 $(x_n, y_n)$또한 Pell의 방정식의 해이다.

*증명*. $x+y\sqrt{D}\in\Z\left[\sqrt{D}\right]^{\times}$ ($x,y\in\Z$) 에 대하여,
$\overline{x+y\sqrt{D}} = x-y\sqrt{D}$로 두고,
위에서 $N$을 정의한 것처럼 사상
$N_D\left(x+y\sqrt{D}\right) = \left(x+y\sqrt{D}\right)\overline{\left(x+y\sqrt{D}\right)}=\left(x+y\sqrt{D}\right)\left(x-y\sqrt{D}\right)=x^2-Dy^2$
을 정의하자. $N$과 같이,

- $x\in\Z\left[\sqrt{D}\right]$에 대해 $N_D(x)\in\Z$
- $x\in\Z\left[\sqrt{D}\right]$에 대해 $N_D(x)=N_D(\overline{x})$, $N_D(-x)=N_D(x)$
- $x,y\in\Z\left[\sqrt{D}\right]$에 대해 $N_D(xy)=N_D(x)N_D(y)$

과 같은 성질이 $N_D$에 대해 성립한다.
여기서 Pell의 방정식을 $N_D$를 이용하여 표현하면, $N_D\left(x+y\sqrt{D}\right)=1$이다.
이 때, $N_D\left(x_1+y_1\sqrt{D}\right)=1$가 성립하는 것이 알려져 있으므로,
$N_D\left(x_n+y_n\sqrt{D}\right) = N_D\left(\pm\left(x_1+y_1\sqrt{D}\right)^n\right) = \left\{N_D\left(x_1+y_1\sqrt{D}\right)\right\}^n = 1^n = 1$ 이다. 따라서, $(x_n,y_n)$ 또한
Pell의 방정식의 해라는 것을 알 수 있다. □

> **보조정리**. $a,b,c,d\in\N^+$에 대해 $a+b\sqrt{D}<c+d\sqrt{D}$이고, $a^2-Db^2 = c^2-Dd^2 = 1$이면,
> $\frac{c+d\sqrt{D}}{a+b\sqrt{D}}\in\left\{x+y\sqrt{D}\,|\,x,y\in\N^+\right\}$이다.

*증명*. 분모의 유리화에 의해,

$$
\begin{aligned}
\frac{c+d\sqrt{D}}{a+b\sqrt{D}}
&= \frac{\left(c+d\sqrt{D}\right)\left(a-b\sqrt{D}\right)}{a^2-Db^2} \\
&= \left(c+d\sqrt{D}\right)\left(a-b\sqrt{D}\right) \\
&= \left(ac-Dbd\right)+\left(ad-bc\right)\sqrt{D}
\end{aligned}
$$

와 같이 나타낼 수 있다. 여기서 $ac-Dbd, ad-bc\in\Z$ 이므로, $ac-Dbd, ad-bc > 0$ 임을 보이면 된다.
먼저 $ac-Dbd>0$임을 보이자. 이를 위해 $ac-Dbd \leq 0$ 라고 가정하면, $ad+bc > 0$이므로,

$$
\begin{aligned}
\left(ac-Dbd\right)\left(ad+bc\right) &\leq 0 \\
a^2cd+abc^2-Dabd^2-Db^2cd &\leq 0 \\
cd+ab = cd\left(a^2-Db^2\right) + ab\left(c^2-Dd^2\right) &\leq 0
\end{aligned}
$$

이나, $a,b,c,d\in\N^+$에 모순되므로, $ac-Dbd>0$임을 알 수 있다.

다음으로 $ad-bc>0$을 보이자. $ac-Dbd>0$ 임을 보였으므로,
$\left(a^2-Db^2\right)+\left(c^2-Dd^2\right) = 2 > 2(Dbd-ac)$ 가 성립한다. 따라서,

$$
\begin{aligned}
\left(a^2-Db^2\right)+\left(c^2-Dd^2\right) &> 2(Dbd-ac) \\
a^2+2ac+c^2 &>D\left(b^2+2bd+d^2\right) \\
\left(a+c\right)^2 &> D\left(b+d\right)^2\\
a+c &> \sqrt{D}\left(b+d\right) \\
a-d\sqrt{D} &> -c+b\sqrt{D} \\
\end{aligned}
$$

이 성립하는 동시에, $a-d\sqrt{D} < c-b\sqrt{D}$ 가 성립하므로,
$\left|a-d\sqrt{D}\right| < \left|c-b\sqrt{D}\right|$,
$\left(a-d\sqrt{D}\right)^2 < \left(c-b\sqrt{D}\right)^2$이 성립한다.
이를 다시 전개하면,

$$
\begin{aligned}
\left(a-d\sqrt{D}\right)^2 &< \left(c-b\sqrt{D}\right)^2 \\
a^2 + Dd^2 - 2ad\sqrt{D} &< c^2 + Db^2 - 2bc\sqrt{D}  \\
\left(a^2 - Db^2\right) - \left(c^2 - Dd^2\right) &< 2\sqrt{D}\left(ad-bc\right) \\
0 &< ad-bc
\end{aligned}
$$

를 보일 수 있다. □

> **명제**. $\left\{x+y\sqrt{D}\,|\,x,y\in\Z,\,x^2-Dy^2=1\right\}=\left\{\pm\left(x_1+y_1\sqrt{D}\right)^n\,|\,n\in\Z\right\}$ 이다. 즉, 위의 명제를 통해 구하여지는 해가 곧 Pell의 방정식의 모든 해이다.

*증명*. $A = \left\{x+y\sqrt{D}\,|\,x,y\in\Z,\,x^2-Dy^2=1\right\}$,
$B=\left\{\pm\left(x_1+y_1\sqrt{D}\right)^n\,|\,n\in\Z\right\}$ 라고 두면, $B\subset A$ 인 것은 위의 명제에서
이미 보였다. 따라서, $A\subset B$임을 보이기만 하면 된다.

여기서, $A^+ = \left\{x+y\sqrt{D}\,|\,x,y\in\N^+,\,x^2-Dy^2=1\right\}$,
$B^+=\left\{\left(x_1+y_1\sqrt{D}\right)^n\,|\,n\in\N^+\right\}$ 으로 두자.
그렇다면, $x_1+y_1\sqrt{D}$는 $A^+$의 최소 원소가 될 것이다.
($\because$ 임의의 $x+y\sqrt{D}\in A^+$에 대해 $x\geq x_1$ 이므로,
$Dy^2+1 = x^2 \geq {x_1}^2 = D{y_1}^2 +1$, 따라서 $y \geq {y_1}$,
$x+y\sqrt{D}\geq x_1+y_1\sqrt{D}$)
만약, $A^+\subset B^+$이라고 하면, 임의의 $x+y\sqrt{D}\in A^+$에 대해 적절한 $n\in\N^+$가
존재하여 $x+y\sqrt{D}=\left(x_1+y_1\sqrt{D}\right)^n\in B^+$ 일 것이고,

- $\overline{x+y\sqrt{D}} = \overline{\left(x_1+y_1\sqrt{D}\right)^n} = \left(x_1-y_1\sqrt{D}\right)^n = \left(x_1+y_1\sqrt{D}\right)^{-n}\in B$
- $-\left(x+y\sqrt{D}\right) = -\left(x_1+y_1\sqrt{D}\right)^n \in B$
- $-\left(\overline{x+y\sqrt{D}}\right) = -\left(x_1+y_1\sqrt{D}\right)^{-n} \in B$
- $\pm1 = \pm\left(x_1+y_1\sqrt{D}\right)^0\in B$

이 성립하므로,

$$
A=\left(A^+\cup\left\{-x\,|\,x\in A^+\right\}\cup\left\{\overline{x}\,|\,x\in A^+\right\}\cup\left\{-\overline{x}\,|\,x\in A^+\right\}\cup\left\{1,-1\right\}\right)\subset B
$$

가 성립하게 된다. 따라서 $A\subset B$임을 보이기 위해서는,
$A^+\subset B^+$을 보이는 것으로 충분하다.
이를 보이기 위해 $p\in A^+$를 만족하는 동시에 $p\not\in B^+$를 만족하는 $p=x'+y'\sqrt{D}$가
존재한다고 가정하자. ($x',y'\in\N^+$) 그렇다면 적절한 $k\in\N^+$가 존재하여

$$
\left(x_1+y_1\sqrt{D}\right)^k < x'+y'\sqrt{D} < \left(x_1+y_1\sqrt{D}\right)^{k+1}
$$

일 것이다. $\left(x_1+y_1\sqrt{D}\right)^k > 0$ 이므로,
각 변을 $\left(x_1+y_1\sqrt{D}\right)^k$으로 나누면,

$$
1 < \frac{x'+y'\sqrt{D}}{\left(x_1+y_1\sqrt{D}\right)^k} < \left(x_1+y_1\sqrt{D}\right)
$$

이고,

$$
\frac{x'+y'\sqrt{D}}{\left(x_1+y_1\sqrt{D}\right)^k}
= \frac{\left(x'+y'\sqrt{D}\right)\overline{\left(x_1+y_1\sqrt{D}\right)^k}}
{\left(x_1+y_1\sqrt{D}\right)^k\overline{\left(x_1+y_1\sqrt{D}\right)^k}}
= \left(x'+y'\sqrt{D}\right)\overline{\left(x_1+y_1\sqrt{D}\right)^k}
= x''+y''\sqrt{D}
$$

으로 나타낼 수 있다. 단, $x'', y''\in\Z$ 이다.
여기서, 위의 보조정리에 따라 $x'+y'\sqrt{D}>\left(x_1+y_1\sqrt{D}\right)^k$이 성립하므로,
$x'', y''\in\N^+$이고,

$$
\begin{aligned}
x''^2-Dy''^2
&= N_D\left(x''+y''\sqrt{D}\right) \\
&= N_D\left(x'+y'\sqrt{D}\right)N_D\left(\overline{\left(x_1+y_1\sqrt{D}\right)^k}\right) \\
&= N_D\left(x'+y'\sqrt{D}\right)N_D\left(x_1+y_1\sqrt{D}\right)^k \\
&= 1\cdot1^k = 1
\end{aligned}
$$

이므로, $x''+y''\sqrt{D}\in A^+$임을
알 수 있다. 그러나, $x''+y''\sqrt{D}<x_1+y_1\sqrt{D}$이 성립하므로,
이는 $x_1+y_1\sqrt{D}$가 $A^+$의 최소 원소라는 전제에 모순된다. 따라서 $A^+\subset B^+$,
$A\subset B$ □

### 확장된 Pell의 방정식

이 글의 처음에서 다룬 문제에 등장한 방정식은
일반적인 Pell의 방정식의 해를 포함하는 방정식
$x^2-Dy^2 = \pm 1$으로, 이 방정식의 해를 구하기 위해서는
기존의 일반적인 Pell의 방정식의 해와 동시에 $x^2-Dy^2=-1$의 해를 구하여야 한다.
이 방정식의 해는 위에서 보인 일반적인 Pell의 방정식의 해를
구하는 것과 같은 방법으로 구할 수 있고 (충분성과 필요성 모두),
실제로 방정식의 해 전체는

$$
\left\{x+y\sqrt{D}\,|\,x,y\in\Z,\,x^2-Dy^2=\pm1\right\}=\left\{\pm\left(x_1+y_1\sqrt{D}\right)^n\,|\,n\in\Z\right\}
$$

와 같이 나타난다. 단, $(x_1, y_1)$는 방정식 $x^2-Dy^2=\pm1$의 $x$와 $y$가
동시에 자연수인 해 중에서 $x$가 최소인 해이다. 결론적으로,
$\Z\left[\sqrt{D}\right]^{\times}=\left\{\pm\left(x_1+y_1\sqrt{D}\right)^n\,|\,n\in\Z\right\}$
와 같이 쓸 수 있으며, 구체적으로는
$x^2-2y^2=\pm1$을 만족하는 $x$가 최소인 자연수해가 $(x,y)=(1,1)$이므로,
$\Z\left[\sqrt{2}\right]^\times = \left\{\pm\left(1+\sqrt{2}\right)^n\,|\,n\in\Z\right\}$로 나타내어짐을 알 수 있다.

## 해의 일반화

### 연분수를 이용하여 최소해 구하기

$x,y$에 관한 방정식의 해 중에서, $x$가 최소인 자연수해를 단순히 최소해로
부르기로 하자.

자연수의 제곱으로 나타내어지지 않는 자연수 $D$에 대하여,
$\sqrt{D}$를 연분수 표기로 나타내면 $[a_0;(a_1, a_2, \ldots, a_k)]$와
같이 나타내어지는 것이 알려져 있다. (괄호 안의 부분은 반복되는 부분이다.)
이 성질을 이용한 다음 정리가 성립하는 것이 알려져 있다.

> **정리**. $\sqrt{D} = [a_0;(a_1, a_2, \ldots, a_k)]$라고 하자.
> 점화식으로 두 수열 $X_n$, $Y_n$을 다음과 같이 정의할 때,
> - $X_0 = 1$, $X_1 = a_0$, $X_{n+1} = X_{n-1}+a_{n}X_{n}$
> - $Y_0 = 0$, $Y_1 = 1$,  $Y_{n+1} = Y_{n-1}+a_{n}Y_{n}$
>
> 다음이 성립한다.
> 1. $k$가 홀수일 때, $(X_k, Y_k)$는 $x^2-Dy^2=-1$의 최소해이다. 또한,
> $(X_{2k}, Y_{2k})$는 $x^2-Dy^2=1$의 최소해이다.
> 1. $k$가 짝수일 때, $(X_k, Y_k)$는 $x^2-Dy^2=1$의 최소해이다.
> 또한, $x^2-Dy^2=-1$의 해는 존재하지 않는다.

자세한 증명은 생략한다. 실제로 이 정리를 이용하면, 단순히 대입하는 것만으로는
해를 찾기 어려운 확장된 Pell의 방정식의 최소해를 쉽게 구할 수 있다.
예를 들어, $\sqrt{13} = [3;(1,1,1,1,6)]$이므로,
$(X_5, Y_5)=(18,5)$로 $x^2-13y^2=-1$을 만족하는 최소해는 $(18,5)$임을
알 수 있다.

### 해의 일반항 구하기

Pell의 방정식 $x^2-Dy^2 = \pm1$이 주어졌을 때, 해의 전체가
$\left\{\pm\left(x_1+y_1\sqrt{D}\right)^n\,|\,n\in\Z\right\}$와
같이 나타내어졌으므로, $x_n+y_n\sqrt{D} = \left(x_1+y_1\sqrt{D}\right)^n$ 
에 의하여 정해지는 자연수열 $x_n$과 $y_n$은 점화식에 의해 나타낼 수 있다.
초항은 정의 그대로 $(x_1,y_1)$일 것이고,

$$
\begin{aligned}
x_{k+1} + y_{k+1}\sqrt{D} &= \left(x_1+y_1\sqrt{D}\right)^{k+1} \\
&= \left(x_1+y_1\sqrt{D}\right)\left(x_1+y_1\sqrt{D}\right)^k \\
&= \left(x_1+y_1\sqrt{D}\right)\left(x_k+y_k\sqrt{D}\right) \\
&= x_1x_k + y_1y_kD + \left(x_1y_k + x_ky_1\right)\sqrt{D}
\end{aligned}
$$

임을 알 수 있다. 이를 통해 얻어진 선형점화식을 행렬의 형태로 쓰면,

$$
\begin{bmatrix}x_{k+1} \\ y_{k+1}\end{bmatrix}
= \begin{bmatrix}x_{1} & y_1D \\ y_{1} & x_1\end{bmatrix}
\begin{bmatrix}x_{k} \\ y_{k}\end{bmatrix}
$$

로 나타낼 수 있으므로, 일반항은

$$
\begin{bmatrix}x_{n} \\ y_{n}\end{bmatrix}
= \begin{bmatrix}x_{1} & y_1D \\ y_{1} & x_1\end{bmatrix}^{n-1}
\begin{bmatrix}x_{1} \\ y_{1}\end{bmatrix}
$$

로 나타내어진다. 적절히 행렬의 대각화를 이용하면 $x_n$과 $y_n$ 각각에 대한
일반항을 얻는 것도 가능하다.
