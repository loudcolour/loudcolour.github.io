<!---
title: 'Pell의 방정식'
category: Mathematics
language: Korean
--->

# Pell의 방정식

Pell의 방정식에 대해 기술하기에 앞서, $\Z[\sqrt{2}]^{\times}$에 대해 고찰하자.
$\Z[\sqrt{2}]^{\times}$란, $\Z[\sqrt{2}]=\left\{ a+b\sqrt{2}\,|\,a,\,b\in\Z \right\}$의
가역원 전체의 집합이다. $\Z[\sqrt{2}]^{\times}$는 $\R$의 부분환으로, 환에서는 $0$가 아닌 원소 중에서도
곱셈에 대한 역원이 존재하지 않는 원소가 존재한다.
예를 들어, $1+\sqrt{2}\in\Z[\sqrt{2}]$는 $\left( 1+\sqrt{2} \right)\left( 1-\sqrt{2} \right) = 1$
이므로 역원 $1-\sqrt{2}$가 $\Z[\sqrt{2}]$ 내에 존재하는 가역원이지만,
$3+\sqrt{2}\in\Z[\sqrt{2}]$의 경우, $\left( 3+\sqrt{2} \right)x=1$을 만족하는
$x\in\Z[\sqrt{2}]$가 존재하지 않으므로, 가역원이 아니다.

그렇다면, 이런 가역원 전체의 집합인 $\Z[\sqrt{2}]^{\times}$에 대하여
$a+b\sqrt{2}\in\Z[\sqrt{2}]$일 필요충분조건을 생각하자.
이를 위해서, $a+b\sqrt{2}$의 켤레를 $\overline{a+b\sqrt{2}}=a-b\sqrt{2}$로 정의하자.
(여기서 각 원소에 대한 켤레가 well-defined이기 위해서는 $\R$을 $\Z$에 대한 벡터공간으로 하여
$1$과 $\sqrt{2}$가 선형독립임을 보일 필요가 있으나, 여기서는 생략한다.)
또한, $a+b\sqrt{2}$에 대하여, $N\left(a+b\sqrt{2}\right) = (a+b\sqrt{2})\overline{(a+b\sqrt{2})}=a^2-2b^2$가 되도록 사상 $N$를 정의하자.

여기에서 정의한 사상 $N$에 대해, 다음 성질이 성립한다.
첫번째 성질과 두번째 성질 모두 $N$의 정의에 따라 간단히 확인할 수 있다.
($\overline{xy} = \overline{x}\cdot\overline{y}$이 성립하는 것을 이용하면 된다.)

- $x\in\Z[\sqrt{2}]$에 대해 $N(x)\in\Z$
- $x,y\in\Z[\sqrt{2}]$에 대해 $N(xy)=N(x)N(y)$

여기서 $x=a+b\sqrt{2}\in\Z[\sqrt{2}]^{\times}$ ($a,b\in\Z$) 라고 한다면, $xy=1$인 $y\in\Z[\sqrt{2}]$가 존재할 것이다.
따라서, $N(x)N(y)=N(xy)=N(1)=1$이다. $N(x), N(y)\in\Z$ 이므로, $N(x)=\pm 1$이라는 것을 알 수 있고,
이를 $a,b$에 대해서 나타내면 $a^2-2b^2=\pm1$이다. 따라서 $x\in\Z[\sqrt{2}]^{\times}$일 필요조건은
$a^2-2b^2=\pm1$이다. 역으로, $a^2-2b^2=\pm1$일 경우에는 $\left(a+b\sqrt{2}\right)\left(a-b\sqrt{2}\right)=\pm1$이 성립하므로,
$x=a+b\sqrt{2}\in\Z[\sqrt{2}]^{\times}$ 인 것을 알 수 있다. 그러므로 $a^2-2b^2=\pm1$이 $x=a+b\sqrt{2}\in\Z[\sqrt{2}]^{\times}$일
필요충분조건이라는 것을 알 수 있다. 집합으로는 $\Z[\sqrt{2}]^{\times}=\left\{ a+b\sqrt{2}\,|\,a,b\in\Z, a^2-2b^2=\pm1 \right\}$와
같이 쓸 수도 있다.

필요충분조건을 사용하여 집합을 나타내는 것에는 성공했지만, $\Z[\sqrt{2}]^{\times}$의 원소들을 외연적 방법으로 나타내려 한다면,
$a^2-2b^2=\pm1$라는 방정식의 정수해를 찾아내어야 한다. 이 방정식이 바로 이 문서에서 다룰 Pell의 방정식이다.

## Pell의 방정식이란

Pell의 방정식은 두 정수 $x,y\in\Z$에 대하여 $x^2-Dy^2 = \pm 1$과 같이 주어진다.
(단, $D$는 자연수의 제곱꼴로 나타내어지지 않는 2 이상의 자연수)

> **명제**. Pell의 방정식의 자연수해 중 $x$가 최소인 것을 $(x,y) = (x_1,y_1)$이라고 두면,
> $X+Y\sqrt{D} = \pm\left(x_1+y_1\sqrt{D}\right)^n$ ($n,X,Y\in\Z$)로 얻어지는 $(X, Y)$또한 Pell의 방정식의 해이다.
