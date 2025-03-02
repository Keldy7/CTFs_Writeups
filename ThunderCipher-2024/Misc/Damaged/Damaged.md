# Damaged

> Level: xxx || 100 points

## 1. Data

> Instruction

![Instruction Challenge Damaged](challenge_Damaged.png)

> Resource

A data file (See Resource folder)


## 2. Solution

A very basic challenge to repair a corrupted file. First, no extension for this file, so I start with a good old command `file` to see what it's all about. Result: “data”. Super vague... but that doesn't stop us!

![File type](https://github.com/user-attachments/assets/c7992152-fdd8-4a0f-87db-c6543135fca9)

I decide to take a look at the content with `cat` command. And there, jackpot! I recognize something familiar: *IHDR*. Ok, we have a PNG here. 

![File contents](https://github.com/user-attachments/assets/ab8cbcf0-c66b-4c24-935d-1f8fa32d67fa)

Let's then use a hexadecimal editor to see the first bytes of the file.

```bash
$ hexeditor damaged
```
A valid PNG file must start with the following signature:

```mathematica
89 50 4E 47 0D 0A 1A 0A
```
However, the first bytes of the file were corrupted and did not match this signature.

![PNG signature](https://github.com/user-attachments/assets/87ca33e7-b287-4ce2-9ac1-6eeaf83ffd80)

Once the first 8 bytes were corrected with the correct signature of the PNG format, I saved the file. Bingo! The image is displayed with the flag clearly visible.



## 3. Flag

```text
ThunderCipher{fixing_images_is_fun}
```
