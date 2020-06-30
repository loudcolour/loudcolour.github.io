<!---
title: '준동형과 동형'
category: Algebra
language: Korean
--->

# 준동형과 동형

"두 군이 본질적으로 같은 구조를 갖고 있는가"라는 질문에 대답하기 위해서는
군이 단순한 집합이 아닌, 특정한 연산이 주어진 집합이라는 사실을 상기할 필요가
있다. 따라서 두개의 군을 집합 대 집합으로서 비교하는 것은 무리가 있으며,
연산에 직접 대응하는 것이 필요하다는 것을 알 수 있다. 여기서 새로이 도입할
준동형과 동형은 이러한 연산에 대응하고 있는 두 군 사이의 사상이다.

## 군의 준동형

> **정의**(군의 준동형). 군 $G_1, G_2$에 대해서 사상 $\phi: G_1 \to G_2$이
> 다음 조건을 만족하면 $\phi$는 준동형이다.
>
> - $\forall x,y \in G_1$에 대하여, $\phi(xy) = \phi(x)\phi(y)$

> **정의**. 군 $G_1, G_2$간의 준동형사상 $\phi$가 역사상을 가지며,
> 역사상 또한 준동형일 때, $\phi$는 동형 사상이라고 한다.
> 이 경우, 군 $G_1, G_2$는 서로 동형이라고 하며, 기호로
> $G_1\cong G_2$와 같이 나타낸다.

> **정의**. 군 $G_1, G_2$간의 준동형사상 $\phi$에 대하여 각각
> $\text{Ker}(\phi)$와 $\text{Im}(\phi)$를 다음과 같이 정의한다.
> 
> - $\text{Ker}(\phi) = \left\{x\in G_1 | \phi(x) = 1_{G_2}\right\}$
> - $\text{Im}(\phi) = \left\{\phi(x)|x\in G_1\right\}$

### 군의 준동형에 관한 명제

> **명제**. 전단사 사상 $\phi:G_1 \to G_2$가 준동형사상이라면,
> $\phi$는 동형 사상이다.

*증명*. $\phi$는 전단사이므로 역사상이 존재한다. 그 역사상을
$\psi: G_2 \to G_1$라고 하자. $x,y\in G_2$에 대해

$$
\phi(\psi(x)\psi(y)) = \phi(\psi(x))\phi(\psi(y)) = xy = \phi(\psi(xy))
$$

가 준동형에 의해 성립하고, $\phi$는 단사이므로, $\psi(x)\psi(y) = \psi(xy)$가
성립한다. □

> **명제**. $\phi:G_1\to G_2$가 준동형이라면, 다음이 성립한다.
> 
> 1. $\phi(1_{G_1}) = 1_{G_2}$
> 1. $\forall x\in G_1,\ \phi(x^{-1}) = {\phi(x)}^{-1}$

*증명*. 
1. $\phi(1_{G_1}) = \phi(1_{G_1}\cdot 1_{G_1}) = \phi(1_{G_1})\cdot\phi(1_{G_1})$,
양변에 $\phi(1_{G_1})^{-1}$을 오른쪽에 (혹은 왼쪽에) 곱하면, $1_{G_2} = \phi(1_{G_1})$
1. $1_{G_2} = \phi(1_{G_1}) = \phi(xx^{-1}) = \phi(x)\phi(x^{-1})$,
양변에 $\phi(x)^{-1}$을 왼쪽으로 곱하면 $\phi(x^{-1}) = {\phi(x)}^{-1}$ □

> **명제**. $\phi:G_1\to G_2$가 준동형일 때,
> $\text{Ker}(\phi)$과 $\text{Im}(\phi)$는 각각 $G_1$과 $G_2$의 부분군이다.

*증명*.

**$\text{Ker}(\phi)$은 $G_1$의 부분군이다.**  
1번에서 알 수 있듯이 $1_{G_1}\in\text{Ker}(\phi)$ 이다.
$x,y \in\text{Ker}(\phi)$이라고 하면, $\phi(xy) = \phi(x)\phi(y) = 1_{G_2}\cdot1_{G_2} = 1_{G_2}$,
따라서 $xy\in\text{Ker}(\phi)$, $\text{Ker}(\phi)$는 주어진 연산에 대해 닫혀있다.
마지막으로 2번에 의해 $\phi(x)=1_{G_2}$라면, $\phi(x^{-1}) = \phi(x)^{-1}=1_{G_2}$,
$\text{Ker}(\phi)$는 역원에 대해서도 닫혀있음을 알 수 있다.

**$\text{Im}(\phi)$은 $G_2$의 부분군이다.**  
역시 1번에 의해 $1_{G_{2}}\in\text{Im}(\phi)$. $x,y \in\text{Im}(\phi)$일 때, $\phi(a) = x$,
$\phi(b) = y$인 $a, b\in G_1$가 존재한다.
$\phi(ab)=\phi(a)\phi(b)=xy$이므로, $\text{Im}(\phi)$은 닫혀있다.
$x \in\text{Im}(\phi)$ 이라고 하면 $\phi(a)=x$인 $a\in G_1$이 존재하고, 2번에 의해
$1_{G_2} = \phi(1_{G_1}) = \phi(aa^{-1}) = \phi(a)\phi(a^{-1})$이고,
$\phi(a^{-1})\in \text{Im}(\phi)$이므로 $\text{Im}(\phi)$에 대해서도 닫혀있음을 알 수 있다. □

> **명제**. 준동형사상 $\phi: G_1\to G_2$에 대하여 다음 두 조건은 동치이다.
>
> - $\phi$가 단사
> - $\text{Ker}(\phi) = \left\{ 1_{G_1} \right\}$

### 군의 준동형의 예시

- 어떤 군 $G$와 그 부분군 $H$에 대하여, $\phi: H\to G, x\mapsto x$는
준동형사상이다. $G$와 $H$의 구체적인 예로, $G = \text{GL}_n(\R)$,
$H = \text{O}(n)$을 들 수 있다.
- $\R^{+}$는 곱에 의해, $\R$은 합에 의해 군을 이룬다.
여기서 사상 $\phi:\R\to\R^{+}, x\mapsto e^x$은 이 군 사이의 준동형이고,
전단사 사상이므로, 동형 사상이다.
- 가역행렬의 행렬식을 사상으로 생각하면,
$\text{det}:\text{GL}_n(\R)\to\R^{\times}$와 같이 나타내어지고,
두 행렬 $A, B$에 대해 $\text{det}(AB) = \text{det}(A)\text{det}(B)$이므로,
이는 준동형사상임을 알 수 있다. $\text{Ker}$의 정의상
$\text{Ker}(\text{det})$은 $\text{SL}_n(\R)$임을 보일 수 있다.

## 환의 준동형

> **정의**(환의 준동형). 환 $R_1, R_2$에 대해서 사상 $\phi: R_1\to R_2$가
> 다음 조건을 만족하면 $\phi$는 준동형이다.
>
> - $\forall x,y\in R_1$에 대하여 $\phi(x+y) = \phi(x) + \phi(y)$
> - $\forall x,y\in R_1$에 대하여 $\phi(xy) = \phi(x)\phi(y)$
> - $\phi(1_{R_1}) = 1_{R_2}$

세번째의 조건을 빼고 환의 준동형을 정의하는 경우도 있으나,
여기에서는 편의상 세번째의 조건을 포함하여 환의 준동형을 정의한다.

> **정의**. 환 $R_1, R_2$간의 준동형사상 $\phi$가 역사상을 가지며,
> 역사상 또한 준동형일 때, $\phi$는 동형사상이라고 한다.
> 군과 마찬가지로, 이 때, $R_1\cong R_2$와 같이 나타낸다.

> **정의**. 환 $R_1, R_2$간의 준동형사상 $\phi$에 대하여 각각
> $\text{Ker}(\phi)$와 $\text{Im}(\phi)$를 다음과 같이 정의한다.
> 
> - $\text{Ker}(\phi) = \left\{x\in R_1\,|\,\phi(x) = 0_{R_2}\right\}$
> - $\text{Im}(\phi) = \left\{\phi(x)\,|\,x\in R_1\right\}$

### 환의 준동형에 관한 명제

> **명제**. 전단사 사상 $\phi: R_1\to R_2$가 준동형사상이면,
> $\phi$는 동형사상이다.

> **명제**. $\phi:R_1\to R_2$가 준동형이라면, 다음이 성립한다.
> 
> 1. $\phi(0_{R_1}) = 0_{R_2}$
> 1. $\forall x\in R_1 \left[ \phi(-x) = -{\phi(x)}\right]$
> 1. $\forall n\in\Z \left[ \phi(n\cdot 1_{R_1}) = n\cdot 1_{R_2} \right]$

> **명제**. $\phi: R_1\to R_2$가 준동형이라면, $\text{Im}(\phi)$는
> $R_2$의 부분환이다.

> **명제**. $\phi: R_1\to R_2$가 준동형이라면, $\text{Ker}(\phi)$는
> $R_1$의 양쪽아이디얼이다.

> **명제**. 준동형사상 $\phi: R_1\to R_2$에 대하여 다음 두 조건은 동치이다.
>
> - $\phi$가 단사
> - $\text{Ker}(\phi) = \left\{ 0_{R_1} \right\}$

> **명제**. $R_2\neq \left\{ 0_{R_2} \right\}$이고, $\phi: R_1\to R_2$가 환의 준동형사상이라고
> 하면, 다음이 성립한다.
>
> 1. $R_1\neq \left\{ 0_{R_1} \right\}$
> 1. $u\in R_1^\times \implies \phi(u)\in R_2^\times$
>    이며, $\phi(u^{-1}) = \phi(u)^{-1}$
> 1. $R_1^\times\cap\text{Ker}(\phi) = \emptyset$
> 1. $1_{R_1}\notin \text{Ker}(\phi)$

### 환자기동형

> **정의**(환자기동형). 환 $R$에 대하여 동형사상 $\phi: R\to R$을
> $R$의 환자기동형이라고 한다. 또한, 환자기동형 전체의 집합을 $\text{Aut}(R)$로 쓴다.

> **명제**. 환 $R$에 대하여 다음이 성립한다.
>
> 1. $\text{id}_{R} \in \text{Aut}(R)$
> 1. $\phi, \psi \in \text{Aut}(R) \implies \phi\circ\psi\in\text{Aut}(R)$
> 1. $\phi \in \text{Aut}(R) \implies \phi^{-1}\in\text{Aut}(R)$

