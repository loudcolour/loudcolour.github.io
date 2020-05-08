<!---
title: 'GnuPG 고급편'
category: Security
language: Korean
--->

# GnuPG 고급편

[GnuPG 실전편](https://loudcolour.github.io/notes/practical_gnupg.html)에서는
GnuPG를 설치하고 사용하는 방법에 대해서 다루었습니다.
GnuPG 고급편에서는 GnuPG를 더 편리한 방법으로 사용하고,
더 다양한 상황에서 활용하는 방법을 다룹니다.

## GnuPG를 더욱 편리하게

GnuPG는 기본적으로 터미널과 같은 커맨드라인 인터페이스에서 조작하도록 되어있지만,
GUI에서도 GnuPG를 사용할 수 있도록 여러가지 확장 프로그램이 개발되어 왔습니다.
이 페이지에서는 그 중 일부만을 다룹니다.

### 웹브라우저 플러그인 Mailvelope

[Mailvelope](https://www.mailvelope.com/en/)는 웹메일 등에서 OpenPGP의 기능을
사용할 수 있도록 하는 웹브라우저 확장 프로그램입니다.
Google Chrome, MS Edge, Mozilla Firefox를 지원하며, Gmail 등의 보편적인 웹메일에서
암호화/복호화, 서명/검증 등의 기능을 사용할 수 있습니다.
GnuPG에 저장된 키들을 이용하여 해당 기능을 이용하는 것도 가능하고,
GnuPG와는 별도의 키 저장소를 사용하여 GnuPG를 설치하지 않고도 이용하는 것이 가능합니다.
(이는 GnuPG와는 별도의 OpenPGP 구현체인 OpenPGP.js를 이용하기 때문입니다.)
[튜토리얼](https://www.mailvelope.com/en/help)을 통해 Mailvelope를 사용하는
기초적인 방법을 익힐 수 있습니다.

### Keybase 이용하기

Keybase는 공개키를 SNS나 DNS, 암호화폐 인증과 함께 배포할 수 있는 서비스입니다.
자신의 Twitter나 Gist에 인증 메세지를 포스팅하면, Keybase가 그것을 판독하여
공개키와 함께 인증된 계정을 표시하는 형식입니다. 그 외에도 Keybase는 많은 기능을
지원하는데,

- 공개키 동기화: 자신이 팔로우하는 계정에 등록된 공개키를 자동으로 가져오기 할 수 있습니다.
또한 자신의 공개키가 변경된 경우에도 공개키를 업데이트할 수 있습니다.
- 개인키 호스팅: 개인키를 업로드하여 Keybase 웹상에서 복호화와 서명 기능을 이용할 수 있습니다.
물론 개인키를 항상 업로드할 필요는 없고, 복호화와 서명 기능을 웹에서 이용하고 싶은 경우에만
업로드하면 됩니다. Keybase를 신뢰할 수 없다면 개인키를 업로드하지 않아도 됩니다.
- 기기 관리: 계정 정보가 변경되고 새로운 내용이 추가될 때마다, 그 내용에 Keybase는
서명을 필요로 합니다. 이 때, 서명의 키 역할을 하는 것이 기기입니다.
기기는 Keybase 어플리케이션을 설치하여 인증을 마친 기기로,
다른 기기를 추가하거나, 해지하는 경우에 필요하게 됩니다.
스마트폰이나 컴퓨터 등 물리적인 기기 외에도, 단어를 나열한 형태로 되어있는
종이(paper) 기기도 존재합니다.
- Sigchain: 위에서 언급한 계정의 변경 사항들은 서명을 통해 체인 형태로 이어져
투명하게 공개됩니다. 예를 들면, 저의 계정의 Sigchain은 [여기](https://keybase.io/loudcolour/sigchain#67caa149d3c2f96d1440b5d4777ce5082042094d49a373509ae250279888864c0f)서
확인할 수 있습니다. Sigchain 이외에도 계정에 연결된 SNS 계정이나 기기가
어떤 관계에 의해 연결되고 해지되었는지, [그래프](https://keybase.io/loudcolour/graph)를 통해 확인할 수도 있습니다.
- Keybase 챗: 종단간(E2E) 암호화가 적용된 채팅 기능입니다. Keybase 앱을 설치하여
스마트폰이나 컴퓨터에서 사용할 수 있습니다.
- KBFS: Keybase File System. 클라우드 기반의 파일 공유 기능입니다.
[Keybase.pub](https://keybase.pub)에서 관련 내용을 확인할 수 있습니다.
- 그 밖에 다양한 기능들은 [공식 문서](https://book.keybase.io/docs)에서 확인할 수 있습니다.

## OpenPGP 카드 사용하기

### OpenPGP 카드란 무엇인가

### OpenPGP 카드 구입하기

사실은 OpenPGP 카드 뿐만이 아니라 Yubico와 Nitrokey 또한 이 기능을 지원합니다.

## GnuPG, 고급편?

### 고급: Git Commit에 서명하기

### 고급: SSH 너머로 사용하기
