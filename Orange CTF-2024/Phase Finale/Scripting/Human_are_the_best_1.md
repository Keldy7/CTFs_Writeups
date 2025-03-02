# Human are the best 1

> Level: xx points


## 1. Data

> Resource

A link to a web page https://orangesecurity-challengescripting1.chals.io/



## 2. Solution

Exploring the page, we discover a discussion between a human and a robot. This suggests that we need to analyze their interaction in greater depth.

![Home page](https://github.com/user-attachments/assets/0b9c7d90-30b8-44cc-9f0b-2f5f89287d19)

Curious, we delved into the HTML source code and spotted a hidden comment mentioning that robots have their own discussion space.

![Source code](https://github.com/user-attachments/assets/2c00bc0e-b8da-4cdc-ad9e-6ef4621cc078)

One word comes up a lot: robot. This leads us to test access to a file often used by indexing robots: `robots.txt`. <br>
=> This is a file that guides search engine robots by telling them which pages of a site they can crawl, in order to avoid query overload. <br>
Accessing robots.txt, we find a simple question: a multiplication to be solved.

![script3](https://github.com/user-attachments/assets/e4cde44d-6dc0-4d2b-afd9-11d110bfd87d)


The page waits for a response, but after a while, the multiplication changes and we receive the message: **"You are not one of us... ”** 
The file is dynamic, which means we have to automate the sending of responses to be accepted as “one of them”.

![script4](https://github.com/user-attachments/assets/69862581-9d83-4815-a7e5-bc714d0b5fc5)

We use a Python script with the *requests* library to retrieve the mathematical operation then calculate the answer and automatically submit the answer before expiration. <br><br>

```python
import re, requests

# URL of the page containing the challenge
URL_PAGE = "https://orangesecurity-challengescripting1.chals.io/robots.txt"

with requests.Session() as session:
    while True:        
        
        # Sending a GET request to fetch the page content
        page = session.get(URL_PAGE)
        page_content = page.text
        print("Page content : ", page_content)

        # Searching for a multiplication operation in the page content
        match = re.search(r"What is the answer to this\s*:\s*(\d+)\s*x\s*(\d+)", page_content)

        if match:
            # Extracting the two operands and performing the multiplication
            operand1, operand2 = map(int, match.groups())
            result = operand1 * operand2
            print(f"Calculating : {operand1} x {operand2} = {result}")

            # Sending the computed result as a parameter in the request
            response = session.get(URL_PAGE, params={'solution': result})
            page_content = response.text

            # Checking if the response contains a different message, indicating success
            if "You are not one of us..." not in page_content and "What is the answer to this" not in page_content:
                print("Result:", page_content)
                break

        else:
            # If no operation is found in the page content, print and break
            print("Page content : ", page_content)
            break
```
🔗 Useful documentation for writing the script : [Requests - Advanced Usage](https://requests.readthedocs.io/en/latest/user/advanced/)



## 3. Flag

```text
OCI_{IA_STARTED_WITH_SCRIPTING}
```




