# Reverse L2N

> Level: xxx || 20 points


## 1. Data

> Instruction

![Instruction Challenge Reverse L2N](challenge_Reverse_L2N.png)


## 2. Solution


The title `Reverse L2N` gives a big hint! It is about doing an inverse operation, so "Number to Letter" (N2L) while converting the numbers to letters in reverse alphabetical order to get the flag. That is to say:
- 1 → Z,
- 2 → Y,
- ...,
- 26 → A.


So we have to write a Python script to solve this challenge

![Script Python Reverse L2N](https://github.com/user-attachments/assets/09ff66ce-df54-4d66-a1a1-d0107325f6e4)


We get the flag `theking`. For the final flag, we need to hash the flag with [SHA1](http://www.sha1-online.com/).


## 3. Flag

```plaintext
SDICTF{b4f283414a963c09f49cfde4a5eeba9752196247}
```