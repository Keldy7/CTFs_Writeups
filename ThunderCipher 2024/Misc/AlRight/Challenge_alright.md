# AlRight

> Level: xxx || 100 points

## 1. Data

> Instruction

![Instruction Challenge Alright](https://github.com/Keldy7/CTFs_Writeups/assets/93558050/a9287dd2-a055-413f-8a02-5d06afb45bd8)


> Resource

A file `Alright` (See Resources folder)

## 2. Solution

Wowwww for this chalenge, I really beat around the bush despite the fruitful results of my Internet research. Beginner's error I had forgotten that I did not have the applications from the LibreOffice pack of which Word was part. <br>
Let's get started, I first used the `file` command to find out what type of file I'd be dealing with.

![Type of file](https://github.com/Keldy7/CTFs_Writeups/assets/93558050/4d476d1b-1501-43f6-962f-87b580800551)

The file is not a classic Word document, it's a CDFv2 or "Compound Document Format version 2", but also encrypted, as indicated by the file command above. The fact that the document is encrypted makes it very difficult for antivirus software to detect whether it is malicious or not.<br>

CDFV2 can be decrypted with John The Ripper: `office2john`:<br>

```bash
$ office2john AlRight > hash_cdfv.txt
$ john hash_cdfv.txt /usr/share/wordlists/rockyou.txt
```

The password is `qtpie13` and opening the file with LibreOffice Writer to get the flag.<br>

![Password obtained with John The Ripper](https://github.com/Keldy7/CTFs_Writeups/assets/93558050/cb70c198-f90e-4443-a9c5-d6aec60a6d3a)



## 3. Flag
    
```
ThunderCipher{Offic3_F1L3_Cr4cked!!}
```
