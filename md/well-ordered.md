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

> **정의**. $(X, \leq)$가 정렬집합이라고 하자. 이때 $a\in X$에 대하여,
> $X\langle a\rangle = \{x\in X\,|\,x\leq a, x\not=a\}$를 $a$에 대한 $X$의 절편이라고 한다.

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

## 정렬집합의 비교정리

> **정의**. $(X,\leq)$와 $(Y, \leq')$가 정렬집합이라고 하자. 이 때,
> 어떤 $b\in Y$가 존재하여 $X\simeq Y \langle b \rangle $라면, $\|X\| < \|Y\|$라고
> 쓰자. 또한 $\|X\|<\|Y\|$이거나 $X\simeq Y$일 때, $\|X\| \leq \|Y\|$라고 쓰도록 하자.

> **명제**. 정렬집합 $(X,\leq)$와 $(Y,\leq')$가 주어졌을 때,
> $\|X\|\leq\|Y\|$인 동시에 $\|Y\|\leq\|X\|$이면, $X \simeq Y$이다.

