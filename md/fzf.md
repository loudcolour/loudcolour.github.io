<!---
title: fzf
language: Korean
category: Linux
--->

# fzf

## 설치하기

Homebrew를 비롯한 여러 패키지 매니저를 이용하여 `fzf`를 설치할 수 있다.
터미널 상에서의 키 바인딩과 fuzzy completion을 이용하기 위해서는
아래의 설치 스크립트를 실행하여야 한다.

```
brew install fzf
$(brew --prefix)/opt/fzf/install
```

vim의 경우 `fzf` 플러그인을 Vim-Plug 등의 플러그인 매니저로 설치할 수 있다.
다음을 `.vimrc`에 추가하여 `:PlugInstall`을 실행하면 된다.

```
Plug 'junegunn/fzf', { 'do': { -> fzf#install()} }
Plug 'junegunn/fzf.vim'
```

플러그인의 설치와 업그레이드에 관한 자세한 정보는 [GitHub
저장소](https://github.com/junegunn/fzf#using-the-finder)를 참고.

## 사용하기

`fzf`는 인터랙티브 파인더를 불러와 STDIN으로 리스트를 불러들인 후 선택된 항목을
STDOUT으로 쓴다.  STDIN 파이프가 주어지지 않을 경우에는 자체적으로 (숨김처리
되지 않은) 파일의 리스트를 불러오기 위해 `find` 명령어를 사용한다.  `find`
이외의 명령어를 사용하기를 원한다면 `FZF_DEFAULT_COMMAND` 변수를 변경하여
설정할 수 있다. (`find` 대신 `fd`를 사용하는 경우 등.)

`find` (혹은 `fd`)를 기본 명령어를 사용하면 다음과 같은 명령어로 어떤 파일을
vim으로 편집할 지 선택하는 것도 가능하다.

```
vim $(fzf)
```

인터랙티브 파인더에서는 emacs-like 단축키를 사용할 수 있다.  항목을 선택하기
위해서는 `Enter` 를, 나가기 위해서는 `Ctrl-c`, `Ctrl-g` 중 어느 하나를 누르면
된다.  복수 선택을 원하는 경우, `-m` 옵션을 주어 실행하면 된다. 이 때는 `Tab`과
`Shift-Tab`을 이용하여 항목을 마킹하면 된다.  모두 선택하는 단축키는 `Meta-a`,
모두 선택해제하는 단축키는 `Meta-e`이다.  이외에도 마우스 동작을 이용하여
항목을 선택할 수도 있다.

별도로 지정되지 않는 한, `fzf`는 `extended-search mode` 로 실행된다.  공백으로
분리하여 검색 키워드를 지정할 수 있으며, 각각의 키워드에는 여러가지 토큰을
지정하여 특수한 매치를 얻을 수 있다. 예를 들어 `^`, `$`으로 줄의 prefix,
suffix를 매치하거나, `!`를 통해 부정에 해당하는 매치를 얻을 수 있다.
`exact-match`를 원하는 경우에도 `'` 토큰을 지정하여 매치를 얻을 수 있다.
(처음부터 `-e`, `--exact` 옵션을 지정하여도 된다.)

키워드 사이의 공백은 AND로 인식된다. OR을 원하는 경우에는 공백 사이에 `|`를
넣으면 된다.

## 단축키, fuzzy completion 사용하기

설치 스크립트에 의해서 설치된 `fzf`의 단축키를 쉘 상에서 사용할 수 있다.
스크립트를 통해 설치되는 단축키는 3가지로, 기본적으로 설정되어 있는 기능은 다음과 같다.

- `Ctrl-t`: fzf를 열어서, 선택된 파일, 디렉토리를 커맨드라인에 붙여넣기 한다.
- `Ctrl-r`: fzf를 열어서, 선택된 히스토리 상의 명령어를 커맨드라인에 붙여넣기 한다.
- `Meta-c`: 선택된 디렉토리로 들어간다.
	
fuzzy completion을 사용하기 위해서는, 명령어 뒤에 `**`을 커맨드라인에 입력 후
`Tab`키를 눌러 바로 fuzzy pattern을 입력할 수 있는 창을 활성화 시키면 된다.
`**Tab` 이외에도 `[디렉토리 경로]**Tab`을 입력 시, 해당 `[디렉토리]` 상의
파일 목록을 불러오며, `[fuzzy pattern]**Tab`을 입력하면 즉시 `[fuzzy pattern]`에
매치된 목록을 불러온다.

```
vim **[Tab]
vim ../**[Tab]
```

fuzzy completion을 사용할 수 있는 것은 파일과 디렉토리 뿐만이 아니다.
다음과 같이, 프로세스 ID, 호스트네임, 환경변수, 바로가기 등에서도 fuzzy completion을 사용할 수 있으며,
별도의 설정으로 작성한 completion API를 사용하는 것도 가능하다.

```
kill -9 [Tab]

ssh **[Tab]
telnet **[Tab]

unset **[Tab]
export **[Tab]
unalias **[Tab]
```

## `vim`과 연동하여 사용하기

`fzf`에서 지원하는 기능을 `vim`에서 사용할 수 있도록 플러그인이 마련되어 있다.
이를 설치하는 방법은 위에서 설명하였다.
더 자세한 설명은 [fzf의 공식 문서](https://github.com/junegunn/fzf/blob/master/README-VIM.md)
와 [fzf.vim의 공식 문서](https://github.com/junegunn/fzf.vim/blob/master/README.md)
에서 확인할 수 있다.

`fzf`의 `vim` 플러그인은 크게 두가지 코어 기능을 제공한다. 또한 이를 바탕으로 작성된 편리한
명령어 `:FZF`를 사용할 수 있게 한다.

1. `fzf#run([spec dict])`:  주어진 `[spec dict]`에 맞추어 `vim` 내에서 `fzf`를 실행한다.
	* `call fzf#run({'source': 'ls'})`
2. `fzf#wrap([spec dict]) -> (dict)`: 주어진 스펙을 전역 설정에서 지정된 추가 옵션을
덧붙여, 스펙을 생성한다. `fzf#run`을 실행과 함께 쓰인다.
	* `call fzf#run(fzf#wrap({'source': 'ls'}))`
3. `:FZF`: 기본적인 `fzf`를 이용한 파일 선택기이다. `fzf`의 옵션과 파일 검색의 디렉토리를
인자로 받는다.

특히 `:FZF`를 실행할 때, 파일을 여는 단축키 4가지는 다음과 같다.

- `Enter`: 현재 창에서 열기
- `Ctrl-t`: 새 탭에서 열기
- `Ctrl-x`: 수평 분할 창에서 열기
- `Ctrl-v`: 수직 분할 창에서 열기

별도의 설정 없이도 `:FZF`는 기본 쉘의 `fzf`와 같은 환경변수 설정(`$FZF_DEFAULT_COMMAND` 등)
을 공유한다.

`junegunn/fzf.vim` 플러그인에서는 `:FZF` 이외의 다양한 기능을 제공한다.

- `:Files [경로]`: `[경로]`의 파일을 `$FZF_DEFAULT_COMMAND`에서 정의된 파일 탐색기를 이용하여 표시한다.
- `:GFiles [옵션]`: `git` 상의 파일을 표시한다. (`git ls-files`)
- `:GFiles?`: `git status`를 표시한다.
- `:Buffers`: 버퍼를 표시한다.
- `:Colors`: 컬러스킴을 표시한다.
- `:Ag [패턴]`: `ag` 검색의 결과를 표시한다.
- `:Rg [패턴]`: `rg` 검색의 결과를 표시한다.

