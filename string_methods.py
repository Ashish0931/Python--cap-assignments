#string methods 
text="this is a test text"
text_2="joined text"
text_3="100"
print("capitalize: ",text.capitalize())
print("casefold: ",text.casefold())
print("center:", text.center(100))
print("count :" ,text.count("t"))
print("encode: ",text.encode())
print("endswith: ",text.endswith("h"))	
print("expand tabs: ",text.expandtabs())	 
print("format: ",text.format())	
print("isalnum: ", text.isalnum())	
print("is alpha: ", text.isalpha())	
print("is ascii: ", text.isascii())	 
print("is decimal: ",text.isdecimal())	
print("is digit: ",text.isdigit())	
print("is identifier: ",text.isidentifier())	 
print("is numeric: ",text.isnumeric())
print("is printable: ",text.isprintable())	
print("is space: ",text.isspace())	
print("is title",text.istitle())	
print("is upper: ",text.isupper()) 	 
print("text join: ",text.join(text_2))                      	
print("text partition: ",text.partition("h"))	
print("replace word x with z: ",text.replace("x","z"))	
print("find e:",text.rfind("e"))	
print("index of s: ",text.rindex("s"))	
print("space of 100 spaces: ",text.rjust(100))	
print("split from s: ",text.rsplit("s"))	
print("rstrip: ",text.rstrip())	
print("split lines: ",text.splitlines())	
print("if starts with y? :",text.startswith("y"))	
print("strip:", text.strip())	
print("title: ",text.title())	
print("fill zeroes: ",text.zfill(25))