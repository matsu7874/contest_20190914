# fuzzy search queries

## Challenge Name

fuzzy search queries

## Problem Statement

ゴリ太郎君はスーパープログラマなので下のような仕様の検索プログラムを実装した。  

- `Q`個のクエリ文字列`q_i`それぞれに対して、  
  - 文字列`S`の部分文字列として`q_i`が含まれていたら、`YES`と出力する。  
  - そうでないとき、`q_i`と **同じ長さの** 部分文字列であり、辞書順で`q_i`の直後に来るものが存在すれば、その部分文字列を出力する。  
  - それも存在しないときは `NO`と出力する。  

文字列`S`と、`Q`個のクエリ文字列`q_i`が与えられる。`(1<=i<=Q)`  
各クエリに対して、ゴリ太郎君の検索プログラムの出力を求めよ。  

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
- `1 <= |S| <= 3*10^4`
- `1 <= Q <= 10^5`
- `|q_i| >= 1`
- `1 <= Σ|q_i| <= 10^5`

## Output Format

`Q`行出力すること。  
`i`行目には、`q_i`に対するゴリ太郎君の検索プログラムの出力結果を出力せよ `(1<=i<=Q)`  
末尾に改行をいれること。  

## Sample Case

### Sample Case 1

```
abracadabra
12
abra
cadabra
brabra
abura
banana
gorilla
zebra
a
chocolate
rarara
aaaaaaaaaaa
aaaaaaaaaaaa
```

```
YES
YES
bracad
acada
bracad
racadab
NO
YES
racadabra
NO
abracadabra
NO
```

例えば、
- `1`番目の`abra` は `abracadabra` の部分文字列なので `1`行目には`YES`と出力する。  
- `3`番目の`brabra` は `abracadabra` の部分文字列ではない。`brabra`と同じ長さ`6`の部分文字列を辞書順に列挙すると、`abraca`,`acadab`,`adabra`,`bracad`,`cadabr`,`racada`の順になるが、このうち`brabra`の直後に来るのは`bracad`となるので、`3`行目には`bracad`と出力する。  
- `7`番目の`zebra` は`abracadabra` の部分文字列ではなく、`zebra`と同じ長さ`5`の部分文字列の中で`zebra`より辞書順で後に来るものは存在しない。そのため`7`行目には`NO`と出力する。  
- `12`番目の`aaaaaaaaaaaa`のように、元の文字列`S`の長さより長いクエリも混入しているので注意。  

### Sample Case 2

```
yurufuwaonsite
10
yuru
fuwa
onsite
gorira
no
chosenjo
thank
you
for
coming
```

```
YES
YES
YES
onsite
ns
fuwaonsi
ufuwa
yur
fuw
fuwaon
```
