# Steg 1

> Level: Easy || 50 points

## 1. Data

> Instruction

![Instruction Challenge Steg1](challenge_steg1.png)

> Resource

Two images : `hack.jpg` and `hack.png` (See Resources folder)

## 2. Solution

Utilizing the [zsteg](https://github.com/zed-0xff/zsteg) tool, we extracted text embedded in the image `hack.png`, we successfully uncovered the initial segment of the flag.

![Segment 1 of the flag](https://github.com/Keldy7/CTFs_Writeups/assets/93558050/8412fa6f-fece-4a7b-b8ca-93715ee10112)


Next, we employed the *steghide* tool on the second file `hack.jpg`. Since it required a passphrase, we utilized *stegseek* with the dictionary `rockyou.txt` to discover the passphrase and acquire the second part of the flag.

![Segment 2 of the flag](https://github.com/Keldy7/CTFs_Writeups/assets/93558050/6df54d50-b0fc-4197-8c2d-028de5762ad6)

## 3. Flag

```text
CAF_{Crack_If_You_Can}

```
