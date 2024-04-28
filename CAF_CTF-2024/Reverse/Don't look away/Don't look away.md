# Don't look Away

> Level: Easy || 50 points

## 1. Data

> Instruction

![Instruction Challenge Don't look away](challenge_Dont-look-away.png)

> Resource

A compiled python script `Problem_1.pyc` (See Resources folder)


## 2. Solution

For this challenge, we have a compiled python script when we run with the following command, the script requires a password so we will try to decompile to see the source code.<br>

```bash
$ python3 Problem_1.pyc
```

To decompile it, we can use `uncompyle6` package available via *pip install uncompyle6* but with his last we get a decompilation error about the python@3.11 version. After various online researchs, we have found the [lddgo](https://www.lddgo.net/en/string/pyc-compile-decompile) website who we have allowed to see partially the content of file.

![Decompilation](https://github.com/Keldy7/CTFs_Writeups/assets/93558050/9e214831-5631-419c-8b18-a0a7826b2eb6)

After decompiling, we can see a *correct_password* variable. It's the flag.

![Flag](https://github.com/Keldy7/CTFs_Writeups/assets/93558050/960e69ec-d96f-471c-97f4-02b73b1b1ace)


## 3. Flag

```text
CAF_{Enter the password}
```
