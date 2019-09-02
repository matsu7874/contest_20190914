# simple search queries

## Challenge Name

simple search queries

## Problem Statement

文字列`S`と、`Q`個のクエリ文字列`q_i`が与えられる。`(1<=i<=Q)`  
`q_i` それぞれについて、文字列`S`の部分文字列として含まれているかどうか判定せよ。  

≪部分文字列とは≫   

- `"ab"` や `"bca"` や `"c"` や `"abcac"` は、`"abcac"` の部分文字列である  
- `"aa"` や `"aba"` や `"xyz"` は、`"abcac"` の部分文字列ではない  

## Input Format

```
S
Q
q_1
q_2
...
q_Q
```

## Constraints

- `Q`は整数、`S`や`q_i`はすべて英小文字からなる  
- `1 <= |S| <= 1000`
- `1 <= Q <= 10^6`
- `1 <= |q_i| <= |S|`
- `1 <= Σ|q_i| <= 10^6`

## Output Format

`Q`行出力すること。  
`i`行目には、`q_i`が`S`の部分文字列なら`"YES"`、そうでなければ`"NO"`と出力せよ `(1<=i<=Q)`  
末尾に改行をいれること。  

## Sample Case

### Sample Case 1

```
yurufuwacontest
8
yurufuwacon
yuruyuru
fuwafuwa
ac
wa
contest
contestttt
goriiiiiiii
```

```
YES
NO
NO
YES
YES
YES
NO
NO
```

例えば、
* `1`番目の`yurufuwacon` は `yurufuwacontest` の部分文字列なので `1`行目には`YES`と出力する。  
* `2`番目の`yuruyuru` は `yurufuwacontest` の部分文字列ではないので `2`行目には`NO`と出力する。  
...
以下同様に`8`行出力する。  

### Sample Case 2

```
okomenooishiitakikatasoshiteokomewotaberukotoniyorusonokouka
5
okome
okomekome
bitamin
mineraru
shokumotsusenni
```

```
YES
NO
NO
NO
NO
```
