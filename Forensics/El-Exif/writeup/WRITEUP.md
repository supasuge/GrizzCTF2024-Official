# El Exif Writeup


```bash
exiftool src/kewlkeyboard.png | awk '/Description/' | awk {'print $3'}
```
- Running this command output's the exifdata using `exiftool`, then uses `awk` to filter & extract the flag from the data.

```
GrizzCTF{ex1fd4ta_1s_1nt3r3st1ng}
```
![cmd](image.png)
