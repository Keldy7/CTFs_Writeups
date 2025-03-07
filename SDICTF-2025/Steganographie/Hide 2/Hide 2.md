# Hide 2

> Level: xxx || 50 points


## 1. Data

> Instruction

![Instruction Challenge Hide 2](challenge_Hide_2.png)

> Resource

A text file `victor2.txt`

> Hint (I didn't use it)



## 2. Solution

On opening the file, I realized that the text it contained looked as if it had undergone some kind of processing (a text stegnography technique).

I used the following [tool] (https://holloway.nz/steg/) to extract the hidden message.

![Extracted message](https://github.com/user-attachments/assets/afffdc0b-0e7a-43e2-b6a4-7cc547dc813a)

The extracted message is: `twitter_flag` which is the flag but hashed with [SHA1](https://www.sha1-online.com/).<br>

=> Note: https://securityaffairs.com/24681/hacking/steganography-tweet.html
<br>


## 3. Flag

```plaintext
SDICTF{f247ffde107489a174e72d63bcbd872937b39614}
```
