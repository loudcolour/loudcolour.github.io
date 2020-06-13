<!---
title: '$n!>\left( \frac{n}{e} \right)^n$'
language: Korean
category: Mathematics
--->

# $n!>\left( \frac{n}{e} \right)^n$

$\left( 1+\frac{1}{n} \right)^n<e$라는 것을 이항정리와 단조증가성으로부터 알 수 있다.
이 결과를 이용하여, 계승에 관한 부등식 $n!>\left( \frac{n}{e} \right)^n$
를 수학적 귀납법으로 유도할 수 있다.

$n=1$인 경우에는
$1!>\frac{1}{e}$ 이 성립한다. $n=k$인 경우에 $k!>\left( \frac{k}{e} \right)^k$이 성립한다면
$\left( 1+\frac{1}{k} \right)^k<e$로부터 $k+1> \frac{\left( k+1 \right)^{k+1}}{ek^k}$이 성립하므로,

$$
(k+1)! = k!\cdot(k+1) > \left( \frac{k}{e} \right)^k\cdot
\frac{\left( k+1 \right)^{k+1}}{ek^k}= \left( \frac{k+1}{e} \right)^{k+1}
$$

와 같이 $n=k+1$일 때에도 성립하는 것을 알 수 있다. 따라서 부등식
$n!>\left( \frac{n}{e} \right)^n$이 성립한다.
