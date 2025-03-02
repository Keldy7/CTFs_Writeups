# Bot

> Level: xxx || 10 points

## 1. Data

> Instruction

![Instruction Challenge Bot](challenge_bot.png)


## 2. Solution

Very easy challenge. Just seeing the challenge statement made me think of the robots.txt file, which is a file that tells a search engine's crawler which URLs it can and can't access on your site.

So, I tried to access the robots.txt file by adding `/robots.txt` to the URL of the challenge.

![robots.txt file](https://github.com/user-attachments/assets/fef112bf-7a4c-404c-b964-8dc32823e09d)


And it worked! The robots.txt file contains a forbidden page named `S3cR3tD1r.html`, we access it and get the flag.

```text
https://thundercipher.tech/S3cR3tD1r.html
```

## 3. Flag

```text
ThunderCipher{R0B0ts_4r3_$c4rY}
```
