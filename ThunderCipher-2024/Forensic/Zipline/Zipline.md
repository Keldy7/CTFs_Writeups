# Zipline

> Level: xxx || 50 points

## 1. Data

> Instruction

![Instruction Challenge Zipline](challenge_ZipLine.png)

> Resource

A zipped folder `zipline.zip` (See Resource folder)


## 2. Solution

For this challenge, we've got a zipped folder, and we're working as usual with our favorite tools.

Ok, so we start by trying to unzip our folder with the `unzip` command, but it requires a password.

![Unzipping folder](https://github.com/user-attachments/assets/9f3af225-e713-4bfd-984d-804ac78b132e)

We're going to use the best tool for cracking passwords: **JohnTheRipper** with its zip2john command to generate a hash of the zip file.

![using JohnTheRipper](https://github.com/user-attachments/assets/195eb3bd-83ff-4e35-999e-b03aa3a739e3)

We'll then use the `john` command to decrypt the password. The password found is *zigzag*, which we enter to unzip the folder and obtain the flag.

![Flag found](https://github.com/user-attachments/assets/4dd46269-859c-4706-b2c2-8d1f6f21b068)

## 3. Flag

```text
ThunderCipher{P4ssW0rd_Pr0t3Ct3D_z1PPP$$$$}
```
