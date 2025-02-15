# Oh, oh where is my phone

> Level: Easy || 50 points

## 1. Data

> Instruction

![Instruction Challenge Steg2](challenge_oh_oh_where_my_phone.png)

> Resource

A text file `challent1.txt` (See Resources folder)


## 2. Solution

The challenge provides a Mobile Country Code (MCC), Mobile Network Code (MNC), Cell ID (CID), and Location Area Code (LAC). The objective is to determine the corresponding geographic coordinates (latitude and longitude).  

Initially, this seemed straightforward, but not knowing the appropriate tools made it more challenging. After some research, I tried different approaches and eventually used **Google Dorking**

![Dorking query](https://github.com/user-attachments/assets/2b08c0b9-c335-47d8-a888-a9f042d36049)

This led me to a [Stack Overflow](https://stackoverflow.com/questions/26086736/get-mnc-mcc-lac-and-cid-from-mobile-number) thread where users recommended two methods:

- https://unwiredlabs.com/api (one involving an API which I ignored due to the need for coding)
- https://opencellid.org

**OpenCelliD** is an open database that maps cell towers worldwide, allowing users to retrieve location data based on MCC, MNC, CID, and LAC. Using the website, I quickly found the corresponding latitude and longitude.

![The corresponding latitude and longitude](https://github.com/user-attachments/assets/c4f845ce-a283-4b39-b417-012cb469850a)


## 3. Flag
    
```text
CAF_{51.492359,-0.087228}
```
