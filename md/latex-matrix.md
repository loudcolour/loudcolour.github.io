<!---
title: "$\\LaTeX$에서 행렬 표시하기"
category: Typesetting
language: Korean
--->

# LaTeX에서 행렬 표시하기

$\LaTeX$을 사용한다면 `amsmath` 패키지를 불러와야 한다.
$\KaTeX$를 사용한다면 별도의 설정 없이 바로 행렬을 입력할 수 있다.

## `matrix`

$$
\begin{matrix}
   a & b \\
   c & d
\end{matrix}
$$

```latex
\begin{matrix}
   a & b \\
   c & d
\end{matrix}
```

## `pmatrix`

$$
\begin{pmatrix}
   a & b \\
   c & d
\end{pmatrix}
$$


```latex
\begin{pmatrix}
   a & b \\
   c & d
\end{pmatrix}
```

## `bmatrix`, `Bmatrix`

$$
\begin{bmatrix}
   a & b \\
   c & d
\end{bmatrix}
\begin{Bmatrix}
   a & b \\
   c & d
\end{Bmatrix}
$$


```latex
\begin{bmatrix}
   a & b \\
   c & d
\end{bmatrix}

\begin{Bmatrix}
   a & b \\
   c & d
\end{Bmatrix}
```

## `vmatrix`, `Vmatrix`

$$
\begin{vmatrix}
   a & b \\
   c & d
\end{vmatrix}
\begin{Vmatrix}
   a & b \\
   c & d
\end{Vmatrix}
$$

```latex
\begin{vmatrix}
   a & b \\
   c & d
\end{vmatrix}

\begin{Vmatrix}
   a & b \\
   c & d
\end{Vmatrix}
```

## 이외의 형식

`matrix` 형식으로 행렬을 불러온 뒤, 원하는 괄호에 `\left`와 `\rigth`를 덧붙여 행렬을
감싸도록 하는 것도 가능하다.

$$
\left\lceil
\begin{matrix}
a & b \\
c & d
\end{matrix}
\right\rceil

\left\langle
\begin{matrix}
a & b \\
c & d
\end{matrix}
\right\rangle
$$

```latex
\left\lceil
\begin{matrix}
a & b \\
c & d
\end{matrix}
\right\rceil

\left\langle
\begin{matrix}
a & b \\
c & d
\end{matrix}
\right\rangle
```

## 참고문헌

- [KaTeX, Supported Functions](https://katex.org/docs/supported.html)
- [Overleaf, Matrices](https://www.overleaf.com/learn/latex/Matrices)
