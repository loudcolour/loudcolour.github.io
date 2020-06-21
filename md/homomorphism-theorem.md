<!---
title: "준동형, 동형정리"
category: Mathematics
language: Korean
--->

# 준동형, 동형정리

## 준비

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

## 환의 준동형정리
