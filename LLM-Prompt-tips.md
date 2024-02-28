
# **Tips for Better Results with Large Language Models**

## **Understanding LLMs**

* **Capabilities:** LLMs are incredibly powerful tools for text generation, translation, summarization, and more.  But they are not all-knowing; they process information based on the massive datasets they've been trained on.
* **Limitations:** LLMs can sometimes produce incorrect or misleading responses. They are prone to biases present in their training data, and may "hallucinate" information  that seems plausible but isn't factually true. Always carefully evaluate LLM output.

### **Providing Quality Input**

* **Be Specific:**  Avoid vague, overly broad queries. The more specific and detailed your input, the better the LLM's understanding and the more focused its response.
* **Give Context:** The more background information you provide, the better the LLM can interpret your request and tailor its response. Consider  describing the goal or task you have in mind.
* **Structure Clearly:** Use well-formed sentences and avoid excessive ambiguity. Clear structure leads to clearer output.

### **Crafting Your Prompts**

* **Clear Instructions:** Give direct instructions on what kind of output you want: 
    * "Write a poem about..."
    * "Summarize this article..."
    * "Translate this paragraph into French..."
    * "Create a Powershell cheat sheet in markdown format"
* **Keywords:** Include relevant keywords to provide guidance and focus the LLM on the most important aspects of your query.
* **Examples:** Show the LLM  the style or format you want it to emulate. Providing a previous example of successful output can significantly improve results.

### **Iterative Improvement**

* **Start Simple:** Test with basic requests before complex ones. This helps gauge the LLM's baseline understanding.
* **Do prior research**: If you don't already understand the vocabulary being used in the given context, it is difficult to form good prompts and thus get accurate results. Doing a small amount of research on the topic can be hugely beneficial. You don't always need to understand all of it, and it can be useful to ask for analogies to understand complex things.
* **Refine with Feedback:** If the response misses the mark, provide feedback explaining why, and try rephrasing your query. Be specific about what you'd like to see changed in the output.
* **Multi-Turn Conversations:**  Engage in dialogue with the LLM to build upon previous responses and fine-tune results.
* **Verify the logical processes:** Tell the bot to output the response in a format such that it's logical decision making processes can be verified in the output (basically fact checks itself). 

### **Advanced Techniques**

* **Chain of Thought (CoT) Prompting**: Provide your LLM with a step-by-step reasoning process, prompting it to break down problems  into smaller, easier-to-solve chunks.  This promotes more thorough and logical responses.

* **Few-Shot Learning:** Supply a few carefully chosen examples (input/output pairs) to demonstrate the kind of response you expect.  The LLM often uses these to adjust its approach, giving better results.

* **Code Formatting:** For code snippets, use triple backticks (```) followed by the language name for proper syntax highlighting:

   ```python
   print("Hello, world!")
   ```

* **Role Specification:** For more creative responses, define roles:

- `"You are a professional Math mentor/tutor, with a specialization in Algebraic Number theory. I'm a student struggling with a math problem. Can you help me understand this concept?"`
- ```
  [Role: Professional Cyber Security tutor/Professor]
  [Content: Markdown Format, Easy to understand, Concise, Straight-to-the-point, Code examples (Python)]
  [Prompt: I am doing a Web Exploitation CTF challenge, please help me understand this concept, what are some possible routes towards retrieving the flag in this challenge? Don't give me the answer, help me understand the underlying concepts.]
  [Prompt: Please output your response in a manner such that you logical decision making can be further validated by an external entity]
  ```
   - By asking the bot to output the respond in a manner that can be validated by an external entity, it essentially fact checks itself automatically (sometimes). This can be very useful for getting more accurate responses. If you notice hallucinations, tell it where it was wrong and why. 

### **Tips for Using LLMs in CTFs**

**Know Your Limitations**

* **Fact-Checking is Essential:** LLMs can be helpful, but don't blindly trust their output.  Always cross-reference information with reputable sources or tools, especially for critical cybersecurity concepts.
* **No Replacement for Tools:** LLMs are **not** substitutes for specialized cybersecurity tools like vulnerability scanners or exploit frameworks. They can supplement, but not replace, these specialized resources.

**Providing Context for Optimal Use**
* **Provide Similar Challenge  Writeups:** For example, if you are doing a RSA Crypto challenge, look up CTF writeups for similar challenges, and if it is useful for the given challenge, copy and paste the writeup in the LLM prompt to help you narrow down your logical deecision making. 
* **Challenge Description:**  Give the LLM a brief summary of the challenge you're working on, including the overall objective and any specific clues or context you've gathered.
* **Relevant Technologies:** Specify the technologies in play (e.g., "Reverse engineering a Linux binary," "Analyzing a web application for SQL injection"). This helps the LLM focus its response.
* **Current Attempts:** Explain what you've already tried. This avoids the LLM simply repeating something you already know doesn't work.

**Prompting Strategies**

* **Explaining Concepts:** Ask the LLM to explain relevant concepts:
    * "Explain buffer overflows in detail."
    * "Describe common XSS attack vectors."
* **Tool Suggestions:** Get recommendations for tools or techniques:
    * "What tools are useful for decompiling binaries?"
    * "Suggest common commands for network enumeration."
* **Code Snippets:** If stuck on a code-related task, provide your existing code (properly formatted within code blocks) and ask for assistance:
    * "Can you help me spot the error in this Python exploit script?" 
    * "How would you optimize this SQL injection payload?"
* **Hypothetical Scenarios:** If a CTF involves unique rules or setups, outline a hypothetical scenario based on the CTF context to get tailored guidance. 

**Leveraging LLMs Responsibly**

* **Avoid Direct Answers**: If an LLM seems to know a challenge solution, resist asking for it directly; as this completely defeats the purpose of the CTF.  Use it to build knowledge, not to spoil the learning process.
* **Hints, Not Handouts:** Seek specific hints or explanations of underlying concepts and techniques to progress in challenges.  Outright solutions won't help you develop those "learn by doing" skills essential for the CTF mindset.



**Remember:** Experimenting with different phrasing and approaches is key. LLMs are powerful but nuanced tools. With these tips, you'll achieve better and more satisfying results from your interactions! 

