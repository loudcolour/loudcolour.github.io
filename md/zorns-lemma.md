<!---
title: "Zorn의 보조정리"
category: Set Theory
language: Korean
--->

# Zorn의 보조정리

> **정의**. 순서집합 $(X,\leq)$가 주어졌을 때, 임의의 전순서인 부분집합(즉, 사슬(chain))이
> 위로 유계라면 $(X, \leq)$는 귀납적(inductive)이다.

> **정의**. 순서집합 $(X,\leq)$가 주어졌을 때, $X$의 원소 $a\in X$가 극대라는 것은,
> $a\leq x$ 인 동시에 $a\not= x$인 $x\in X$가 존재하지 않는 것을 의미한다.

> **정리**(Zorn의 보조정리). 귀납적인 순서집합은 적어도 하나의 극대 원소를 갖는다.

## 증명에 필요한 보조정리

> **보조정리**. $(A,\leq)$를 귀납적인 순서집합이라고 하자. $\forall x\in A \left[ x\leq f(x) \right]$인
> 사상 $f: A\to A$에 대하여, $f(a) = a$인 $a\in A$가 하나 이상 존재한다.

*증명*. $f$가 순서를 보존하는 사상이라면 임의의 $x\in A$에 대하여 $x\leq f(x)$가 성립하는 것은
알려져 있으므로, 이러한 $f$가 우선 존재한다는 것을 확인할 수 있다.
이 때, 다음 조건을 만족하는 $A$의 부분집합 $W$를 생각하자. (단, $x_0\in A$는 고정된 원소이다.)

1. $W$는 정렬집합.
2. $\min W = x_0$.
3. $x\in W$에 대하여 $x^*:=\max W \langle x \rangle$ 가 존재한다면, $x = f(x^*)$
4. $x\in W\setminus \left\{ x_0 \right\}$에 대하여 $x^*:=\max W \langle x \rangle$ 가 존재하지 않는다면,
$x = \sup_A W \langle x \rangle$

실제로 $ \left\{ x_0 \right\}$로 두어 순서를 부여하면, 자명하게 $W$의 조건을 만족하고 있으므로,
조건을 만족하는 $W$는 존재한다. 따라서, $B$를 조건을 만족하는 $W$ 전체의 집합이라고 하면,
$B\neq \emptyset$ 임을 알 수 있다.

여기서, $W, W'\in B$라면, $W=W'$이거나 $W$나 $W'$의 어느 한쪽이 다른 한쪽의 절편과
일치하는 것을 보이자.
정렬집합의 비교정리에 의하여,
$W\simeq W'$ 혹은 $W$와 $W'$의 어느 한쪽이 다른 한쪽의 절편과 동형이라는 것을 알 수 있다.
$W\simeq W'$ 인 경우를 생각하자. 이 때의 순서동형사상을 $\phi: W\to W'$라고 하면,
모든 $x\in W$에 대하여 $\phi(x) = x$가 성립하는 것을 초한귀납법을 이용하여 보일 수 있다.

- $x_0= \min W = \min W'$이므로, $\phi(x_0) = x_0$이다.
- $x\in W\setminus \left\{ x_0 \right\}$이고, $y<x$인 $y\in W$에 대하여
$\phi(y) = y$가 성립하고 있다고 하자. 그렇다면,
	* $x^* = \max W \langle x \rangle$가 존재하는 경우:
	$\phi$는 순서동형사상이므로, $\phi(x^*) = \max W' \langle \phi(x) \rangle$ 이고,
	$\phi(x^*) = x^*$이므로, $\phi(x) = f(\phi(x^*)) = f(x^*) = x$가 성립한다.
	* $x^* = \max W\langle x\rangle$가 존재하지 않는 경우:
	$\phi$가 순서동형사상이므로, $\max W'\langle\phi(x)\rangle$ 역시 존재하지 않는다.
	또한 $\phi(W \langle x \rangle) = W' \langle \phi(x) \rangle$이고,
	$W \langle x \rangle$의 모든 원소에 대하여 $\phi(y) = y$가 성립하고 있으므로,
	$W\langle x\rangle = \phi(W \langle x \rangle) = W' \langle \phi(x) \rangle$.
	따라서, $\phi(x) = \sup_A W' \langle \phi(x) \rangle = \sup_A W \langle x \rangle = x$가 성립한다.

이는 $W, W'$의 어느 한쪽이 다른 한쪽의 절편과 동형인 경우에도 적용할 수 있으므로,
결론적으로 $W$와 $W'$가 일치하거나, $W, W'$의 어느 한쪽이 다른 한쪽의 절편과 일치하는 것을
알 수 있다. 이상과 위의 [정렬집합의 구성정리](./well-ordered.html#정렬집합의-구성정리)로부터,
$W_0 := \bigcup B$으로 두면, $W_0$ 또한 정렬집합이고,
$B$의 임의의 원소는 $W_0$와 일치하거나 $W_0$의 절편이다. 따라서, $W_0$는
위의 조건 1, 2, 3, 4를 만족, $W_0\in B$이다. 특히 $W_0 = \max_{\subset} B$임을 보일 수 있다.

$W_0$는 정렬집합인 $A$의 부분집합이므로, $W_0$는 사슬이다. $A$가 귀납적이므로,
$a := \sup_A W_0$가 존재한다. 여기서 만약 $a\notin W_0$라고 가정하면,
$W_1 = W_0 \cup \left\{ a \right\}$로 두면, $W_1$역시 $W_1\in B$이고 $W_0\subsetneq W_1$이므로,
$W_0 = \max_{\subset} B$에 모순이다.
따라서 $a\in W_0$이고, $a :=\max_A W_0$라는 것을 알 수 있다.

여기서 $f(a) = a$임을 보이자.
$f(a) \neq a$라고 가정하면 $f(a) > a$이다. $a = \max_A W_0$이므로, $f(a)\notin W_0$
이나, $W_2 = W_0 \cup \left\{ f(a) \right\}$로 두면 $W_2$가 조건 1, 2, 3, 4
를 만족한다는 것을 쉽게 알 수 있으므로, $W_2\in B$이고 $W_0\subsetneq W_2$이므로,
$W_0 = \max_{\subset} B$에 모순이다. 따라서 $f(a) = a$. □

> **보조정리**. $A$를 극대원소를 갖지 않는 순서집합이라고 하면,
> 임의의 $x\in A$에 대하여 $x< f(x)$인 $f:A\to A$가 존재한다.

*증명*. 
$\mathscr{A} = \mathscr{P}(A)\setminus \left\{ \emptyset \right\}$로 두면,
$\bigcup\mathscr{A} = A$이라는 것을 알 수 있다.
[선택공리](./axiom-of-choice.html)에 의하면,
임의의 $X\in \mathscr{A}$에 대하여 $s(X)\in X$인 사상 $s: \mathscr{A}\to A$가 존재한다.

$x\in A$에 대하여
여기서 $M_x = \left\{ y\in A \,|\, y > x \right\}$로 두면,
$A$가 극대원소를 갖지 않는 순서집합이라고 하였으므로,
임의의 $x\in A$에 대하여 $M_x\neq\emptyset$, $M_x\in \mathscr{A}$임을 알 수 있다.

여기서 $f: A\to A, x\mapsto s(M_x)$와 같이 $f$를 정의하면,
$f(x)\in M_x$, $x < f(x)$이다. □

따라서 위의 두 보조정리를 이용하면 Zorn의 보조정리의 증명을 얻는다.

## 참고문헌

- 松坂 和夫, *集合・位相入門*

