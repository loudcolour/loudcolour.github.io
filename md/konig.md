<!---
title: Kőnig의 보조정리
category: Graph Theory
language: Korean
--->

# Kőnig의 보조정리

> **정리**(Kőnig의 보조정리). 국소유한인 무한연결그래프는 무한단순경로를 갖는다.

*증명*. $\textsf{DC}$를 필요로 한다.

$G = (V, E)$를 국소유한인 무한연결그래프로 두자.
여기서 한 꼭짓점 $v_0\in V$을 고정하자.
$G$는 연결그래프이므로, 임의의 $v\in V$에 대하여, $v_0$와
$v$를 잇는 경로가 존재한다. 그 경로 전체의 집합을 $P(v)$라고 하면, 경로의 정의에 따라
함수 $f: P(v)\to\N$을 $f(p)$가 $p$를 구성하는 모서리의 갯수가 되도록 정의할 수 있다.
$ \left\{ f(p) \,|\, p\in P(v) \right\}\subset\N$이므로,
$\min \left\{ f(p) \,|\, p\in P(v) \right\}$가 존재하고, 이를 $d(v)$라고 하자.
단, $d(v_0) = 0$으로 한다.

이 때, $T_n = \left\{ v\in V\,|\, d(v) = n \right\}$으로 두자.

- $v\in T_n$이고 $v$와 인접한 $v'$에 대하여,
$d(v')> n$이라면, $d(v') = n+1$이다. 이는 간단하게 $d(v')> n+1$인
인접꼭짓점 $v'$가 존재한다고 가정하면, $v$에서 $v'$로는 하나의 모서리를 통하여
이동할 수 있기 때문에 $d(v')\leq d(v)+1 = n+1$이게 되어 모순임을 알 수 있기 때문이다.
- 마찬가지로, $v\in T_n$과 인접한 $v'$에 대하여 $d(v') < n$이라면, $d(v') = n - 1$이다.
- $\bigcup_{n\in\N} T_n = V$이다.
$\bigcup_{n\in\N} T_n \subset V$는 자명. 어떠한 $v\in V$에 대해서도,
$v\in T_{d(v)} \subset \bigcup_{n\in\N} T_n$이므로, $\bigcup_{n\in\N} T_n \supset V$.
- 모든 $n\in\N$에 대하여 $T_n$은 유한집합이다.
이는 귀납법을 통하여 보일 수 있다.
$T_0$, $T_1$은 $G$의 국소유한성에 의하여 유한집합이다.
또한, $T_k$가 유한집합이라고 가정하자. 그렇다면, $T_k$의 인접꼭짓점의 집합
$\text{Adj}(T_k)$ 또한 유한집합이다. 어떠한 $T_{k+1}$의 원소에 대해서도,
인접한 $T_k$의 원소가 존재하여, $T_{k+1}\subset\text{Adj}(T_k)$ 일것이므로,
$T_{k+1}$또한 유한집합이다.
- 모든 $n\in\N$에 대하여 $T_n\neq\emptyset$이다.
만약, 어떤 $n_0\in\N$에 대하여 $T_{n_0}=\emptyset$이라고 가정한다면,
$T_{n_0+1}\subset\text{Adj}(T_{n_0}) = \emptyset$이므로, $T_{n_0+1}=\emptyset$이다.
그렇다면, 모든 $n\geq n_0$에 대하여 $T_{n} = \emptyset$이고,
$V = \bigcup_{n\in\N} T_n= \bigcup_{n=0}^{n_0-1} T_n$, $V$가 유한집합이므로,
이는 $G$가 무한그래프임에 모순이다.

여기서, $v_1,v_2\in V$에 대하여 $v_1$와 $v_2$가 인접하고, $v_1\in T_n$, $v_2\in T_{n+1}$인
$n\in \N$이 존재할 때, $V$ 상의 이항관계 $v_1\sim v_2$가 성립한다고 정의하자.
또한, $v_1\in V$에 대하여

$$
I(v_1) = \left\{ v_1 \right\} \cup
\left\{ v\in V \,|\, \exists n\in \N_{\geq 2}, \exists \left\{ s_i \right\}_{i=1}^{n} \subset V \left[
s_1\sim s_2, \ldots , s_{n-1}\sim s_n
\land \left( s_1 = v_1\right) \land \left(s_n = v\right)
\right] \right\}
$$

라고 할 때,
$V' = \left\{ v\in V \,|\, |I(v)| = \infty \right\}$로 두자.
여기서 $\sim$의 $V'$에 대한 제한을 $\sim'$으로 두면,
임의의 $x\in V'$에 대하여 $y\in V'$이 존재하여 $x\sim' y$이 성립한다.
($\because$ $T = \left\{ y\in V \,|\, x\sim y \right\}$라고 하면,
$I(x) = \bigcup_{y\in T}I(y)$ 임을 쉽게 확인할 수 있다.
만약, $y \in T$ 중에서, $y\in V'$인 것이 존재하지 않는다고 가정하면,
모든 $y\in T$에 대하여 $|I(y)|<\infty$이고, $T\subset \text{Adj}(x)$이므로
$T$ 또한 유한집합, 따라서 $|I(x)| = |\bigcup_{y\in T}I(y)| < \infty$, 이는 $x\in V'$에 모순이다.)

$\textsf{DC}$에 의하여, 임의의 $i\in\N$에 대하여 $v_{i}'\sim' v_{i+1}'$인
$ \left\{ v_{i}' \right\}_{i = 1}^{\infty}\subset V'$를 얻는다.
$v_{i}'\sim' v_{i+1}'$이므로, 각 $i\in\N$에 대하여 $v_{i}'$와 $v_{i+1}'$은
인접, $v_{1}'\in T_{k}$이면, 각 $i\in\N$에 대하여 $v_{i}\in T_{k+i-1}$임을
알 수 있으므로, 열 $ \left\{ v_{i}' \right\}_{i = 1}^{\infty}\subset V'$는
단순무한경로를 구성하고 있음을 알 수 있다. □

