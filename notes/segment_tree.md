<!---
title: '[Example NOTE] Segment Tree에 대하여'
category: Algorithms
language: Korean
--->

배열의 부분열의 총합을 구하는 문제를 생각하자.
이 때, 배열을 수열로 생각하여 부분합을 미리 계산하여 부분합의 차로 부분열의 총합을 구하는
방법이 고려되나, 이는 O(n)의 시간복잡도를 가진다.
부분합의 배열대신. segment tree를 생성하여,
해당하는 연산의 시간복잡도를 O(log n)으로 단축할 수 있다.

segment tree는 바이너리 트리를 기반으로 하여, children node에는 배열에 저장된 값을,
해당하는 parent node에는 children node들의 합을 저장하도록 한다.
segment tree의 각 node에는 트리의 윗부분부터 높이 계층을 우선시하여 번호를 부여한다.
이를 위해서는, 최상위 node의 번호를 0로 잡아 어떤 node의 번호가
`x`일 때, 왼쪽 children node는 `2*x-1`, 오른쪽 children node는 `2*x`로 할당하면 된다.
다음 코드는 배열 `a`가 주어졌을 때, segment tree인 `tree`를 생성하는 코드이다.

``` rust
fn main() {
    let a = vec![11, 14, 56, 13, 6, 12, 67, 34]; // random vector
    let mut tree = vec![0;16];    // zero-initialized tree vector
    let l = a.len()-1;
    init(&a, &mut tree, 1, 0, l);             // generate segtree
    println!("{:?}", a);
    println!("{:?}", tree);
}

fn init(a:&Vec<i64>, tree:&mut Vec<i64>,
        n:usize,
        b:usize, e:usize) -> i64 {
    if b == e {
        tree[n] = a[b];
        return tree[n];
    } else {
        let k = (b+e)/2;
        tree[n] = init(a, tree, 2*n, b, k) + init(a, tree, 2*n+1, k+1, e);
        return tree[n];
    }
}
```

재귀를 이용하여, segment tree를 생성하였다. 위의 코드를 실행한 결과는 다음과 같다.

``` shell
[0, 213, 94, 119, 25, 69, 18, 101, 11, 14, 56, 13, 6, 12, 67, 34]
```

`tree`의 `1`번 index를 최상단 node로 하였으므로 위와 같은 결과를 얻는다.
위의 코드에서는 segment tree의 크기를 적당히 `16`으로 정하였지만,
실제로는 주어진 배열의 크기가 $N$이라면, $H=\lceil \log_2N\rceil$으로 둘 때,
segment tree의 크기를 $2^{H+1}$로 두는 것이 적당하다.

## 구간의 총합 구하기

어떤 node가 담당하고 있는 구간을 `[b,e]`, 합을 구하려하는 구간을 `[left,right]`로 둘 때,
tree를 순회하면서 적합한 node를 탐색하는 경우를 생각하자.
`[b,e]`와 `[left,right]` 사이의 관계를 고찰하면,

1. `[b,e]`와 `[left,right]`가 겹치지 않는 경우.
2. `left <= b`, `e <= right`인 경우.
3. `b < left`, `right < e`인 경우.
4. 셋 중 어느 것에도 속하지 않는 경우.

가 있다. 1번의 경우, 더이상 구하고자 하는 범위에 children node가 존재하지 않으므로
0를 return하여 탐색을 종료하면 된다. 2번의 경우 역시, 구하고자 하는 범위 내에
node가 담당하는 범위가 포함되므로, node 자신의 값만을 return하여 탐색을 종료하면 된다.

3번과 4번의 경우는 node가 담당하는 값 이외에도 구하고자 하는 범위의 값이 존재하므로,
재귀를 이용하여 탐색을 이어나갈 필요가 있다. 이를 구현한 코드는 다음과 같다.

``` rust
fn main() {
    let a = vec![11, 14, 56, 13, 6, 12, 67, 34]; // random vector
    let mut tree = vec![0;16];    // zero-initialized tree vector
    let l = a.len()-1;
    init(&a, &mut tree, 1, 0, l);             // generate segtree
    println!("{:?}", a);
    println!("{:?}", tree);
    println!("{}", range_sum(&mut tree, 1, 0, l, 2, 5));
}

fn init() {
    ...
}

fn range_sum(tree:&mut Vec<i64>,
             n:usize,
             b:usize, e:usize,
             left:usize, right:usize) -> i64 {
    if      (left>e) || (right<b)   {0}
    else if (left<=b) && (right>=e) {tree[n]}
    else {let k = (b+e)/2;
          range_sum(tree, 2*n, b, k, left, right)
        + range_sum(tree, 2*n+1, k+1, e, left, right)}
}
```

## 수 변경하기

중간의 어떤 수`a[index]`를 `val`로 변경한다면 그 변경사항에 맞도록 tree
또한 업데이트할 필요가 있다.
변경되는 수를 가지는 요소에 해당되는 leaf node를 탐색해가며, 경로 위의 모든 node를
업데이트하여야 한다. 해당 leaf node의 모든 ancestor node의 diff는
`val-a[index]`로 일치함을 이용하면 된다.

노드 탐색을 시작하여, 어떤 node가 담당하는 범위 내에 `index`가 포함되면 diff를 더하고
자식 노드로 진행하게 하는 식으로 탐색을 진행하면 된다.
`index`가 포함되지 않는다면 그대로 탐색을 종료하면 된다.
다음 코드는 `diff`값을 통해 tree를 업데이트 하는 함수를 구현한 것이다.

``` rust
fn main() {
    let a = vec![11, 14, 56, 13, 6, 12, 67, 34]; // random vector
    let mut tree = vec![0;16];    // zero-initialized tree vector
    let l = a.len()-1;
    init(&a, &mut tree, 1, 0, l);             // generate segtree
    println!("{:?}", a);
    println!("{:?}", tree);
    println!("{}", range_sum(&mut tree, 1, 0, l, 2, 5));
    update_tree(&mut tree, 4, -23, 1, 0, l);
    println!("{:?}", tree);
    println!("{}", range_sum(&mut tree, 1, 0, l, 2, 5));
}

fn init(a:&Vec<i64>, tree:&mut Vec<i64>,
    ...
}

fn range_sum(tree:&mut Vec<i64>,
             n:usize,
             b:usize, e:usize,
             left:usize, right:usize) -> i64 {
    ...
}

fn update_tree(tree:&mut Vec<i64>,
               index:usize, diff:i64,
               n:usize,
               b:usize, e:usize) {
    if (index < b) || (index > e) {return;}
    tree[n] += diff;
    if b != e {
        let k = (b+e)/2;
        update_tree(tree,index,diff,2*n,b,k);
        update_tree(tree,index,diff,2*n+1,k+1,e);
    }
}

```
