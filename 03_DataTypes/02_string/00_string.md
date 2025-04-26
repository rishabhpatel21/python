# > Strings

- A string is a sequence of characters surrounded by quotes 
- A string can be single or double quoted examples: 'hello', "hello"
- A string can also be triple quoted examples: '''hello''', """hello"""

- raw string - explanation is that it is a raw string, it will not be escaped means it will be printed as is - example: r'hello', code: print(r'hello\nworld') - output: hello\nworld
---

# > String methods

- len() - returns the length of the string
- upper() - returns the string in upper case, cdoe-example: "hello world" - output: "HELLO WORLD"
- lower() - returns the string in lower case, code-example: "HELLO WORLD" - output: "hello world"
- title() - returns the string in title case, code-example: "hello world" - output: "Hello World"
- capitalize() - returns the string in capitalize case, code-example: "hello world" - output: "Hello world"

- casefold() - returns the string in casefold case, code-example: "HELLO WORLD" - output: "hello world"
- swapcase() - returns the string in swapcase case, code-example: "hello world" - output: "HELLO WORLD"

- center() - returns the string in center case
- ljust() - returns the string in ljust case, left justify, example: "abc " - output: "abc   "
- rjust() - returns the string in rjust case, right justify, example: "abc" - output: "   abc"
- zfill() - returns the string in zfill case, zero fill, example: "abc" - output: "000abc"

- strip() - returns the string in strip case
- lstrip() - returns the string in lstrip case, left strip
- rstrip() - returns the string in rstrip case, right strip

- replace() - returns the string in replace case, code formate: "a".replace("a", "b") - output: "b"
- join() - returns the string in join case , code formate: "abc".join(["a", "b", "c"]) - output: "abc"
- format() - returns the string in format case, code formate: "{} {}".format("a", "b") - output: "a b"

- encode() - returns the string in encode case
- decode() - returns the string in decode case

- isalnum() - returns the string in isalnum case , alpha numeric , example: "abc123" 
- isalpha() - returns the string in isalpha case , alpha only , example: "abc"
- isdigit() - returns the string in isdigit case , digits only , example: "123"
- isspace() - returns the string in isspace case , spaces only , example: "   "
- islower() - returns the string in islower case , lowercase only , example: "abc"
- isupper() - returns the string in isupper case , uppercase only , example: "ABC"
- isnumeric() - returns the string in isnumeric case , numeric only , example: "123"
- isdecimal() - returns the string in isdecimal case , decimal only , example: "123.45"

---

# > library for strings



- [Python String Functions](https://www.w3schools.com/python/python_ref_string.asp)

---