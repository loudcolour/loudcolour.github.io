<!---
title: "공리적 집합론: ZFC 공리계"
category: Mathematics
language: Korean
--->

# 공리적 집합론: ZFC 공리계

## Russell의 역설

집합을 "특정한 조건을 만족하는 원소의 모임"으로 정의하였을 때의 문제점을 생각하자.
어떠한 조건이든지 집합을 만드는 것이 가능하므로 가령 $A = \left\{ x \,|\, x\notin x \right\}$와
같은 집합을 정의할 수 있다. 실제로 $A$ 에 속하는 원소가 존재하는지 알 수는 없지만,
만약 $A\in A$라고 가정하면 $A\notin A$이고, $A\notin A$라고 가정하면 $A\in A$이다.
즉 $A\in A \iff A\notin A$이므로, 이는 논리 체계에 있어서 모순이다. (Russell의 역설)

이 모순의 근원은 어느 대상을 "집합"으로 정의하는 가에 있어서, 어떠한 조건이든지 그에 해당하는
집합을 만들 수 있다고 가정한 것이다. (즉, 그에 따라 "지나치게 거대한" 대상마저
집합으로 정의된 것.) 따라서 이러한 모순을 회피하기 위해서는
어떤 대상을 집합으로 바라볼 것인지에 대하여 공리적으로 명시하는,
아래에서 설명할 "공리적 집합론"이 필요하게 되었다.

## ZFC 공리계

Zermelo와 Fraenkel에 의한 ZF 공리계 이외에도 위의 역설에 관한 문제를 회피한
공리계가 여럿 존재하나, 일반적으로 ZF 공리계에 선택공리를 추가한 ZFC 공리계가
가장 널리 쓰이고 있다. 단, ZF 공리계에서는 특정한 조건을 만족하는 집합을 모아서
만든, *모임(class)* 이 형식적으로 다루어지지 않으므로, 이를 형식적으로 다루기 위해서는
*모임*을 기본적인 대상으로 바라보는 공리계인 NBG 공리계, 혹은 MK 공리계가 필요하다.
바꾸어 말하자면, ZF 공리계에서 다루는 모든 대상은 집합이다.

아래에서 기술된 일부 명제들은 조건의 범위가 집합으로 한정되어,
술어논리(predicate logic)를 이용하여 기술하는 것이 가능하지만, 일관성을 위하여
단순 논리식으로 기술하였다. 술어논리를 이용한다면 일부 명제는 다음과 같이 표기할 수 있을 것이다.

- $\forall w\in x [\phi(w)]$는 $\forall w \left[ w\in x \implies \phi(w) \right]$
- $\exists w\in x [\phi(w)]$는 $\exists w \left[ w\in x \land \phi(w) \right]$
	* $\exists w \left[ w\in x \implies \phi(w) \right]$와는 다르다. 정확히는 이 조건이
	  $\exists w\in x [\phi(w)]$로부터 유도되지만, 역은 일반적으로 성립하지 않는다.

### 외연성공리 (axiom of extensionality)

> **공리**. $\forall x \forall y \left[ x = y \iff \forall z \left[ z\in x \iff z\in y \right] \right]$

외연적기법을 통해 집합을 나타낼 수 있게 한다. 즉, 이 공리에 의하면 $ \left\{ a, b \right\} = \left\{ b, a \right\}$,
$ \left\{ a, a \right\} = \left\{ a \right\}$

### 이원집합공리 (axiom of pairing)

> **공리**. $\forall x \forall y \exists z \forall w \left[ w\in z \iff (w=x \lor w=y) \right]$

두 집합 $x, y$가 주어졌을 때, 이 두 집합만을 원소로 갖는 집합(pairing) $z = \left\{ x, y \right\}$가 존재한다는 공리이다.

### 병합공리 (axiom of union)

> **공리**. $\forall x \exists y \forall z \left[ z\in y \iff \exists w \left[ w\in x \land z\in w \right] \right]$

집합 $x$가 주어졌을 때, $x$의 원소인 집합 $w$의 원소 $z$를 원소로 갖도록하는 집합 $y$가 존재한다는 공리이다.
따라서, 일반적인 병합집합(union)의 표기를 빌려 사용하자면, $y = \bigcup x$인 것이다.
집합 $a, b$가 주어졌을 때의 일반적인 의미의 합집합 $a\cup b$ 또한
이 공리와 이원집합공리를 이용하여 존재를 보일 수 있다.

### 멱집합공리 (axiom of power set)

간단하게 표기하기 위해 다음 기호 $\subset$을 정의하자.

> **정의**(부분집합). $a\subset b \iff \forall x \left[ x\in a \implies x\in b \right]$

> **공리**. $\forall x\exists y \forall z \left[ z\in y \iff z\subset x \right]$

즉, 집합 $x$가 주어졌을 때, 그 부분집합 $z$의 전체를 원소로 갖는 집합 $y$가 존재한다는 공리이다.
일반적으로 $y$를 $x$의 멱집합(power set)이라고 하며, $y = \mathscr{P}(x)$와 같이 쓴다.

*주*. $(a\subset b \land b\subset a) \iff a = b$이다.

$$
\begin{aligned}
	a = b &\iff \forall x \left[ x\in a \iff x\in b \right] \\
	&\iff (\forall x \left[ x\in a \implies x\in b \right]) \land (\forall x \left[ x\in a \impliedby x\in b \right]) \\
	&\iff a\subset b \land b\subset a
\end{aligned}
$$

이러한 성질로부터, 쉽게 $\subset$이 순서의 이항관계라는 것을 알 수 있다.

### 분출공리꼴 (axiom schema of specification)

> **공리**. $\forall x \exists y \forall z \left[ z\in y \iff (z\in x \land \phi(z)) \right]$

여기서 $\phi(z)$는 $z$에 관한 조건이다. 즉, $z$에 관한 조건이 주어진다면, $\phi(z)$가 참값인
$z$만을 원소로 갖는 부분집합 $y$가 존재한다는 공리꼴이다.
원소의 범위를 이미 존재하는 집합인 $x$로 한정함으로써, Russell의 역설을 회피하는 것이 가능하다.
여기서 $\phi(z)$를 어떻게 설정하는가에 따라서 다양한 부분집합을 만드는 연산자를 정의할 수 있다.

> **정의**(교집합). 집합 $a, b$가 주어졌을 때, $\phi(z) = z\in b$로 두자. 위의 공리에 의하여 얻어지는
> $\forall z \left[ z\in y \iff (z\in a \land z\in b) \right]$ 인 $y$를 $a\cap b$, $a$와 $b$의 교집합(intersection)이라고 한다.

> **정의**(차집합). 집합 $a, b$가 주어졌을 때, $\phi(z) = z\notin b$로 두자. 위의 공리에 의하여 얻어지는
> $\forall z \left[ z\in y \iff (z\in a \land z\notin b) \right]$ 인 $y$를 $a\setminus b$, $a$와 $b$의 차집합(set difference)이라고 한다.

> **정의**. 집합 $a$가 주어졌을 때, $\phi(z) = \forall x [x\in a \implies z\in x]$로 두자. 위의 공리에 의하여 얻어지는
> $\forall z \left[ z\in y \iff (z\in \bigcup a \land \phi(z) ) \right]$ 인 $y$를 $\bigcap a$, $a$의 교집합이라고 한다.

집합론에서 다루어지는 다양한 요소의 존재 역시, 분출공리에 의하여 그 존재가 보장된다.

> **정의**(순서쌍). $(a, b) := \left\{ \left\{ a \right\}, \left\{ a, b \right\} \right\}$ 로 정의한다.

위 정의와 외연성공리에 의하여 $(a,b)=(c,d) \iff a=c \land b=d$임을 확인할 수 있다.

> **명제**(곱집합의 존재). 집합 $x$와 $y$가 주어졌을 때, $z\in x$, $w\in y$인 $(z, w)$ 전체의 집합이 존재한다.

*증명*. 집합 $x,y$가 주어졌을 때, $z\in x$, $w\in y$인 $(z,w)$전체의 집합이 존재함을 분출공리에 의하여 보일 수 있다.
$(z,w)= \left\{ \left\{ z \right\}, \left\{ z, w \right\} \right\}$이므로,
$ \left\{ z \right\}, \left\{ z,w \right\} \in \mathscr{P}(x\cup y)$,
$(z,w)= \left\{ \left\{ z \right\}, \left\{ z,w \right\} \right\} \in \mathscr{P}(\mathscr{P}(x\cup y))$이다.
따라서 $\phi(s) = \exists z\exists w \left[ s = (z,w) \land z\in x \land w\in y \right]$로 두면,
$\forall s \left[ s\in p \iff (s\in\mathscr{P}(\mathscr{P}(x\cup y))\land\phi(s)) \right]$를 만족하는 $p$가 존재하며,
이것이 $z\in x, w\in y$인 $(z,w)$전체의 집합임을 알 수 있다. □

*주*. 위 증명에서의 $p$를 $x$와 $y$의 *곱집합*이라고 하며, $p=x\times y$와 같이 나타낸다.

> **명제**(사상의 존재). 집합 $x$와 $y$가 주어졌을 때, $x$의 각 원소에 $y$의 원소 하나만이 대응하는
> 순서쌍의 집합 전체의 집합(사상의 집합)이 존재한다.
> 즉 $\forall z \left[ z\in x \implies \exists! w \left[ (z,w)\in f \right] \right]$를 만족하는 $f$ 전체의 집합이
> 존재한다.

*증명*. $\phi(f) = \forall z \left[ z\in x \implies \exists! w \left[ (z,w)\in f \right] \right]$로 두면,
분출공리꼴에 의해 $\forall f \left[ f\in m \iff (f\in\mathscr{P}(x\times y) \land \phi(f)) \right]$인 집합 $m$이 존재한다. □

*주*. $f$와 같은 순서쌍의 집합을 $x$에서 $y$로의 *사상(map)* 이라고 한다.
$x$에서 $y$로의 사상이라는 것을 나타내기 위해 $f: x\to y$와 같이 쓴다.
또한 $x$에서 $y$ 로의 사상 $m$ 전체의 집합을 $\text{Map}(x,y)$와 같이 쓴다.
$(a,b)\in f$인 것을 $f(a) = b$ 혹은 $f: a\mapsto b$와 같이 쓰기도 한다.

### 무한공리 (axiom of infinity)

여기서 분출공리꼴과 무한공리를 적용하면 공집합 $\emptyset$의 존재를 보일 수 있다.

### 정칙성공리 (axiom of regularity)

### 치환공리꼴 (axiom schema of replacement)

### 선택공리 (axiom of choice)

## 부수적인 성질과 정의

### 집합의 연산

집합의 연산에 관하여 이하의 성질이 성립한다. 단, $A^\complement$는, $A$를 포함하는 보편집합 $X$가 주어졌을 때,
$X\setminus A$를 의미한다.

1. $A\cup B = B\cup A$ : 합집합 연산은 가환이다.
2. $A\cap B = B\cap A$ : 교집합 연산은 가환이다.
3. $A\subset X \land B\subset X \implies A\cup B\subset X$ : 두 집합의 합집합은 두 집합을 동시에 포함하는 최소의 집합이다.
4. $A\supset X \land B\supset X \implies A\cap B\supset X$ : 두 집합의 교집합은 두 집합에 동시에 포함되는 최대의 집합이다.
5. $(A\cup B)\cup C = A\cup(B\cup C)$ : 합집합 연산에 관하여 결합법칙이 성립한다.
6. $(A\cap B)\cap C = A\cap(B\cap C)$ : 교집합 연산에 관하여 결합법칙이 성립한다.
7. $(A\cup B)\cap C = (A\cap C)\cup(B\cap C)$ : 합집합과 교집합 연산간에 분배법칙이 성립한다.
8. $(A\cap B)\cup C = (A\cup C)\cap(B\cup C)$ : 합집합과 교집합 연산간에 분배법칙이 성립한다.
9. $X\setminus(A\cup B) = (X\setminus A)\cap(X\setminus B)$ : de Morgan의 법칙.
10. $X\setminus(A\cap B) = (X\setminus A)\cup(X\setminus B)$ : de Morgan의 법칙.
11. $(A\cup B)^\complement = A^\complement \cap B^\complement $
12. $(A\cap B)^\complement = A^\complement \cup B^\complement $
13. $X-A = X\cap A^\complement$

공집합이 아닌 $\Lambda$를 첨자집합으로 하여,
집합계 $A: \Lambda\to X, \lambda \mapsto A_\lambda$ 가 주어진 경우에는 다음과 같은 기술도 가능하다.

- $\bigcup_{\lambda\in\Lambda}A_\lambda = \left\{ x \,|\, \exists\lambda\in\Lambda[x\in A_\lambda] \right\}$
- $\bigcap_{\lambda\in\Lambda}A_\lambda = \left\{ x \,|\, \forall\lambda\in\Lambda[x\in A_\lambda] \right\}$

이 기술에 의하면, 다음과 같은 성질이 집합계 $A$와 집합 $B$에 대하여 성립한다.

1. $ \left( \bigcup_{\lambda\in\Lambda} A_\lambda \right) \cap B = \bigcup_{\lambda\in\Lambda} \left( A_\lambda \cap B \right)$
2. $ \left( \bigcap_{\lambda\in\Lambda} A_\lambda \right) \cup B = \bigcap_{\lambda\in\Lambda} \left( A_\lambda \cup B \right)$
3. $ \left( \bigcup_{\lambda\in\Lambda} A_\lambda \right)^\complement = \bigcap_{\lambda\in\Lambda} \left( A_\lambda \right)^\complement$
4. $ \left( \bigcap_{\lambda\in\Lambda} A_\lambda \right)^\complement = \bigcup_{\lambda\in\Lambda} \left( A_\lambda \right)^\complement$

### 사상

#### 사상에 의한 상과 역상

집합 $A$에서 $B$로의 사상 $f: A\to B$ (혹은 $f\in \text{Map}(A, B)$)가 주어졌을 때,
$A_1\subset A$에 대하여
$f(A_1):= \left\{ y\in B \,|\, \exists x\in A_1 \left[ f(x) = y \right] \right\}= \left\{ f(x) \,|\, x\in A_1 \right\}$
를 $A_1$에 대한 $f$의 상(image)이라고 한다.
또한, $B_1\subset B$에 대하여 $f^{-1}(B_1) = \left\{ x\in A \,|\, f(x) \in B_1 \right\}$을 $B_1$에 대한 $f$의 역상이라고 한다.

다음 성질이 $f: A\to B$, $A_1,A_2\subset A$, $B_1, B_2\subset B$에 대하여 성립한다.

1. $f(A_1\cup A_2) = f(A_1)\cup f(A_2)$
2. $f(A_1\cap A_2) \subset f(A_1)\cap f(A_2)$
3. $f^{-1}(B_1\cup B_2) = f^{-1}(B_1)\cup f^{-1}(B_2)$
4. $f^{-1}(B_1\cap B_2) = f^{-1}(B_1)\cap f^{-1}(B_2)$
5. $A_1\subset f^{-1}(f(A_1))$
6. $f(f^{-1}(B_1))\subset B_1$
7. $f(A_1) \setminus f(A_2) \subset f(A_1\setminus A_2)$
8. $f^{-1}(B_1) \setminus f^{-1}(B_2) = f^{-1}(B_1\setminus B_2)$

집합계 $A: \Lambda\to X$와 사상 $f: Y\to Z$, $g:Z\to Y$가 주어졌을 때,
임의의 $\lambda\in\Lambda$에 대하여 $A_\lambda \in Y$라면, 다음이 성립한다.

1. $f \left( \bigcup_{\lambda\in\Lambda} A_\lambda \right) = \bigcup_{\lambda\in\Lambda} f(A_\lambda)$
1. $f \left( \bigcap_{\lambda\in\Lambda} A_\lambda \right) \subset \bigcap_{\lambda\in\Lambda} f(A_\lambda)$
1. $g^{-1} \left( \bigcup_{\lambda\in\Lambda} A_\lambda \right) = \bigcup_{\lambda\in\Lambda} g^{-1}(A_\lambda)$
1. $g^{-1} \left( \bigcap_{\lambda\in\Lambda} A_\lambda \right) = \bigcap_{\lambda\in\Lambda} g^{-1}(A_\lambda)$

#### 전사, 단사, 전단사

사상 $f: X\to Y$가 주어졌다고 하자.

- 임의의 $x_1, x_2\in X$에 대하여 $f(x_1) = f(x_2)$ 이면 $x_1 = x_2$일 때, $f$는 *단사(injection)* 이다.
- 임의의 $y\in Y$에 대하여 $f(x) = y$인 $x\in X$가 존재하면 $f$는 *전사(surjection)* 이다.
- $f$가 전사인 동시에 단사이면, $f$는 *전단사(bijection)* 이다.

> **명제**. 다음 두 조건은 동치이다.
>
> 1. $f: X\to Y$가 전단사
> 2. $\exists! g\in \text{Map}(Y,X) \left[ g\circ f = \text{id}_{X} \land f\circ g = \text{id}_{Y} \right]$,
>    (단, $\text{id}_{A}$는 집합 $A$ 상의 항등사상.)

*증명*.

**1에서 2를 유도**  
$g: Y\to X, f(x)\mapsto x$와 같이 정의할 때, $f$의 전단사성으로부터 사상 $g$가 well-defined임을 알 수 있다.
$(g\circ f)(x) = g(f(x)) = x$, 또한, 임의의 $y\in Y$가 주어졌을 때, $f(x')= y$인 $x'\in X$가 존재하므로,
$(f\circ g)(x) = f(g(y)) = f(g(f(x'))) = f(x') = y$이므로, $g$는 2의 조건을 만족하는 사상이다.

$g$가 존재하는 것을 보였으므로, $g$가 2를 만족하는 유일한 사상임을 보이자. $h$ 또한 2를 만족하는 사상이라고
가정하면, 임의의 $y\in Y$에 대하여 $f(g(y)) = y = f(h(y))$이다. $f$의 단사성에 의해 $g(y) = h(y)$이므로,
$g=h$임을 알 수 있다. 따라서 $g$는 유일.

**2에서 1을 유도**  
2의 조건을 만족하는 사상 $g$가 존재한다고 하자. $x_1, x_2\in X$에 대하여
$f(x_1) = f(x_2)$라고 하면, $x_1 = g(f(x_1)) = g(f(x_2)) = x_2$이므로 $f$는 단사.
임의의 $y\in Y$에 대해서 $x = g(y)$로 두면, $f(x) = f(g(y)) = y$이므로 $f$는 전사.
따라서 $f$는 전단사 사상이다. □

*주*. $y_1, y_2\in Y$에 대하여 $g(y_1) = g(y_2)$이면, $y_1 = f(g(y_1)) = f(g(y_2)) = y_2$이므로 사상 $g$는 단사,
임의의 $x\in X$에 대하여 $y = f(x)$로 두면 $g(y) = g(f(x)) = x$이므로 사상 $g$는 전사, 즉 $g$가 전단사임을 알 수 있다.
따라서 $g$ 역시 $g\circ g' = \text{id}_X$, $g'\circ g = \text{id}_Y$ 를 만족하는 사상 $g': X\to Y$이 존재함을 알 수 있고,
이러한 사상이 유일하게 존재한다는 것을 보였으므로 $g' = f$이다. 이러한 성질으로부터, $f$와 $g$를 서로의 역사상이라고 부르며, $f$가 전단사 사상일 때,
$f$의 역사상을 $f^{-1}$로 쓰기도 한다.

