<!---
title: "$\\KaTeX$ 적용하기"
category: Typesetting
language: Korean
--->

# $\KaTeX$ 적용하기

$\KaTeX$는 $\LaTeX$ 수식을 웹에서 표시할 수 있도록 하는 라이브러리이다.
Javascript를 실행할 수 있는 환경에서 사용가능하며, 별도의 의존성 패키지를
요구하지 않아 리소스를 추가하는 것만으로 적용할 수 있다.

[$\KaTeX$의 공식문서](https://katex.org/docs/browser.html)에서 아래와 같은 최신의 Starter template 코드를 찾아,
원하는 웹페이지에 적용하면 된다.

```html
<!DOCTYPE html>
<!-- KaTeX requires the use of the HTML5 doctype. Without it, KaTeX may not render properly -->
<html>
  <head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.11.1/dist/katex.min.css" integrity="sha384-zB1R0rpPzHqg7Kpt0Aljp8JPLqbXI3bhnPWROx27a9N0Ll6ZP/+DiW/UqRcLbRjq" crossorigin="anonymous">

    <!-- The loading of KaTeX is deferred to speed up page rendering -->
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.11.1/dist/katex.min.js" integrity="sha384-y23I5Q6l+B6vatafAwxRu/0oK/79VlbSz7Q9aiSZUvyWYIYsd+qj+o24G5ZU2zJz" crossorigin="anonymous"></script>

    <!-- To automatically render math in text elements, include the auto-render extension: -->
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.11.1/dist/contrib/auto-render.min.js" integrity="sha384-kWPLUVMOks5AQFrykwIup5lo0m3iMkkHrD0uJ4H5cjeGihAutqP0yW0J6dpFiVkI" crossorigin="anonymous"
        onload="renderMathInElement(document.body);"></script>
  </head>
  ...
</html>
```

`$`으로 싸여져 있는 수식을 렌더링하기를 원한다면 아래의 Javascript 설정을 추가하면 된다.

```javascript
let delimeters_settings = {
            delimiters: [
                {left: "&#36;&#36;", right: "&#36;&#36;", display: true},
                {left: "&#36;", right: "&#36;", display: false},
            ]
        };
```

설정을 마친 뒤, $\LaTeX$ 수식을 `$`로 감싸서
$\KaTeX$을 적용한 HTML 파일에 입력하면, 정상적으로
수식이 렌더링되어 있는 것을 확인할 수 있을 것이다.

## 참고문헌

- [KaTeX, Browser](https://katex.org/docs/browser.html)
