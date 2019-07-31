# simple search queries 

## Challenge Name

simple search queries

## Problem Statement

文字列`S`と、`Q`個のクエリ文字列`q_i`が与えられる。`(1<=i<=Q)`  
`q_i` それぞれについて、文字列`S`の連続した部分文字列として含まれているかどうか判定せよ。  
  
≪連続した部分文字列とは≫   
 
- `"ab"` や `"bca"` や `"c"` や `"abcac"` は、`"abcac"` の連続した部分文字列である  
- `"aa"` や `"aba"` や `"xyz"` は、`"abcac"` の連続した部分文字列ではない  

## Input Format

```
N K
v_1 a_1 c_1
v_2 a_2 c_2
...
v_N a_N c_N
```

## Constraints

- `Q`は整数、`S`や`q_i`はすべて英小文字からなる  
- `1 <= |S| <= 1000`
- `1 <= Q <= 2*10^5`
- `1 <= |q_i| <= |S|`
- `1 <= Σq <= 2*10^5`

## Output Format

`Q`行出力すること。  
`i`行目には、`q_i`が`S`に含まれているなら`"YES"`、含まれていなければ`"NO"`と出力せよ `(1<=i<=Q)`  
末尾に改行をいれること。  

## Sample Case

TODO

### Sample Case 1

```
```

```
```

### Sample Case 2

```
```

```
```
