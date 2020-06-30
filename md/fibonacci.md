<!---
title: 'Fibonacci 수열'
language: Korean
category: Algebra
--->

# Fibonacci 수열

Fibonacci 수열은 이전의 두 항의 합이 다음 항과 같은 수열이다.
이 수열 $F_n$을 초항과 점화식을 이용하여 나타내면,
$F_0 = 0$, $F_1 = 1$에 $F_{n+2} - F_{n+1} - F_{n}=0$과 같이 나타내어진다.

## 선형점화식과 행렬

선형점화식이란 점화식의 각 요소가 선형합으로 구성되어있는 점화식이다.
따라서 Fibonacci 수열의 점화식 역시 선형점화식이다.
선형점화식을 구성하는 요소의 첨자중 가장 큰 첨자와 가장 작은 첨자의 차를 선형점화식의 크기라고 하면,
모든 선형점화식은 선형점화식의 크기를 행수로 하는 정방행렬에 대응한다.
행렬의 대각화 등을 이용하여 정방행렬의 거듭제곱을 구할 수 있으므로,
이를 응용하여 해당 선형점화식의 일반항을 구할 수 있다.
위에서 언급한 Fibonacci 수열의 점화식 역시 선형점화식이므로 이 방법을 이용할 수 있다.

구체적으로, 다음과 같은 선형변환을 정의하자.

$$ T_A:\R^2\to\R^2, \begin{bmatrix}F_{n+1}\\F_{n}\end{bmatrix}\mapsto\begin{bmatrix}F_{n+2}\\F_{n+1}\end{bmatrix} $$

이 선형변환에 대응하는 2차 행렬 $A$는 위에서 정의된 점화식에 의해,
$A=\begin{bmatrix}1 & 1 \\ 1 & 0\end{bmatrix}$임을 알 수 있다.

$$ \begin{bmatrix}F_{n}\\F_{n-1}\end{bmatrix}=T_A\left(\begin{bmatrix}F_{n-1}\\F_{n-2}\end{bmatrix}\right)=\cdots={T_A}^{n-1}\left(\begin{bmatrix}F_{1}\\F_{0}\end{bmatrix}\right) $$

위 식을 대응하는 행렬의 거듭제곱 형태로 변환하면,

$$ \begin{bmatrix}F_{n}\\F_{n-1}\end{bmatrix}={A}^{n-1}\begin{bmatrix}1\\0\end{bmatrix} $$

으로 나타내어진다. 실제로 이 행렬의 거듭제곱을 일반항으로 구하면,
Fibonacci 수열의 일반항을 유도할 수 있다.
실제로 구하여지는 일반항은 다음과 같다.

$$ \frac1{\sqrt5}\left(\left(\frac{1+\sqrt5}2\right)^n-\left(\frac{1-\sqrt5}2\right)^n\right) $$

## Python으로 구현

행렬의 거듭제곱에 재귀로 분할정복을 적용하면 Fibonacci 수열의 N번째 항을
$O(\log N)$에 구할 수 있다. Python으로 구현하면 다음과 같다.

```python
def mat_m(m_1,m_2):
    res_m = [m_1[0]*m_2[0]+m_1[1]*m_2[2],
             m_1[0]*m_2[1]+m_1[1]*m_2[3],
             m_1[2]*m_2[0]+m_1[3]*m_2[2],
             m_1[2]*m_2[1]+m_1[3]*m_2[3]]
    return res_m

def mat_pow(m,n):
    if n == 1:
        return m
    k = n // 2
    return mat_m(mat_pow(m,k),mat_pow(m,n-k))

def fib(n):
    mat_f = [1,1,1,0]
    return mat_pow(mat_f,n)[0]
```
