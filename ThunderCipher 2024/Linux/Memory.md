# Memory

> Level: Easy<br>
> Points: 15 

## 1. Instruction

![Assist challenge](https://github.com/Keldy7/CTFs_Writeups/assets/93558050/cb8298a9-6281-42ba-bfef-d118236c61d1)


## 2. Solution

To find out the memory capacity of his system, Johnny can use different commands depending on the operating system he is using. But since this is a Linux challenge, the command is `free`. <br>
Using the `free` Command:<br>
```bash
free -h
```

This command displays the total, used, and free memory in a human-readable format.


## 3. Flag

```text
ThunderCipher{free}
```
