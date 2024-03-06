# Wavvy Karate

This challenge provides the participant with the `.wav` file of the song: "https://www.youtube.com/watch?v=cLi05MF5X7Q".

- **Update:** I am quite upset as I had to replace the fire tunes provided with a short video="https://www.youtube.com/watch?v=k-fVjHzxKzo".
  - The song was *unsurprisingly* large... Unlucky. 

To create this challenge, I provided the link of the song on youtube to: "https://y2down.cc/en/youtube-wav.html"

Then I used `steghide` to embed `flag.txt` using a randomly selected password from `/usr/share/wordlists/rockyou.txt`.

## Solution
```bash
#!/bin/bash
# replace yourfile.wav with the name of the .wav file you are trying to extract data from.
FILE="yourfile.wav" # The file you're trying to extract data from
# rockyou wordlist using the standard kali path for wordlists
WORDLIST="/usr/share/wordlists/rockyou.txt"

while IFS= read -r line; do
  echo "Trying passphrase: $line"
  if steghide extract -sf "$FILE" -p "$line" 2>/dev/null; then
    echo "Success! Passphrase is: $line"
    break
  fi
done < "$WORDLIST"
```
- Note: It may take a while, it depends on how much hardware resources you have allocated.

```
GrizzCTF{
```
