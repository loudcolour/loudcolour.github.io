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
준동형사상 $\phi$와 (정규)부분군 $\text{Ker}(\phi)$이 주어진다면 이 조건을 만족할 수 있다는
아이디어로부터, 다음 정리가 얻어진다.

> **정리**(준동형정리).
> $\phi: G\to H$를 군의 준동형이라고 하자. $\pi: G\to G/\text{Ker}(\phi)$를
> 자연스러운 준동형이라고 할 때, $\phi = \psi\circ\pi$를 만족하는 준동형
> $\psi: G/\text{Ker}(\phi) \to H$가 유일하게 존재한다.
> 또한, $\psi$에 의하여 $G/\text{Ker}(\phi)\cong \text{Im}(\phi)$이다.

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

마지막으로, $\psi$에 의하여, $G/\text{Ker}(\phi) \cong \text{Im}(\phi)$이 성립함을 보이자.
우선, $\psi$가 단사임을 확인하자.
$\psi(gN) = 1_H$이라고 할 때, $\phi(g) = \psi(gN) = 1_H$이므로, $g\in \text{Ker}(\phi) = N$,
$gN = N = 1_{G/N}$이 성립함을 알 수 있다. 따라서 $\psi$는 단사.
다음으로, $\psi(G/\text{Ker}(\phi)) = \text{Im}(\psi) = \text{Im}(\phi)$임을 보이자.
$g\in G$에 대하여, $\phi(g) = \psi(gN) \in \text{Im}(\psi)$이므로
$\text{Im}(\phi)\subset\text{Im}(\psi)$임은 분명하다.
반대로, 임의의 $G/N$의 원소는 어떤 $g\in G$가 존재하여 $gN$의 꼴로 나타내어지므로,
$\psi(gN) = \phi(g)\in \text{Im}(\phi)$, $\text{Im}(\psi)\subset\text{Im}(\phi)$,
따라서, $\text{Im}(\psi)=\text{Im}(\phi)$가 성립한다. 이상을 정리하면
$G/\text{Ker}(\phi) \cong \text{Im}(\phi)$ □

*주*. 군 $G$와 그 부분군 $N$이 주어졌을 때, 자연스러운 준동형 $\pi: G\to G/N$ 역시
준동형이므로, 준동형정리가 성립한다. 그 결과는 당연하게도,
$\text{Im}(\pi) = G/N$, $\text{Ker}(\pi) = N$에 의하여
$G/\text{Ker}(\pi) = G/N \cong G/N = \text{Im}(\pi)$

*예*. 준동형사상 $\det:\text{GL}_n(\R)\to \R^{\times}$이 주어졌을 때,
$\text{Im}(\det) = \R^{\times}$, $\text{Ker}(\det) = \text{SL}_n(\R)$과
준동형정리에 따라, $\text{GL}_n(\R)/\text{SL}_n(\R) \cong \R^{\times}$ 임을 알 수 있다.

> **정리**(부분군의 대응). $N$을 군 $G$의 정규부분군이라고 하자.
> $\pi: G\to G/N$을 자연스러운 준동형, $X$를 $G/N$의 부분군의 집합,
> $Y$를 $N$을 포함하는 $G$의 부분군 전체의 집합이라고 두면, 다음 두 사상
> $\phi$와 $\psi$가 존재하며,
>
> - $\phi: X \ni H \mapsto \pi^{-1}(H) \in Y$
> - $\psi: Y \ni K \mapsto \pi(K) \in X$
> 
> $\phi$와 $\psi$는 서로의 역사상이다. 따라서 $X$와 $Y$간에는 일대일 대응이 존재한다.

*증명*. $H\in X$의 $\pi$에 의한 역상 $\pi^{-1}(H)$는 어떠한 형태로도 존재함을 알 수 있으므로,
**$\phi$가 well-defined임** 을 보이기 위해서는 $\pi^{-1}(H)\in Y$임을 보이는 것만으로도 충분하다.
즉, $G/N$의 부분군인 $H$에 대하여 $\pi^{-1}(H)$이 $G$의 부분군이며, 동시에 $N$을 포함하는 것을 보이면
된다.

- $N\subset\pi^{-1}(H)$을 보이는 것은 간단하다. $H\in X$이므로, $ \left\{ 1_{G/N} \right\} \subset H$이고,
$\pi^{-1}\left( \left\{ 1_{G/N} \right\}\right) \subset \pi^{-1}(H)$이다. 여기서 $\pi$의 정의에 따라
$\pi^{-1}\left(\left\{ 1_{G/N}\right\}\right) = N$이므로, $N\subset \pi^{-1}(H)$.
- $\pi^{-1}(H)$는 아래의 조건을 만족하므로 $G$의 부분군이다.
	* $1_G = 1_N\in N \subset \pi^{-1}(H)$.
	* $x,y \in \pi^{-1}(H)$라고 하면, $\pi(x), \pi(y)\in H$, $\pi(xy)=\pi(x)\pi(y)\in H$이므로,
	  $xy\in \pi^{-1}(H)$.
	* $x\in \pi^{-1}(H)$라고 하면, $\pi(x)\in H$, $\pi(x^{-1}) = \pi(x)^{-1}\in H$이므로,
	  $x^{-1}\in \pi^{-1}(H)$.

따라서 $\pi^{-1}(H) \in Y$, $\phi$는 well-defined이다.

다음으로, **$\psi$가 well-defined** 인 사상임을 보이자.
$\phi$와 마찬가지로, 군 $G$의 $N$을 포함하는 부분군 $K\subset G$에 대하여
$\pi(K)\in X$, 즉 $\pi(K)$가 $G/N$의 부분군임을 보이면 된다.
$N$은 정규부분군이므로, 임의의 $g\in G$에 대하여 $gNg^{-1}\subset N$이 성립한다.
따라서 임의의 $g\in K$에 대해서도 이가 성립할 것이므로, $K \vartriangleright N$.
$K/N$은 $g\in K$인 $gN$의 집합이므로, $K/N\subset G/N$인 동시에,
$\pi(K) = \left\{ gN \,|\, g\in K \right\} = K/N$이다. $\pi(K) = K/N$이 정규부분군 $N$에
의하여 잉여군의 구조를 갖는
것으로부터 $\pi(K)$는 $G/N$의 부분군이라는 것을 알 수 있으므로, $\pi(K)\in X$. 따라서
$\psi$는 well-defined인 사상이다.

마지막으로, **$\phi$와 $\psi$가 서로의 역사상** 임을 보이자.

- 임의의 $H\in X$에 대하여 $(\psi\circ\phi)(H) = H$. 즉 $\pi(\pi^{-1}(H)) = H$.
	* $\pi(\pi^{-1}(H))\subset H$: [집합의 기본 성질](./zfc.html#사상에-의한-상과-역상)로부터 분명.
	* $\pi(\pi^{-1}(H))\supset H$: $h\in H$라고 하자. $\pi$의 전사성에 의하여,
	  $h=\pi(g)$를 만족하는 $g\in G$가 존재한다. 따라서 $\pi(g)\in H$, $g\in \pi^{-1}(H)$이다.
	  따라서 $h = \pi(g) \in \pi(\pi^{-1}(H))$.
- 임의의 $K\in Y$에 대하여 $(\phi\circ\psi)(K) = K$. 즉 $K = \pi^{-1}(\pi(K))$.
	* $K\subset \pi^{-1}(\pi(K))$: [집합의 기본 성질](./zfc.html#사상에-의한-상과-역상)로부터 분명.
	* $K\supset \pi^{-1}(\pi(K))$: $g\in\pi^{-1}(\pi(K))$라고 하자.
	  그렇다면, $\pi(g)\in\pi(K)$이고, $\pi(g) = \pi(k)$인 $k\in K$가 존재하게 된다.
	  이는 $gN = kN$을 의미하고, $g=kn$인 $n\in N \subset K$가 존재함을 의미한다.
	  따라서 $g\in K$. □

> **정리**(제2동형정리). $H, N$을 군 $G$의 부분군, 특히 $N \vartriangleleft G$라고 하자. 이 때, 다음 사실이 성립한다.
>
> 1. $HN = NH$이다.
> 1. $HN$은 $G$의 부분군이다.
> 1. $H\cap N \vartriangleleft H$, $N\vartriangleleft HN$
> 1. $H/H\cap N\cong HN/N $

*증명*.

1. 임의의 $h\in H$에 대하여 $hN=Nh$이므로 $HN=NH$.
2. $HN$이 부분군의 조건을 만족하는지 확인한다.
	* $1_G = 1_G1_G \in HN$
	* $h_1, h_2\in H$, $n_1, n_2\in N$에 대하여, $N$이 정규부분군이므로 $h_1n_1h_2n_2 \in h_1Nh_2N = h_1h_2NN\subset HN$
	* $h\in H$, $n\in N$에 대하여, $(hn)^{-1}= n^{-1}h^{-1}\in NH = HN$
3. $H\cap N$이 $H$의 부분군, $N$이 $HN$의 부분군이라는 것은 알기 쉽다. 이들이 정규부분군임을 보이자.
	* $H\cap N \vartriangleleft H$:  
	  $\forall h\in H, \forall n\in H \left[ hnh^{-1}\in H \right]$이고,
	  $\forall h\in H\subset G, \forall n\in N \left[ hnh^{-1}\in N \right]$ 이므로,
	  $\forall h\in H, \forall n\in H\cap N \left[ hnh^{-1}\in H\cap N \right]$
	* $N \vartriangleleft HN$:  
	  $N$은 $G$의 정규부분군이므로, $\forall g\in HN \subset G, \forall n\in N \left[ gng^{-1} \in N \right]$
4. 3의 결과에 의하여 $H/H\cap N$과 $HN/N$은 군을 이룬다.
   이 때, $i: H\to HN, h\mapsto h$, $\pi: HN\to HN/N, hn\mapsto hnN = hN$을 이용하여,
   사상 $\phi = \pi\circ i$을 구축하면, $i$와 $\pi$ 모두 준동형사상이므로, $\phi: H\to HN/N$역시 준동형사상이다.
    * 임의의 $hnN = hN\in HN/N$에 대하여, $h\in H$, $\phi(h) = hnN$이므로, $\phi$는 전사이다.
      따라서 $\text{Im}(\phi) = HN/N$.
    * $x\in H\cap N$이면 $\phi(x) = xN = N$, 따라서 $x\in \text{Ker}(\phi)$이므로 $H\cap N \subset \text{Ker}(\phi)$.
      역으로 $x\in \text{Ker}(\phi)$라고 하면, $xN = \phi(x) = N$. 따라서 $x\in N$이고, $x\in H$는 분명하므로,
      $x\in H\cap N$, $\text{Ker}(\phi)\subset H\cap N$ 이므로, $\text{Ker}(\phi) = H\cap N$

   준동형정리에 의하여, $H/H\cap N = H/\text{Ker}(\phi) \cong \text{Im}(\phi) = HN/N$. □

*예*. $G = \Z$, $H = m\Z$, $N = n\Z$로 두자.
우선 $H$와 $N$ 모두 가환군의 부분군이므로 정규부분군이다.
따라서 제2동형정리를 이용하면 $G = \gcd(m,n)$, $L = \text{lcm}(m,n)$으로 하여
$m\Z/L\Z = H/H\cap N \cong HN / N = G\Z/n\Z$이 성립하는 것을 알 수 있다.

> **정리**(제3동형정리).
> 군 $G$에 대하여, $H\vartriangleleft G$, $N\vartriangleleft G$,
> $H\subset N$이라면, $ \left( G/N \right)/ \left( H/N \right) \cong G/H$

*증명*.
사상 $\phi: G/N \ni gN \mapsto gH \in G/H$ 가 well-defined인 사상임을 보이도록 하자.
모든 $G/N$의 원소는 $gN$, $g\in G$의 형태를 하고 있으므로, 다른 $g'\in G$에 대하여
$gN = g'N$일 때에도 $\phi(gN) = \phi(g'N)$이 성립하는지를 확인하면 된다.
만약 $gN=g'N$이라면, $g^{-1}g'\in N\subset H$임을 알 수 있으므로,
$\phi(gN) = gH = g'H = \phi(g'N)$이 성립, $\phi$는 well-defined이다.

다음으로, $\phi$가 준동형이라는 것을 보이자.
$g_1, g_2\in G$,
$g_1N, g_2N\in G/N$에 대하여,
$\phi((g_1N)(g_2N)) = \phi(g_1g_2N) = g_1g_2H = (g_1H)(g_2H) = \phi(g_1N)\phi(g_2N)$
이므로 $\phi$는 준동형이다.

이 때, 임의의 $X \in G/H$에 대하여 $\exists g\in G \left[ X = gH \right]$이므로,
$gN\in G/N$이 존재하여
$\phi(gN) = gH = X$이다. 따라서 $\text{Im}(\phi) = G/H$.

또한, $h\in H$, $hN\in H/N$에 대하여 $\phi(hN) = hH = H$이므로, $hN\in \text{Ker}(\phi)$
이고 $H/N \subset \text{Ker}(\phi)$.
$g\in G$, $gN\in \text{Ker}(\phi)$라고 하면 $gH = \phi(gN) = H$이므로
$g\in H$이고 $gN\in H/N$, 따라서 $H/N \supset \text{Ker}(\phi)$, $\text{Ker}(\phi) = H/N$이다.

준동형정리에 따르면,
$(G/N)/(H/N) = (G/N)/ \text{Ker}(\phi) \cong \text{Im}(\phi) = G/H$이다. □

*예*. 제3동형정리에 의하면, $(\Z/12\Z)/(3\Z/12\Z)\cong \Z/3\Z$ 임을 쉽게 확인할
수 있다.

## 환의 준동형정리
