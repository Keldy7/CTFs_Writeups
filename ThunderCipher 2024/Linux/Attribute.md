# Attribute

> Level: Easy<br>
> Points: 15 

## 1. Instruction

![Attribute challenge](https://github.com/Keldy7/CTFs_Writeups/assets/93558050/3e4642f6-1eef-4fb3-9c27-9b6b09150a0d)


## 2. Solution

If Johnny is a root user and is unable to delete a file, there could be a few reasons why this issue is occurring. One common reason is that the file might be immutable, meaning it cannot be modified or deleted even by the root user. This can happen if the file has the immutable attribute set.<br>
* Check if the file is *immutable*:
Use the `lsattr` command to check if the file has the immutable attribute (i).

```bash
lsattr /path/to/file
```

* Remove the Immutable Attribute:
If the file has the *i* attribute, we use the `chattr` command to remove the immutable attribute.

```bash
chattr -i /path/to/file
```



## 3. Flag

```text
ThunderCipher{chattr}
```
