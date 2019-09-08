# honda's janken

## Challenge Name

honda's janken

## Problem Statement

じゃんけん界最強の人物であるhondaは、普通のじゃんけんには飽きてしまったので、次のようなじゃんけんを考案した。

* 2人のプレイヤー「honda」と「挑戦者」が同時に、アルファベット大文字が書かれた26種のカードの中からを1つ提出する。
* 2つのアルファベットが等しければ、「あいこ」である。
* 2つのアルファベットが異なれば、「hondaの勝ち」である。
* hondaは決して負けることはない。

2人の出したアルファベットが与えられるので、hondaの勝ちならば`honda`、あいこならば`draw`と出力せよ。

## Input Format

```
S
```

`S`は`2`文字からなる。  
- `1`文字目は、hondaの出したアルファベットを表す。  
- `2`文字目は、挑戦者の出したアルファベットを表す。  

## Constraints

- 入力はすべて英大文字からなる
- `|S| = 2`

## Output Format

hondaの勝ちならば`honda`、あいこならば`draw`と出力せよ。
末尾に改行をいれること。

## Sample Case

### Sample Case 1

```
AC
```

```
honda
```

### Sample Case 2

```
ZZ
```

```
draw
```
