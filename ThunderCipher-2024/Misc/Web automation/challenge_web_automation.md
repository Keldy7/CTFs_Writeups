# Web automation

> Level: xxx || 50 points

## 1. Data

> Instruction

![Instruction Challenge Web automation](challenge_web_automation.png)

> Resource

https://github.com/p4nth3r-5237/web-deploy-automation-docker


## 2. Solution

Clicking on the link in the challenge statement takes you to a Github repo with **11 commits** on a single branch called main.

![Github repo](https://github.com/Keldy7/CTFs_Writeups/assets/93558050/df8e9461-a906-420a-a37c-79c9f2c53cdc)

One thing I took as a clue was the contents of the Readme.md file, which says *Commitment*, so I started analyzing the commits made on the repo. 

![Github repo commits](https://github.com/Keldy7/CTFs_Writeups/assets/93558050/ccf9697f-a76c-4f4d-b1e2-42bbe00b44d2)


Scanning the *adding Dockerfile to host in a container* commit, there's a line containing a string that appears to be encoded.

```text
VGh1bmRlckNpcGhlcntTM2NyM1RfMU5fRzF0X0MwbU1pdCE9PT19
```


To decode it, I used the [CyberChef](https://gchq.github.io/CyberChef/#recipe=Magic(3,false,false,'')&input=VkdoMWJtUmxja05wY0dobGNudFRNMk55TTFSZk1VNWZSekYwWDBNd2JVMXBkQ0U5UFQxOQ&oeol=CR) site using the *Magic* operation to determine the encoding type, I got the flag which was Base64 encoded.

![Decoded string with Cyberchef](https://github.com/Keldy7/CTFs_Writeups/assets/93558050/96109b27-7809-4a27-8c3c-f8cf965cfa05)


## 3. Flag

```text
ThunderCipher{S3cr3T_1N_G1t_C0mMit!===}
```
