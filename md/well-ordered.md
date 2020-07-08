<!---
title: "정렬집합"
category: Set Theory
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
> - 각 $\lambda\in\Lambda$에 대하여
>   $(W_\lambda, \leq_\lambda)$는 $(W, \leq)$ 혹은 $(W,\leq)$의 절편과 일치한다.

*증명*. $x,y\in W$에 대하여, $x\in W_{\lambda_1}$, $y\in W_{\lambda_2}$
가 성립하고 있다고 하자.
가정으로부터 $W_{\lambda_1} \subset W_{\lambda_2}$ 혹은
$W_{\lambda_1} \supset W_{\lambda_2}$
이 성립한다. 따라서 $x,y\in W_\lambda$인 $\lambda\in\Lambda$가 존재한다.
또한, $x,y\in W_\lambda$인 동시에 $x,y\in W_\mu$가 성립한다면,
한쪽이 다른 한쪽의 절편에 일치하므로 $x\leq_\lambda y \iff x\leq_\mu y$가 성립하여,
순서 $\leq$를 위와 같이 잘 정의할 수 있다.
순서 $\leq$는 모든 $x,y\in W$에 대하여 비교가능이므로 전순서이다.

다음으로, $(W, \leq)$가 정렬집합이라는 것을 보이자.
$M\neq\emptyset$을 $W$의 부분집합이라고 하여, $\min W$가 존재하는 것을 보이면 된다.
$M\neq\emptyset$이므로, $M\cap W_\lambda \neq\emptyset$인 $\lambda\in\Lambda$가
존재한다. 이 때, $(W_\lambda,\leq_\lambda)$가 정렬집합이라는 사실으로부터,
그 부분집합인 $M\cap W_\lambda$의 최소원소 $a:=\min M\cap W_\lambda$가 존재한다.
여기서 $a = \min M$인 것을 보이자. $x\in M$에 대하여,

- $x\in W_\lambda$인 경우: $x\in M\cap W_\lambda$이므로, 정의에 따라 $a\leq_\lambda x$,
$a\leq x$
- $x\notin W_\lambda$인 경우: $x\in W_{\lambda'}$인 $\lambda'\in\Lambda$가 존재한다.
이 때, $\lambda\neq\lambda'$, $W_{\lambda'}\not\subset W_\lambda$이 성립하므로,
$W_\lambda$가 $W_{\lambda'}$의 절편이라는 사실을 알 수 있다.
따라서 $a\in W_\lambda$, $x\in W_{\lambda'}\setminus W_\lambda$이므로,
$a\leq_{\lambda'} x$, $a\leq x$.

따라서 $M$에는 최소원소가 존재하므로, $(W,\leq)$는 정렬집합이다.

마지막으로, 임의의 $(W_\lambda, \leq_\lambda)$는 $(W, \leq)$이거나 $(W, \leq)$의 절편과
일치함을 보이자.
만약, 모든 $W_\lambda$에 대하여 $W_\lambda\subset W_\mu$이 성립한다면,
$W_\mu = W$, $(W_\mu, \leq_\mu) = (W, \leq)$는 분명하다.
그렇지 않은 경우,
$W_\mu \subsetneq W$일 것이고, $(W_\mu, \leq_\mu)$는 $(W, \leq)$의 부분순서집합이 될 것이다.
여기서, $(W_\mu, \leq_\mu)$가 $(W, \leq)$의 절편이라는 것을 보이기 위해서는,
$\forall x\in W_\mu, \forall y\in W \left[ x>y \implies y\in W_\mu \right]$를
보이면 된다.
$x,y\in W_{\mu'}$가 성립한다고 하자. 그렇다면, $\mu = \mu'$, 혹은 $(W_{\mu}, \leq_{\mu})$가
$(W_{\mu'}, \leq_{\mu'})$의 절편, 혹은 $(W_{\mu'}, \leq_{\mu'})$가
$(W_{\mu}, \leq_{\mu})$의 절편일 것이다.

- $\mu = \mu'$ 혹은 $(W_{\mu'}, \leq_{\mu'})$가 $(W_{\mu}, \leq_{\mu})$의 절편:
$y\in W_{\mu'}$이므로, $y\in W_{\mu}$가 성립한다.
- $(W_{\mu}, \leq_{\mu})$가 $(W_{\mu'}, \leq_{\mu'})$의 절편:
$x\in W_{\mu}, y\in W_{\mu'}$이고, $W_{\mu}$는 $W_{\mu'}$의 절편이므로,
$y>_{\mu'}x\implies y\in W_{\mu}$가 성립. 따라서 $y>x$이면, $y\in W_{\mu}$. □

## 정렬정리

> **정리**(정렬정리(WOP)).
> [선택공리](./axiom-of-choice.html)를 가정하면, 임의의 집합 $A$에 대하여
> $(A,\leq)$가 정렬집합이 되도록 하는 적절한 $A$상의 순서 $\leq$가 존재한다.

*증명*. 어떤 집합 $A$에 대하여, $A$의 부분집합인 동시에 정렬집합인 집합의 집합을 
$\mathscr{A}$로 두자. 이 때, $\mathscr{A}\neq\emptyset$이다.
두 정렬집합 $(W,\leq), (W', \leq')\in\mathscr{A}$에 대하여,
$(W, \leq) = (W', \leq')$이거나 $(W,\leq)$가 $(W',\leq')$의 절편일 때,
이항관계 $(W, \leq) \rho (W', \leq')$가 성립한다고하자.
여기서 $\rho$가 순서관계라는 사실은 간단하게 확인할 수 있다.

실제로, $(\mathscr{A}, \rho)$는 귀납적인 순서집합이다.
$(\mathscr{A}, \rho)$상의 임의의 사슬 $K$에 대하여 $\bigcup K$는
정렬집합의 구성정리에 의하여 새로운 정렬집합을 이루고,
$\bigcup K$가 $K$의 상한이 됨을 알 수 있다.
[Zorn의 보조정리](./zorns-lemma.html)을 적용하면, $\mathscr{A}$는 극대원소를 가지므로,
이를 $(W^*, \leq^*)$로 두자.

여기서 $A = W^*$임을 보이면, $\leq^*$가 $A$의 정렬순서가 됨을 알 수 있다.
이를 보이기 위하여 $A\neq W^*$를 가정하자.
그렇다면, $A\setminus W^* \neq\emptyset$이므로, 적당한 $a\in A\setminus W^*$가 존재하여,
$W^{**} := W^* \cup \left\{ a \right\}$로 두고, 어떠한 $x\in W^*$에 대해서도
$x\leq^{**} a$가 성립하도록 $\leq^*$를 확장하여 $\leq^{**}$를 정의하면,
$(W^{**}, \leq^{**})\in \mathscr{A}$인 동시에 $(W^*, \leq^*)\rho(W^{**}, \leq^{**})$,
$(W^*, \leq^*)\neq(W^{**}, \leq^{**})$ 가 성립하므로 이는 $(W^*, \leq^*)$가
극대원소라는 것에 모순이다. 따라서 $A = W^*$이고 $A$에는 정렬순서가 존재한다. □

> **따름정리**(기수 비교의 trichotomy). 임의의 두 집합의 농도를 비교할 수 있다.

*증명*. 집합 $A, B$를 가정하자. 여기서 $|A| < |B|$, $|A| = |B|$, $|A| > |B|$가
동시에 성립하지 않는 것은 분명하다.
정렬정리에 의하여 $A$와 $B$에 각각 정렬순서 $\leq_A$와 $\leq_B$를 부여하면,
정렬집합의 비교정리에 의하여 $A$에서 $B$로의 단사와 $B$에서 $A$로의 단사 중
적어도 하나가 존재하는 것을 알 수 있다. □

*주*. 임의의 두 집합의 농도를 비교할 수 있다면, 이로부터 WOP를 유도할 수 있다.
즉, WOP와 기수 비교의 trichotomy는 $\textsf{ZF}$상에서 동치이다.
또한, 선택공리와 WOP가 동치인 것이 아래의 명제로부터 보여지므로,
선택공리와 기수 비교의 trichotomy도 동치이다.

> **명제**(선택공리의 유도). 정렬정리로부터 선택공리가 유도된다.

*증명*.
각 $\lambda\in\Lambda$에 대하여 $A_\lambda\neq\emptyset$인
집합족 $ \left\{ A_\lambda \right\}_{\lambda\in\Lambda}$가 주어졌다고 하자.
이 때, $A := \bigcup_{\lambda\in\Lambda} A_\lambda$ 라고 두면,
정렬정리에 의하여 $A$에 정렬순서를 부여할 수 있다. 이를 $(A,\leq)$라고 하면,
각 $A_\lambda$는 $A$의 공집합이 아닌 부분집합이므로, $\min_{\leq} A_\lambda$가 존재한다.
따라서, 사상
$s: \Lambda\to \bigcup_{\lambda\in\Lambda} A_\lambda, \lambda\mapsto \min_{\leq}A_\lambda$
을 구성하면, 임의의 $\lambda\in\Lambda$에 대하여
$s(\lambda)\in A_{\lambda}$가 성립하므로, 이는 선택사상이고,
선택공리가 성립하는 것을 알 수 있다. □

> **명제**. 선택공리와 기수 비교의 trichotomy는 동치이다.

*증명*. 선택공리(WOP)로부터 기수 비교의 trichotomy가 유도되는 것은 위의 따름정리에서
보였다.

역으로, 기수 비교의 trichotomy가 성립한다면, WOP가 유도되는 것을 보이자.
$X$를 임의의 집합으로 두자. $\mathscr{P}(\mathscr{P}(X))$의 원소는 모두
$\mathscr{P}(X)$의 부분집합이므로, $\subset$에 의하여 반순서집합을 이룬다.
개중에는 정렬집합을 이루는 것이 존재할 것이며, 해당하는 [순서수](./ordinal.html)가 존재함을
순서수의 정의로부터 알 수 있다.
따라서, $\mathscr{P}(\mathscr{P}(X))$의 정렬집합인 원소가 갖는 순서수 전체의
집합을 $E$로 두자. 그렇다면, $E$ 또한 정렬집합이다.
$\lambda\in E$이고 $\mu < \lambda$이면 $\mu\in E$인 것을 순서수의 정의로부터
알 수 있으므로, $\nu'<\nu$인 순서수 $\nu'$전체의 집합을 $S_{\nu}$라고 할때,
$E = S_{\nu}$인 $\nu$가 존재한다.
$\|E\| = \|S_{\nu}\| = \nu$이므로, $E = S_{\|E\|}$이고,
모든 $\lambda\in E$에 대하여 $\lambda<\|E\|$가 성립한다.

여기서, $|E|\not\leq |X|$이다.
만약, $|E|\leq|X|$, 단사 $f: E\to X$가 존재한다고 가정하면,
$f$의 단사성에 의해 $E$와 $f(E)$ 상의 순서동형을 유도하여,
정렬집합 $(f(E), \prec)$를 얻는다.
$f(E)\in \mathscr{P}(X)$의 ($\prec$에 의한) 절편 전체로 이루어진
$A \in\mathscr{P}(\mathscr{P}(X))$는 $\subset$을 순서로 하여 $f(E)$와 순서동형,
즉 $E$와 순서동형이다. $A$는 정렬집합이므로, $\|E\| = \|A\| \in E$.
따라서, $\|E\| < \|E\|$, 이는 모순이다.

기수 비교의 trichotomy를 적용하면, $|E|>|X|$이다. 단사 사상 $g: X\to E$로 부터,
$X$에 정렬순서를 부여할 수 있다. 따라서 WOP가 보여진다. □

