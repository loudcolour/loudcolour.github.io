<!---
title: '선택공리'
category: 'Set Theory'
language: Korean
--->

# 선택공리

> **공리**(선택공리). 공집합이 아닌 집합 $A$의 모든 원소는
> 공집합이 아닌 집합이라고 하자.
> 이 때, 모든 $x\in A$에 대하여 $f(x) \in x$인 사상 $f:A\to\bigcup A$가 존재한다.

$A$가 무한집합이라면, 특히나 가산이 아니라면 위의 공리를 자명한 것으로 받아 들이기 쉽지 않을 것이다.
예를 들어 $A$의 원소가 실수의 개수만큼이나 존재한다면,
그 원소들로부터 하나하나 대표원소를 선택하는 것이 가능하다고 단정지을 수 있을까?
이런 난관으로부터 편리하게 벗어나기 위해 선택공리(axiom of choice, $\textsf{AC}$)를 받아들여 사용할 수 있다.

선택공리의 중요한 점은, 선택 함수(아래 명제에서 등장)가 존재한다는 사실만을
주장하는 것이다. 구체적인 선택 함수—그것을 구하는 것이 난제일 수도 있다—가
어떻게 제시될 지 모르더라도, 선택공리를 통해 **아무튼** 그러한 사상이
존재한다는 것만은 받아들일 수 있도록 하는 것이다.

> **명제**. 다음은 모두 동치이다.
> 
> 1. 선택공리
> 2. $A$가 공집합이 아닌 집합일 때,
> 모든 $x\in\mathscr{P}(A)\setminus\{\emptyset\}$에 대하여
> $f(x)\in x$인 사상 $f:\mathscr{P}(A)\setminus\{\emptyset\}\to A$가
> 존재한다.
> 3. 공집합이 아닌 집합 $I$를 첨자역으로 하는 집합족 $\left\{ A_i \,|\, i\in I\right\}$에
> 대하여, $\forall i\in I, A_i \not=\emptyset$이라면, 곱집합
> $\prod_{i\in I}A_i$또한 공집합이 아니다.
> 즉, 모든 $i\in I$에 대해 $g(i)\in A_i$인 선택 함수
> $g:I\to\bigcup_{i\in I}A_i$가 존재한다.

*증명*.  

**1에서 2를 유도**  
이 때, $X = \mathscr{P}(A)\setminus\left\{\emptyset\right\}$로 두면, $X$의 모든 원소는
공집합이 아니므로, 선택공리에 의하여
$\forall x\in X$에 대해, $f(x)\in x$인 사상 $f:X\to A$가 존재한다.
($\because\,\bigcup\mathscr{P}(A) = A$)  

**2에서 3을 유도**  
$X=\bigcup_{i\in I} A_i$ 라고 두면,
$X\not=\emptyset$이다.
따라서 $\forall x\in \mathscr{P}(X)\setminus\left\{\emptyset\right\}$에 대하여,
$f(x)\in x$인 사상 $f:\mathscr{P}(X)\setminus\left\{\emptyset\right\}\to X$가
존재한다.
$\forall i\in I$에 대해 $A_i\in \mathscr{P}(X)\setminus\left\{\emptyset\right\}$이므로,
$f(A_i)\in A_i$가 성립한다. 여기서 $g:I\to X$, $i\mapsto f(A_i)$와 같은 사상을 정의하면,
$g(i)\in A_i$이므로 각 $i\in I$에 대해 해당하는 $g(i)$를 선택하여
$g(i)$로 순서쌍 $o(g)$을 만들면 $o(g)\in\prod_{i\in I}A_i$, 따라서 $\prod_{i\in I}A_i\not=\emptyset$  

**3에서 1을 유도**  
$A$ 그 자체는 $A$를 첨자역으로하는 집합족 $\left\{ x \,|\, x\in A\right\}$와 같다.
따라서, 모든 $x\in A$에 대해 $g(x)\in x$를 만족하는 사상 $g:A\to\bigcup A$가 존재하고,
이는 선택공리의 진술과 같다. □

> **명제**. $\textsf{ZF}$ 상에서 다음은 모두 동치이다.
>
> 1. 선택공리
> 1. [Zorn의 보조정리 (Zorn's lemma)](./zorns-lemma.html)
> 1. [정렬정리 (well-ordering theorem)](./well-ordered.html#정렬정리)

*증명*. 1 $\implies$ 2 $\implies$ 3$\implies$ 1을 보인다.
1 $\implies$ 2는 [Zorn의 보조정리의 증명](./zorns-lemma.html)을,
2 $\implies$ 3과 3 $\implies$ 1 은 [정렬정리의 증명](./well-ordered.html#정렬정리)을 참고. □

## 선택공리로부터 유도되는 명제

$\textsf{ZF}$ 상에서, 다음과 같은 명제들이 선택공리로부터 유도된다.

- 기수(cardinal)를 정의할 수 있다. 즉, 임의의 집합 $X, Y$에 대하여, $|X|\leq |Y|$혹은 $|X|\geq |Y|$가 성립한다([기수 비교에 있어서의 trichotomy](well-ordered.html#정렬정리)
참고). 이는 선택공리와 동치이다.
- 임의의 무한집합 $X$에 대하여 $|X^2| = |X|$ 이다. 즉, 임의의 기수 $\kappa$에 대하여 $\kappa^2 =\kappa$. 동시에 선택공리와 동치이다.
- 임의의 무한집합 $X$는 가산집합인 부분집합을 갖는다. 따라서 임의의 기수 $\kappa$에 대하여 $\aleph_0 \leq \kappa$.
- 가산집합인 $\Lambda$를 첨자역으로하는 집합족 $ \left\{ A_\lambda \,|\, \lambda\in\Lambda \right\}$에 대하여, 모든 $A_\lambda$가
가산집합이라면 $\bigcup_{\lambda\in\Lambda}A_\lambda$ 역시 가산집합이다.
- [임의의 벡터공간에는 기저가 존재](./basis-of-vector-space.html#벡터공간의-기저의-존재)한다. 동시에 선택공리와 동치이다.
	* $\mathbb{Q}$상의 벡터공간 $\R$ 역시 기저를 갖는다. 이를 이용하면, $f(x+y) = f(x) + f(y)$ 혹은 $f(x+y) = f(x)f(y)$를
	만족하는 동시에 연속이지 않은 함수 $f$를 만드는 것이 가능하다.
- Lebesgue 측도를 갖지 않는 집합이 존재한다.
	* Banach-Tarski의 역설: 구를 유한개의 조각으로 쪼개어, 쪼갠 조각을 다시 붙여서 원래의 구와 같은 크기의 구 2개를 만들 수 있다.
	  Lebesgue 측도를 갖지 않는 집합이 존재하지 않으므로, 모순없이 이런 조작이 가능하다.
- 의존선택공리 (axiom of dependent choice, $\textsf{DC}$)
- 가산선택공리 (axiom of countable choice, $\textsf{AC}_\omega$)
	* 의존선택공리로부터 유도된다. 즉, $\textsf{AC}\implies\textsf{DC}\implies\textsf{AC}_\omega$

## 참고문헌

- [Andreas Blass, *Existence of bases implies the axiom of choice*](http://www.math.lsa.umich.edu/~ablass/bases-AC.pdf)
- [Steven G. Johnson, *Notes on discontinuous $f(x)$ satisfying $f(x+y) = f(x)· f(y)$* ](https://math.mit.edu/~stevenj/exponential.pdf)


