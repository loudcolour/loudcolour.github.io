<!---
title: "PGF/TikZ"
language: Korean
category: Typesetting
--->

# PGF/TikZ

TikZ(TikZ ist kein Zeichenprogramm)은 PGF(Portable Graphics Format)를 이용하여
$\LaTeX$ 상에서 도식을 쉽게 그릴 수 있도록하는 패키지이다.
`\usepackage{tikz}`를 preamble에 두어 `tikz` 패키지를 사용할 수 있다.  또한
`\usetikzlibrary{ [TikZ 패키지] }` 명령어를 통해 추가적인 TikZ 패키지를
사용하도록 할 수 있다.
(`arrows`, `automata`, `calendar`, `chains`, `mindmap` 등)

## 기본

```latex
\begin{tikzpicture}[ [옵션] ] 
[TikZ 명령어]
\end{tikzpicture}
```

이나, 단순히 `\tikz[ [옵션] ]{ [TikZ 명령어] }`를 통해,
TikZ 명령어를 입력할 환경을 만들 수 있다.

TikZ 명령어에서 사용하는 좌표는 직교좌표와 극좌표를 모두 사용할 수 있다.
직교좌표는 `(1cm,2pt)`과 같이 `,`로 구분하여 숫자와 $\LaTeX$에서 사용되는
단위를 표시하면 된다. 극좌표는 `(45:1cm)`와 같이 `:`로 구분하여 도단위의
각도도와 직교좌표계에서와 같은 길이 단위를 표시하면 된다.  위의 직교좌표에서
단위를 표시하지 않으면, 기본단위인 `cm`을 사용하는 것으로 인식한다.

위 문단과 같은 절대좌표 이외에도 바로 이전에 사용한 좌표로부터의 상대좌표를 이용할 수도 있다.
예를 들어 바로 이전에 사용한 좌표를 원점으로 하여 `(1,0)`의 위치를 표시하고 싶다면
`++(1,0)`으로 나타내면 된다.


## 가환도식


## 참고문헌

- [공식 매뉴얼(PDF)](http://mirror.ctan.org/graphics/pgf/base/doc/pgfmanual.pdf)
- [CTAN, PGF TikZ Topic](https://www.ctan.org/topic/pgf-tikz)
- [Wikibooks, LaTeX/PGF/TikZ](https://en.wikibooks.org/wiki/LaTeX/PGF/TikZ)
- [TeXample.net, TikZ and PGF](http://www.texample.net/tikz/)

