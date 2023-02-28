Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = "  There... are... a... lot ...of: delimiters,,, Ryan?!!!" 
s.replace("...","")
s.replace(",,,","")
s.replace("?!!!","")
s.replace(":","")
SyntaxError: multiple statements found while compiling a single statement
>>> s = "  There... are... a... lot ...of: delimiters,,, Ryan?!!!"
>>> s.replace("...","")
'  There are a lot of: delimiters,,, Ryan?!!!'
>>> s.replace(",,,","")
'  There... are... a... lot ...of: delimiters Ryan?!!!'
>>> s.replace("?!!!","")
'  There... are... a... lot ...of: delimiters,,, Ryan'
>>> s.replace(":","")
'  There... are... a... lot ...of delimiters,,, Ryan?!!!'
>>> s.replace("...",",,,","?!!!",":","")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    s.replace("...",",,,","?!!!",":","")
TypeError: replace expected at most 3 arguments, got 5
>>> s = "  There... are... a... lot ...of: delimiters,,, Ryan?!!!"
>>> s.replace("...","")
'  There are a lot of: delimiters,,, Ryan?!!!'
>>> S = '  There are a lot of: delimiters,,, Ryan?!!!'
>>> s.replace(",,,","")
'  There... are... a... lot ...of: delimiters Ryan?!!!'
>>> s = "  There... are... a... lot ...of: delimiters,,, Ryan?!!!"
>>> replace("...","")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    replace("...","")
NameError: name 'replace' is not defined
>>> s = "  There... are... a... lot ...of: delimiters,,, Ryan?!!!"
>>> S.replace("...","")
'  There are a lot of: delimiters,,, Ryan?!!!'
>>>  p = "A man, a plan, a canal... Panama!"
 
SyntaxError: unexpected indent
>>>  p = "A man, a plan, a canal... Panama!"
 
SyntaxError: unexpected indent
>>> p = "A man, a plan, a canal... Panama!"
>>> s = p
>>> s.replace(",", "")
'A man a plan a canal... Panama!'
>>> s
'A man, a plan, a canal... Panama!'
>>> s = s.replace(",","")
>>> s
'A man a plan a canal... Panama!'
>>> s = s.replace("!","")
>>> s
'A man a plan a canal... Panama'
>>> s = s.replace(" ","")
>>> s
'Amanaplanacanal...Panama'
>>> s = p
>>> s
'A man, a plan, a canal... Panama!'
>>> for ch in ", . !":
	s = s.replace(ch, "")

	
>>> s
'AmanaplanacanalPanama'
>>> s = s.lower()
>>> s
'amanaplanacanalpanama'
>>> s = " Now is the time for ... what exactly?"
>>> s
' Now is the time for ... what exactly?'
>>> s = s.replace("?","").replace(".","")
>>> s
' Now is the time for  what exactly'
>>> s = s.lstrip()
>>> s
'Now is the time for  what exactly'
>>> idx = s.find(' ')
>>> s
'Now is the time for  what exactly'
>>> idx
3
>>> s[ : idx]
'Now'
>>> s[ idx: ]
' is the time for  what exactly'
>>> s = s[ idx: ].lstrip()
>>> s
'is the time for  what exactly'
>>> s = "  There... are... a... lot ...of: delimiters,,, Ryan?!!!"
>>> s = s.replace("?","").replace(".","").replace("!","")
>>> s
'  There are a lot of: delimiters,,, Ryan'
>>> s = s.replace(":","").replace(",","")
>>> s
'  There are a lot of delimiters Ryan'
>>> s[ : idx]
'  T'
>>> s = s.lstrip()
>>> s
'There are a lot of delimiters Ryan'
>>> idx = s.find('s')
>>> s = s.replace("s","s,")
>>> s
'There are a lot of delimiters, Ryan'
>>> s = s.replace("Ryan", "Fred")
>>> s
'There are a lot of delimiters, Fred'
>>> s.split(',')
['There are a lot of delimiters', ' Fred']
>>> s
'There are a lot of delimiters, Fred'
>>> s.split(' ')
['There', 'are', 'a', 'lot', 'of', 'delimiters,', 'Fred']
>>> 