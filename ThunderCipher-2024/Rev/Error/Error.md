# Error

> Level: xxx || 10 points

## 1. Data

> Instruction

![Instruction Challenge Error](https://github.com/user-attachments/assets/3a33aa02-ebe4-43cd-8704-e44d919f29ee)

## 2. Solution

In analyzing the unknown binary file, our aim was to extract printable strings.

The file consists of *2705 lines*, as identified by the command :

```bash
wc -l error\ -\ Newuser3\ Diallo
```
We specifically searched for the string “Thunder” in the file and identified its line.

![](https://github.com/user-attachments/assets/3ec7ab64-c1c1-4140-8429-abc6a408dc53)

Once we had the result, we decided to focus on a specific range of lines to identify potentially useful information. This took us directly to the flag from line 252 to line 257.

![Flag](https://github.com/user-attachments/assets/e4a99771-c26a-464a-8b85-5a1b20f6064c)

Explanation of commands used : <br>
`| nl` : Number each extracted line. <br>
`| awk '$1 >= 250 && $1 <= 300'` : Filters out lines where the number is between 250 and 300 inclusive.<br>


## 3. Flag

```text
ThunderCipher{4lw4ys_574rt_w17h_57r1ngs_c0mm4nd}
```
