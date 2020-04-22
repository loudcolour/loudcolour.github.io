<!---
title: 'Basel 문제'
category: Mathematics
language: Korean
--->

# Basel 문제

Basel 문제는 Riemann의 $`\zeta`$ 함수 $`\zeta(s) = \sum_{k=1}^{\infty}\frac{1}{k^s}`$ 에 대하여
$`\zeta(2)`$의 값을 정확하게 닫힌 꼴로 구하는 문제이다.

## 이중적분과의 관계를 이용하는 풀이

### 단위 사각형 $`\square`$과 이중적분

간단히 쓰기 위해, $`\square`$는 $`\R^2`$의 부분집합인
$`[0,1]\times[0,1]`$을 의미하는 것으로 하자.
즉, $`\iint_{\square}f\,dxdy`$는 $`\int_{0}^{1}\int_{0}^{1}f\,dxdy`$와
같은 의미이다. 이 부분집합 내에서의 이중적분인,
$`\iint_{\square}\frac{dxdy}{1-xy}`$가 $`\zeta`$ 함수형의
급수꼴로 나타내어지는 것을 보이자.

먼저, $`|x|<1`$의 상황에서 $`\frac{1}{1-x} = \sum_{k=0}^{\infty}x^k`$ 꼴의
멱급수 전개를 적용하여

```math
\iint_{\square}\frac{dxdy}{1-xy}
= \iint_{\square}\sum_{k=0}^{\infty}x^ky^k\,dxdy
= \sum_{k=0}^{\infty}\iint_{\square}x^ky^k\,dxdy
= \sum_{k=0}^{\infty}\frac{1}{(k+1)^2}
= \sum_{k=1}^{\infty}\frac{1}{k^2}
```

$`\iint_{\square}\frac{dxdy}{1-xy} =\zeta(2)`$임을 보였다.
이와는 별개로 Dilogarithm 함수 $`\text{Li}_{2}(x)`$를 이용하는 방법도 고려할 수 있다.
$`\text{Li}_2(x)`$의 정의는 다음과 같다.

```math
    \text{Li}_2(x) = \int_{x}^{0}\frac{\ln (1-t)}{t}\,dt
```

이 때, $`\text{Li}_2(x)`$의 정의에 따라,
$`\iint_{\square}\frac{dxdy}{1-xy}`$를 $`y`$에 대해서 적분한 꼴이
$`-\int_{0}^{1}\frac{\ln(1-x)}{x}\,dx`$ 이므로,
$`\iint_{\square}\frac{dxdy}{1-xy} = \text{Li}_2(1)`$ 이 성립함을 알 수 있다.
$`|t|<1`$인 경우에 대해 $`-\ln(1-x)`$를 Taylor 전개한 결과는
$`-\ln(1-t) = \sum_{n=1}^{\infty}\frac{t^n}{n}`$ 이므로, $`\text{Li}_2(x)`$의 급수 전개는

```math
\text{Li}_2(x) = -\int_{0}^{x}\frac{\ln (1-t)}{t}\,dt
=\sum_{n=1}^{\infty}\int_{0}^{x}\frac{t^{n-1}}{n}\,dt
=\sum_{n=1}^{\infty}\frac{x^n}{n^2}
```

임을 알 수 있다. 결론적으로, $`\zeta(2) = \text{Li}_2(1)`$가 성립하고,
$`\iint_{\square}\frac{dxdy}{1-xy} =\zeta(2)`$ 임을 보였다.

### 다른 적분: 닫힌 값을 구할 수 있는 적분

위에서는 $`\iint_{\square}\frac{dxdy}{1-xy}`$ 꼴의 적분이 $`\zeta`$ 함수의 형태로
나타내어짐을 보였다. 이번에는 $`\zeta(2)=\frac{\pi^2}{6}`$이라는 결과를 비슷하지만 다른
형태의 적분을 도입하여 직접 도출할 것이다.
이를 위해, 실제로 닫힌 값을 구할 수 있고, $`\zeta(2)`$ 를 이용하여 결과를 나타낼 수 있는
적분을 고려한다. 이 경우, $`\iint_{\square}\frac{dxdy}{1-x^2y^2}`$를
적당한 적분으로 볼 수 있다.

먼저, 이 적분을 $`\zeta(2)`$를 이용하여 나타내어자. 전의 장에서
다루었던 적분 $`\iint_{\square}\frac{dxdy}{1-xy}`$를 이용하면,
$`\frac{2}{1-x^2y^2} = \frac{1}{1-xy}+\frac{1}{1+xy}`$
가 성립하므로,

```math
\iint_{\square}\frac{dxdy}{1-x^2y^2}
= \frac{1}{2}\left(\iint_{\square}\frac{dxdy}{1-xy}
+\iint_{\square}\frac{dxdy}{1+xy}\right)
```

또한,
$`\frac{2xy}{1-x^2y^2}=\frac{1}{1-xy}-\frac{1}{1+xy}`$
가 성립하므로, $`u=x^2`$, $`v=y^2`$으로 치환하면,

```math
    \iint_{\square}\frac{dxdy}{1-xy}
    - \iint_{\square}\frac{dxdy}{1+xy}
    = \iint_{\square}\frac{2xy\,dxdy}{1-x^2y^2}
    = \frac{1}{2}\iint_{\square}\frac{dudv}{1-uv}
    = \frac{1}{2}\iint_{\square}\frac{dxdy}{1-xy}
```

다시말해,

```math
    \frac{1}{2}\iint_{\square}\frac{dxdy}{1-xy}
    = \iint_{\square}\frac{dxdy}{1+xy}
```

이므로, 이 결과를 대입하면,

```math
    \iint_{\square}\frac{dxdy}{1-x^2y^2}
    = \frac{1}{2}\left(\iint_{\square}\frac{dxdy}{1-xy}
    +\iint_{\square}\frac{dxdy}{1+xy}\right)
    = \frac{3}{4}\iint_{\square}\frac{dxdy}{1-xy}
    = \frac{3}{4}\zeta(2)
```

이다. 즉, 이 적분의 결과는 $`\zeta(2)`$에 유리수를 곱한 값으로
나타난다.

그렇다면 이제 이 적분을 직접 계산함으로써 닫힌 값인 $`\frac{3}{4}\zeta(2)=\frac{\pi^2}{8}`$로
나타남을 보이자. $`\iint_{\square}\frac{dxdy}{1-xy}`$을
계산하기 위해 특수한 Jacobian을 도입하자.
$`x=\frac{\sin u}{\cos v}`$, $`y=\frac{\sin v}{\cos u}`$로 두면,

```math
    dxdy = \left|\frac{\partial(x,y)}{\partial(u,v)}\right|
    \,dudv
    = \begin{vmatrix}
        \frac{\cos u}{\cos v} & \frac{\sin u\cdot\sin v}{\cos^2 v}\\
        \frac{\sin u\cdot\sin v}{\cos^2 v}& \frac{\cos v}{\cos u}
    \end{vmatrix}\,dudv
    = |1-\tan^2 u\cdot\tan^2 v|\,dudv
```

이다. 적분 범위를 새로 지정하기 위해 변환 사상
$`\phi:(x,y)\mapsto(u,v)`$에 의한 상 $`\phi(\square)`$을 살펴보자.
$`\phi^{-1}`$가 삼각함수로 구성된 사상임을 고려하면, $`\phi`$가
well-definend이기 위해서는 $`\phi(\square)\subset[0,\frac{\pi}{2}]\times[0,\frac{\pi}{2}]`$ 을 만족하는 것으로 충분하다. 또한, $`0\leq xy=\tan u\cdot\tan v\leq 1`$ 이므로,
$`\tan u\leq\frac{1}{\tan v}=\tan\left(\frac{\pi}{2}-v\right)`$, $`\tan`$가
단조증가함수임에 따라 $`u+v\leq\frac{\pi}{2}`$가 성립한다. 결론적으로
새 적분범위는 $`\phi(\square) = \left\{(u,v)\,|\,0\leq u,v\leq\frac{\pi}{2},\,u+v\leq\frac{\pi}{2}\right\}`$ 임을 알 수 있다.
적분을 계산하면,

```math
    \iint_{\square}\frac{dxdy}{1-x^2y^2}
    =\iint_{\phi(\square)}\frac{|1-x^2y^2|\,dudv}{1-x^2y^2}
    =\iint_{\phi(\square)}dudv
    =\frac{\pi^2}{8}
```

위에서 구한 적분의 결과에 따라,
$`\frac{3}{4}\zeta(2) = \frac{\pi^2}{8}`$, 즉 $`\zeta(2)=\frac{\pi^2}{6}`$이다.

### 같은 결과에 도달하는 다른 방법: 급수를 조작하기

위에서는 $`\iint_{\square}\frac{dxdy}{1-x^2y^2}`$의 적분값을
직접 구하여 그것이 $`\zeta`$ 함수를 통해 나타내어진 꼴과 같음을 보였다.
이 식을 유도하는 또 다른 방법이 존재한다.
단순한 적분을 통해,

```math
    \iint_{\square}\frac{dxdy}{1-x^2y^2}
    = \int_{0}^{1}\frac{\tanh^{-1}(y)}{y}\,dy
    = \sum_{k=0}^{\infty}\int_{0}^{1}\frac{y^{2k}}{2k+1}\,dy
    = \sum_{k=0}^{\infty}\frac{1}{(2k+1)^2}
```

을 구할 수 있다. 이 때, 급수의 꼴에 주목하면,

```math
\begin{aligned}
    \sum_{k=0}^{\infty}\frac{1}{(2k+1)^2}
    &= \frac{1}{1^2} + \frac{1}{3^2} + \frac{1}{5^2} + \cdots \\
    &= \left(\frac{1}{1^2} + \frac{1}{2^2}
    + \frac{1}{3^2} + \cdots\right)
    - \left(\frac{1}{2^2} + \frac{1}{4^2}
    + \frac{1}{6^2} + \cdots\right) \\
    &= \zeta(2) - \frac{1}{2^2}\zeta(2) = \frac{3}{4}\zeta(2)
\end{aligned}
```

임을 쉽게 알아낼 수 있다.
