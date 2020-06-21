<!---
title: "준동형, 동형정리"
category: Mathematics
language: Korean
--->

# 준동형, 동형정리

## 고찰

> **명제**. $\sim$을 집합 $X$상의 동치관계, $\pi: X\to X/\sim$을 자연스러운 전사라고 할 때,
> $f: X \to Y$에 대하여 다음 두 조건은 동치이다.
>
> 1. $\exists! g\in \text{Map}(X/\sim, Y) \left[ f = g\circ \pi \right]$
> 2. $x_1, x_2\in X\left[x_1\sim x_2 \implies f(x_1) = f(x_2)\right]$

*증명*.

**1에서 2를 유도**  
각 $x_1, x_2\in X$에 대하여 $x_1\sim x_2$라면 $\pi(x_1) = \pi(x_2)$이다. 따라서
$f(x_1) = g(\pi(x_1)) = g(\pi(x_2)) = f(x_2)$

**2에서 1을 유도**  
$\pi(x) = \pi(y)$이면, $f(x) = f(y)$라고 하자. $\pi$의 전사성으로부터,
$X/\sim$의 각 원소를 $\pi(a)$와 같이 나타낼 수 있고,
$g: X/\sim \to Y, \pi(a)\mapsto f(a)$와 같이 정의하면 2의 가정에 따라 $g$가
well-defined인 사상임을 확인 할 수 있다. 여기서 임의의 $x$에 대하여
$f(x) = g(\pi(x))$가 성립하므로 1의 조건에서의 존재성을 보였다.

$g$ 이외에 1을 만족하는 사상 $h$가 존재한다고 하면,
$g\circ \pi = f = h\circ\pi$ 이므로, 임의의 $x$에 대하여 $g(\pi(x)) = h(\pi(x))$,
$\pi$의 전사성에 의하여 $\pi(X) = X/\sim$이므로, $g = h$가 성립함을 알 수 있다.
따라서 $g$의 unique함을 보였다. □

*주*. 실제로 어떤 관계 $\sim$를 $x_1\sim x_2 \iff f(x_1) = f(x_2)$같이 정의한다면,
$\sim$은 동치관계임을 바로 확인할 수 있고, 위 명제에 의하여 $f = g\circ\pi$를
만족하는 $g$또한 존재한다. 특히, $f$가 전사인 사상이라면,
$g$는 전단사이다. ($\because$ $f = g\circ\pi$가 전사이므로, $g$는 전사.
$g(p_1) = g(p_2)$라고 가정하면, $p_1 = \pi(x_1), p_2 = \pi(x_2)$를 만족하는 $x_1, x_2$가
존재하여, $f(x_1) = g(\pi(x_1)) = g(p_1) = g(p_2) = g(\pi(x_2)) = f(x_2)$, $x_1\sim x_2$이다.
따라서, $p_1 = \pi(x_1) = \pi(x_2) = p_2$, $g$는 단사.)

## 군의 준동형정리

위의 고찰을 바탕으로, 군의 부분군에 의한 동치관계에서, 몫집합을
얻어 새로운 사상을 유도하는 과정을 생각하자. 고찰한 내용에 따르면,
새로운 사상을 유도하기 위하여 필요(충분)한 조건은,
동치관계에 있는 두 원소 $x_1, x_2$에 대하여
$f(x_1) = f(x_2)$인 사상이 주어지는 것이다.
준동형사상 $\phi$와 부분군 $\text{Ker}(\phi)$이 주어진다면 이 조건을 만족할 수 있다는
아이디어로부터, 다음 정리가 얻어진다.

> **정리**(준동형정리).
> $\phi: G\to H$를 군의 준동형이라고 하자. $\pi: G\to G/\text{Ker}(\phi)$를
> 자연스러운 준동형이라고 할 때, $\phi = \psi\circ\pi$를 만족하는 준동형
> $\psi: G/\text{Ker}(\phi) \to H$가 유일하게 존재한다.
> 또한, $\psi$에 의하여 $G/\text{Ker}(\phi)\simeq \text{Im}(\phi)$이다.

*증명*. $N = \text{Ker}(\phi)$로 두자. $\psi(gN) = \phi(g)$와 같이 정의하면,
$\psi$가 well-defined인 사상임을 먼저 보이자.
$gN = g'N$ 인 경우, $\psi(gN) = \psi(g'N)$이 성립하는 것을 보이면 된다.
$gN = g'N$이므로, $g'\in gN$, $g^{-1}g'\in N$임을 알 수 있다.
따라서 $\phi(g^{-1}g') = 1_H$이고,
$\psi(gN) = \phi(g) = \phi(g)\phi(g^{-1}g') = \phi(g') = \psi(g'N)$,
$\psi$가 well-defined임이 보여진다.
이 $\psi$는 $\phi=\psi\circ\pi$를 만족하는 동시에, 고찰에서와 같은 이유로, unique하게
존재함을 알 수 있다.

다음으로, $\psi$가 준동형임을 보이자.
$g_1,g_2\in G$에 대하여,
$\psi((g_1N)(g_2N)) = \psi(g_1g_2N) = \phi(g_1g_2) = \phi(g_1)\phi(g_2) = \psi(g_1N)\psi(g_2N)$
이므로, $\psi$는 준동형이다.

마지막으로, $\psi$에 의하여, $G/\text{Ker}(\phi) \simeq \text{Im}(\phi)$이 성립함을 보이자.
우선, $\psi$가 단사임을 확인하자.
$\psi(gN) = 1_H$이라고 할 때, $\phi(g) = \psi(gN) = 1_H$이므로, $g\in \text{Ker}(\phi) = N$,
$gN = N = 1_{G/N}$이 성립함을 알 수 있다. 따라서 $\psi$는 단사.
다음으로, $\psi(G/\text{Ker}(\phi)) = \text{Im}(\psi) = \text{Im}(\phi)$임을 보이자.
$g\in G$에 대하여, $\phi(g) = \psi(gN) \in \text{Im}(\psi)$이므로
$\text{Im}(\phi)\subset\text{Im}(\psi)$임은 분명하다.
반대로, 임의의 $G/N$의 원소는 어떤 $g\in G$가 존재하여 $gN$의 꼴로 나타내어지므로,
$\psi(gN) = \phi(g)\in \text{Im}(\phi)$, $\text{Im}(\psi)\subset\text{Im}(\phi)$,
따라서, $\text{Im}(\psi)=\text{Im}(\phi)$가 성립한다. 이상을 정리하면
$G/\text{Ker}(\phi) \simeq \text{Im}(\phi)$ □

*주*. 군 $G$와 그 부분군 $N$이 주어졌을 때, 자연스러운 준동형 $\pi: G\to G/N$ 역시
준동형이므로, 준동형정리가 성립한다. 그 결과는 당연하게도,
$\text{Im}(\pi) = G/N$, $\text{Ker}(\pi) = N$에 의하여
$G/\text{Ker}(\pi) = G/N \simeq G/N = \text{Im}(\pi)$

*예*. 준동형사상 $\det:\text{GL}_n(\R)\to \R^{\times}$이 주어졌을 때,
$\text{Im}(\det) = \R^{\times}$, $\text{Ker}(\det) = \text{SL}_n(\R)$과
준동형정리에 따라, $\text{GL}_n(\R)/\text{SL}_n(\R) \simeq \R^{\times}$ 임을 알 수 있다.

## 환의 준동형정리
