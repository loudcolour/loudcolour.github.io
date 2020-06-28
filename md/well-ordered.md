<!---
title: "정렬집합"
category: Mathematics
language: Korean
--->

# 정렬집합

> **정의**. 순서집합 $(X, \leq)$에 대하여, $X$의 모든 공집합이 아닌 부분집합이 최소원소를 가질 때,
> $(X, \leq)$를 정렬집합(well-ordered set)이라고 한다.

- 정렬집합의 부분집합(과 그 부분집합에 대한 순서의 제한)에 의한 순서집합은 정렬집합이다.
- 정렬집합과 순서동형인 순서집합은 정렬집합이다.
- 임의의 원소가 2개인 정렬집합의 부분집합은 최소원소를 가지므로, 정렬집합은 전순서집합이다.
	* 유한집합인 전순서집합은 정렬집합이다.

> **정의**. $(X, \leq)$가 정렬집합이라고 하자. 이때 $a\in X$에 대하여,
> $X\langle a\rangle = \{x\in X\,|\,x\leq a, x\not=a\}$를 $a$에 대한 $X$의 절편이라고 한다.

> **명제**. $a,b\in X$일 때,
> $X \langle a \rangle \langle b \rangle = X \langle b \rangle$이다.

*증명*. 단순 확인으로 이가 성립하는 것을 알 수 있으므로 생략.

> **명제**. 정렬집합 $(X, \leq)$와 $(Y, \leq')$가 주어졌을 때,
> 순서동형사상 $f: X\to Y$가 존재한다면, $f(X \langle a \rangle) = Y \langle f(a) \rangle$
> 이다.

*증명*. 역시 단순 확인으로 이가 성립함을 알 수 있으므로 생략.

> **명제**. 정렬집합 $(X, \leq)$와 단사인 순서보존사상 $f:X\to X$가 주어졌을 때,
> 임의의 $x\in X$에 대하여 항상 $x\leq f(x)$ 가 성립한다.

*증명*. $a\leq b$인 동시에 $a\not=b$인 것을 $a<b$ 이라고 쓰자.
$A= \left\{ x\in X \,|\, f(x)<x \right\}$라고 두어, $A$가 공집합이라는 것을 보이면 된다.
$A$가 만약 공집합이 아니라면, $A$는 정렬집합 $X$의 부분집합이므로 최소원소를 갖는다.
이를 $a$라고 하자. 여기서 $A$의 조건에 의하여, $f(a) < a$가 성립하고, 동시에 $f$는
순서를 보존하는 단사사상이므로, $f(f(a)) < f(a)$가 성립함을 확인할 수 있다.
따라서 $f(a)\in A$임을 알 수 있으나, $f(a) < a$가 동시에 성립하고 있으므로, 이는
$a$가 $A$의 최소원소라는 것에 모순이다. 따라서 $A$는 공집합. □

> **따름정리**. 정렬집합 $X$와, 임의의 $a\in X$에 대하여 $X\not\simeq X \langle a \rangle$
> 또한, $a,b\in X$, $a\not=b$이면, $X \langle a \rangle\not\simeq X \langle b \rangle$

*증명*. 만약 $X\simeq X \langle a \rangle$가 성립한다고 가정하면, 전단사인
순서를 보존하는 사상 $f:X\to X \langle a \rangle$가 존재한다.  하지만,
$f(a)\in X \langle a \rangle$이고, $f(a) < a$이므로 이는 모순이다.  마찬가지로
$X\langle a \rangle\simeq X \langle b \rangle$가 성립하지 않는 것 또한 보여진다. □

> **명제**. 무한집합 $X$가 정렬집합일 필요충분조건은 $X$의 원소로부터 생성되는
> 강한 단소감소열이 존재하지 않는 것이다.

*증명*. 집합 $X$가 정렬집합이라고 하자. 만약 $X$의 원소로부터 생성되는 강한
단소감소열 $ \left\{ x_n \right\}$이 존재한다고 하면,
$A= \left\{ x_1, x_2, \ldots \right\} \subset X$라고 둘 때, $X$의 정렬성으로부터
$x_k = \min A$가 존재한다. 하지만 $x_{k+1} < x_k$인 $x_{k+1}\in A$가 존재하므로,
이는 모순. 따라서 강한 단소감소열을 갖지 않는다.

역으로, 강한 단소감소열을 갖지 않는다고 가정하자. 만약 $X$가 정렬집합이 아니라고
가정하면 최소 원소를 갖지 않는 $X$의 공집합이 아닌 부분집합$A$가 존재한다.
임의의 $a_1\in A$를 선택하면, $a_2 < a_1$인 $a_2\in A$가 존재할 것이고, $a_2$에 대해서도
$a_3 < a_2$인 $a_3\in A$가 존재한다. 이를 무한히 반복하면 강한 단소감소열 $ \left\{ a_n \right\}$을
얻으므로 이는 모순이다. 따라서 $X$는 정렬집합. □

## 정렬집합의 비교정리

> **정의**. $(X,\leq)$와 $(Y, \leq')$가 정렬집합이라고 하자. 이 때,
> 어떤 $b\in Y$가 존재하여 $X\simeq Y \langle b \rangle $라면, $\|X\| < \|Y\|$라고
> 쓰자. 또한 $\|X\|<\|Y\|$이거나 $X\simeq Y$일 때, $\|X\| \leq \|Y\|$라고 쓰도록 하자.

> **명제**. 정렬집합 $(X,\leq)$와 $(Y,\leq')$가 주어졌을 때,
> $\|X\|\leq\|Y\|$인 동시에 $\|Y\|\leq\|X\|$이면, $X \simeq Y$이다.

*증명*. 위의 조건에 따라 순서를 보존하는 단사 $f: X\to Y$과 $g: Y\to X$가
존재한다고 하자.  만약 $b\in Y$가 존재하여 $f(X)= Y \langle b \rangle$ 라고
가정하면, $f\circ g : Y\to Y$ 역시 순서를 보존하는 단사가 되고,
$(f\circ g)(b) \in Y \langle b \rangle$일 것이므로, $(f\circ g)(b) < b$이므로,
이는 모순이다. $g(Y) = X \langle a \rangle$를 만족하는 $a\in X$가 존재하는 경우도 마찬가지. □

> **따름정리**. 만약 $a<b$인 $a,b$가 정렬집합 $X$의 원소라면,
> $\|X \langle a \rangle\|<\|X \langle b \rangle\|<\|X\|$ 이다.

> **보조정리**. 정렬집합 $(X, \leq)$와 그 부분집합 $A \subset X$에 대하여 다음 조건은
> 모두 동치이다.
>
> 1. $a\in A$, $b\in X$에 대하여 $b<a \implies b\in A$
> 1. $A$는 $X$ 혹은 $X$의 절편과 같다.

*증명*. 2에서 1은 정의에 의하여 자명하다. 1에서 2를 유도하자.
만약 $A$가 1을 만족한다고 하면, $X\setminus A$은 정렬집합의 부분집합이므로
그 최소원소를 $a$라고 할 때,
$A=X \langle a \rangle$이 성립함을 알 수 있다. 만약 $X\setminus A = \emptyset$라고
하면 $A \subset X$이므로 $A = X$임 또한 알 수 있다. □

> **명제**. 정렬집합 $(X, \leq)$와 $(Y, \leq')$가 주어졌을 때,
> $X_1 \subset X$를 $X_1 = \left\{ a\in X \,|\, \exists b\in Y: X \langle a \rangle \simeq Y \langle b \rangle \right\}$로
> 두면, $X_1$은 $X$ 혹은 $X$의 절편이다.

*증명*. $a\in X_1$ 인 동시에 $c<a$ ($\iff c \in X \langle a \rangle $)라고 하자.
그렇다면 순서를 보존하는 동형사상 $f: X \langle a \rangle \to Y \langle b \rangle$에 의하여
$X \langle a \rangle \simeq Y \langle b \rangle$인 $b\in Y$가 존재할 것이다.
여기서, $f(c) = d$라고 두면, $X \langle c \rangle = X \langle a \rangle \langle c \rangle$에 의하여,

$$
f(X \langle c \rangle) = f( X \langle a \rangle \langle c \rangle)
= Y \langle b \rangle \langle f(c) \rangle = Y \langle d \rangle
$$

가 성립하는 것을 알 수 있다. 따라서 $X \langle c \rangle \simeq Y \langle d \rangle$가
성립하므로 $c\in X_1$, 이는 위의 보조정리에 의하여 $X_1$이 $X$ 혹은 $X$의 어느 절편과
일치함을 나타낸다. □

> **정리**(정렬집합의 비교정리). 두 정렬집합 $(X, \leq)$와 $(Y, \leq')$가 주어졌을 때,
> 항상 다음 조건 중 단 하나만이 성립한다.
>
> 1. $X\simeq Y$
> 1. $\exists b\in Y : X \simeq Y \langle b \rangle$
> 1. $\exists a\in X : X \langle a \rangle \simeq Y$

*증명*. 정렬집합 $X$와 $Y$에 대하여 $X\not\simeq Y$라면 $X$와 $Y$의 한 쪽이 다른
한쪽의 절편과 순서동형이라는 것을 보이면 된다.

집합 $X_1 := \left\{ a\in X \,|\, \exists b\in Y : X \langle a \rangle\simeq Y \langle b \rangle \right\} \subset X$와
$Y_1 := \left\{ b\in Y \,|\, \exists a\in X : X \langle a \rangle\simeq Y \langle b \rangle \right\}$
을 정의하자. 위의 명제에 의하여, $X_1$, $Y_1$은 $X$와 $Y$ 전체이거나 절편이다.
$b\not=b'$라면 $Y \langle b \rangle \not\simeq Y \langle{ b' \rangle}$
이므로, 각 $a\in X_1$에 대하여 $X \langle a \rangle\simeq Y \langle b \rangle$인
$b\in Y$는 unique하게 정하여진다. 또한 이 $a$에 대응하는 $b$에 대해서는 $b\in Y_1$이
성립함을 간단하게 알 수 있다.
이에 의하여 사상 $b = f(a)$를 정의하면 위의 설명에 의하여 well-defined인 사상
$f: X_1 \to Y_1$을 얻는다.

$c\in X_1$, $a\in X_1$, $c<a$일 때 $X \langle a \rangle$와 동형인 $Y \langle b \rangle$는
$X \langle c \rangle$와 동형인 $Y \langle d \rangle$을 부분집합으로 두는 것을
위에서 설명한 기본적인 명제를 통해 알 수 있다.
따라서 $f(c) = d$이고 $f(c) = d < b = f(a)$이므로,
$f$는 순서를 보존하는 사상이다. 동시에 $f$와 같은 방법으로
순서를 보존하는 사상 $g: Y_1\to X_1$을
정의할 수 있고, $g\circ f$와 $f\circ g$가 모두 항등사상이 되는 것을 통하여,
$f$와 $g$는 서로의 역사상이므로 $f$는 전단사라는 것을 알 수 있다.
따라서 $X_1 \simeq Y_1$이 성립한다.

만약, $p\in X$와 $q\in Y$가 존재하여
$X_1 = X \langle p \rangle$, $Y_1 = Y \langle q \rangle$라고 하면,
$X_1$과 $Y_1$의 정의상 $p\in X_1$, $q\in Y_1$이게 되므로,
이는 모순.

$X_1 = X$, $Y_1 = Y$라면 $X\simeq Y$이게 되므로, $X\not\simeq Y$인 경우에는
$X_1$과 $Y_1$의 한 쪽은 $X$나 $Y$의 전체, 다른 한 쪽은 남은 한 쪽의 절편이 되는
경우밖에 남지 않는다. □

## 정렬집합의 구성정리

> **정리**. 집합족 $ \left\{ W_\lambda \right\}_{\lambda\in\Lambda}$에 대하여 $W_\lambda\subset A$이고,
> 각 $W_\lambda$에는 순서 $\leq_{\lambda}$가 존재하여 $(W_\lambda, \leq_\lambda)$가 정렬집합을 이루고 있다고 하자.
> 동시에 $\lambda\neq\lambda'$일 때, $W_\lambda$와 $W_{\lambda'}$의 한쪽이 다른 한쪽의 절편과 일치한다면,
> 다음이 성립한다. (단, $W = \bigcup_{\lambda\in\Lambda}W_\lambda$이다.)
>
> - 임의의 $x,y\in W$에 대하여 $x,y\in W_\lambda$인 $\lambda\in\Lambda$가 존재한다.
> - 특히, $x,y\in W$에 대하여 $x\leq y \iff x\leq_\lambda y $로 순서 $\leq$를 정의하면
>   $(W,\leq)$는 정렬집합이 된다.
> - 각 $\lambda\in\Lambda$에 대하여 $(W_\lambda, \leq_\lambda)$는 $(W, \leq)$ 혹은 $(W,\leq)$의 절편과 일치한다.

## 정렬정리

> **정리**(정렬정리). [선택공리](./axiom-of-choice.html)를 가정하면, 임의의 집합 $A$에 대하여
> $(A,\leq)$가 정렬집합이 되도록 하는 적절한 $A$상의 순서 $\leq$가 존재한다.

