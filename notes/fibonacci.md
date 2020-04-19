<!---
title: '[Example NOTE] Fibonacci 수 구하기'
language: Korean
category: Algorithms
--->

## Fibonacci 수, 수열의 정의

Fibonacci 수열은 이전의 두 수의 합이 다음 수를 결정하는 수열으로, 이 수열 $F_n$을 초항과
점화식을 이용하여 나타내면,
$F_0 = 0$, $F_1 = 1$에 $F_{n+2} - F_{n+1} - F_{n}=0$로 나타내어진다.

## 선형점화식의 행렬화

모든 선형점화식은 행렬의 형태로 나타내어, 행렬의 거듭제곱을 통해 일반항을 구할 수 있다.
Fibonacci 수의 점화식 역시 선형점화식이므로 이 방법을 이용할 수 있다.

이를 위해서, 다음과 같은 선형변환을 생각하자.

$T_A:\R^2\to\R^2$,
$\begin{bmatrix}F_{n+1}\\F_{n}\end{bmatrix}\mapsto\begin{bmatrix}F_{n+2}\\F_{n+1}\end{bmatrix}$

이 선형변환에 대응하는 2차 행렬 $A$가 위에서 정의된 점화식에 의해,
$A=\begin{bmatrix}1 & 1 \\ 1 & 0\end{bmatrix}$임을 알 수 있다.

$\begin{bmatrix}F_{n}\\F_{n-1}\end{bmatrix}=T_A\left(\begin{bmatrix}F_{n-1}\\F_{n-2}\end{bmatrix}\right)=\cdots={T_A}^{n-1}\left(\begin{bmatrix}F_{1}\\F_{0}\end{bmatrix}\right)$

이고, 행렬의 거듭제곱 형태로 변환하면,

$\begin{bmatrix}F_{n}\\F_{n-1}\end{bmatrix}={A}^{n-1}\begin{bmatrix}1\\0\end{bmatrix}$

으로 나타내어진다. 실제로 이 행렬의 거듭제곱 꼴을 행렬의 대각화로 일반화하여,
Fibonacci 수열의 일반항을 유도할 수 있다.
실제로 구하여지는 일반항은 다음과 같다.

$\frac1{\sqrt5}\left(\left(\frac{1+\sqrt5}2\right)^n-\left(\frac{1-\sqrt5}2\right)^n\right)$

## Binary search를 통한 계산

위의 일반항을 계산하는 것은 신뢰성이 높은 컴퓨터 알고리즘으로 보기 어렵다.
실수의 곱셈에는 정밀도의 한계가 있으므로 적당히 큰 수에 대해서는
적용되기 어려움이 있고, 유리수의 확장환 계산을 통하여 계산하는 것도 가능하지만 사실 이는
행렬의 곱셈을 다시 구현하는 것과 상등하다.
조금 더 적용하기에 적합한 방식으로는,
행렬을 통해 거듭제곱이 가능한 대수 구조를 만들어 내었으므로, binary search를 통해
행렬의 거듭제곱을 구하는 것이 있다.
아래는 이 계산을 Python으로 구현한 것이다.

``` python
def mat_m(m_1,m_2):
    res_m = [m_1[0]*m_2[0]+m_1[1]*m_2[2],
             m_1[0]*m_2[1]+m_1[1]*m_2[3],
             m_1[2]*m_2[0]+m_1[3]*m_2[2],
             m_1[2]*m_2[1]+m_1[3]*m_2[3]]
    return res_m # matrix multiplication

def mat_pow(m,n):
    if n == 1:
        return m
    k = n // 2
    return mat_m(mat_pow(m,k),mat_pow(m,n-k)) # binary powering matrix

def fib(n):
    mat_f = [1,1,1,0]            # matrix form of linear recurrence relation
    return mat_pow(mat_f,n)[0]   # nth fibonacci number by O(log(n))
```
