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
