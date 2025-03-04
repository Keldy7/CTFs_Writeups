# Cryptic Pixels

> Level: xxx || 200 points


## 1. Data

> Instruction

![Instruction Challenge Cryptic Pixels](challenge_Cryptic_Pixels.png)

> Resource

A picture file `CrypticPixels.png`


## 2. Solution

First, analyze the picture file with the `exiftool` command to see if there is any hidden information but nothing is found. Next, we use the `strings` command and find that there is a file **flag.txt** in the picture file. 

![Hidden file](https://github.com/user-attachments/assets/25f7dd5f-548e-4a14-bf70-237002a73913)

We extract the hidden file with the `binwalk` command. We can see a file **flag.txt** compressed in a Zip archive file **B8103.zip**. 

![Using binwalk command](https://github.com/user-attachments/assets/a8a35a0f-e36d-4d9c-ae46-9cb5f60816f7)

Then we access folder **_CrypticPixels.extracted**, the zipped file is protected by a password. We use the `zip2john` command to crack it. 

> Note: It's possible to use the `fcrackzip` command to crack the password.

![Cracked password](https://github.com/user-attachments/assets/5f8bca63-c649-417d-bc5f-aa08ff513359)

Finally, we extract the file **flag.txt**. It contains a encrypted message in ROT Cipher. We decode it with https://www.dcode.fr/rot-cipher.

![Decoded message](https://github.com/user-attachments/assets/f71169d5-1bc4-4364-a151-29449b964d1d)


## 3. Flag

```plaintext
ACECTF{h4h4_y0u'r3_5m4r7}
```