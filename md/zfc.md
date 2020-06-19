<!---
title: "공리적 집합론: ZFC 공리계"
category: Mathematics
language: Korean
--->

# 공리적 집합론: ZFC 공리계

## Russell의 역설

집합을 "특정한 조건을 만족하는 원소의 모임"으로 정의하였을 때의 문제점을 생각하자.
어떠한 조건이든지 집합을 만드는 것이 가능하므로 가령 $A = \left\{ x \,|\, x\not\in x \right\}$와
같은 집합을 정의할 수 있다. 실제로 $A$ 에 속하는 원소가 존재하는지 알 수는 없지만,
만약 $A\in A$라고 가정하면 $A\not\in A$이고, $A\not\in A$라고 가정하면 $A\in A$이다.
즉 $A\in A \iff A\not\in A$이므로, 이는 논리 체계에 있어서 모순이다. (Russell의 역설)

이 모순의 근원은 어느 대상을 "집합"으로 정의하는 가에 있어서, 어떠한 조건이든지 그에 해당하는
집합을 만들 수 있다고 가정한 것이다. 따라서 이러한 모순을 회피하기 위해서는
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

두 집합 $x, y$가 주어졌을 때, 이 두 집합만을 갖는 집합 $z = \left\{ x, y \right\}$가 존재한다는 공리이다.

### 병합공리 (axiom of union)

> **공리**. $\forall x \exists y \forall z \left[ z\in y \iff \exists w \left[ w\in x \land z\in w \right] \right]$

집합 $x$가 주어졌을 때, $x$의 원소인 집합 $w$의 원소 $z$를 원소로 갖도록하는 집합 $y$가 존재한다는 공리이다.
따라서, 일반적인 집합의 표기를 빌려 사용하자면, $y = \bigcup x$인 것이다.
집합 $a, b$가 주어졌을 때의 일반적인 의미의 합집합 $a\cup b$ 또한
이 공리와 이원집합공리를 이용하여 존재를 보일 수 있다.

### 멱집합공리 (axiom of power set)

간단하게 표기하기 위해 다음 기호 $\subset$을 정의하자.

> **정의**(부분집합). $a\subset b \iff \forall x \left[ x\in a \implies x\in b \right]$

> **공리**. $\forall x\exists y \forall z \left[ z\in y \iff z\subset x \right]$

즉, 집합 $x$가 주어졌을 때, 그 부분집합 $z$의 전체를 원소로 갖는 집합 $y$가 존재한다는 공리이다.
일반적으로 $y$를 $x$의 멱집합이라고 하며, $y = \mathscr{P}(x)$와 같이 쓴다.

*주*. $(a\subset b \land b\subset a) \iff a = b$이다.

$$
\begin{aligned}
	a = b &\iff \forall x \left[ x\in a \iff x\in b \right] \\
	&\iff (\forall x \left[ x\in a \implies x\in b \right]) \land (\forall x \left[ x\in a \impliedby x\in b \right]) \\
	&\iff a\subset b \land b\subset a
\end{aligned}
$$

### 분출공리꼴 (axiom schema of specification)

원소의 범위를 이미 존재하는 집합으로 한정함으로써, Russell의 역설을 회피하는 것이 가능하다.

### 무한공리 (axiom of infinity)

### 정칙성공리 (axiom of regularity)

### 치환공리꼴 (axiom schema of replacement)

### 선택공리 (axiom of choice)

