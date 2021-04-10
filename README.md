# python learning.

# fundamentals of language
  1) Identifiers. 
     
Any names called Identifiers such as variable , method and class name.

Roles:

     1) cash - is valid
     2) ca$h - invalid
     3) total123 - valid
     4) 123total - invalid
     5) all@vars - invalid
     6) java2share - valid
     7) if - reserved words are invalid to use
     8) __add__ : valid

```bash
     _x   : Called protected variables
     __x  : private variables
     __x__: Magic variables
```
     
     
  2) Reserved words/keywords 
     
Python have 33 reserved words.
     True, False, None, and, or, not, if, elif, else, while, for, break, continue, return, in, yield,
     try, except, finally, raise, is, assert, import, from, as, class, def, pass, global, nonlocal, lambda, del, with
# Data types

    int (10)
    float  (10.5)
    boolean ( True, false)
    complex
    str
    list
    tuple
    set
    frozenset
    dict
    bytes
    bytesarray
    range
    None
    
int, float, complex, boolean and str called as fundamental data types
  
 
    1) Base conversion functions. 
    bin()
    oct()
    hex()

    2) string data types
    A) triple quotes
    i) To define multiline string literals  
    ii) To use '  and " as normal charactor in string
    iii) To use in docs string
  - Python support positive and negative index.  
  - python doesn't support the mix dataTypes in str in concatenation. Example s="apple" + "10"
### Type casting
There are five type casting in-built functions. 
1) int()
2) float()
3) complex()
4) bool()
6) str()
Complex type can't be converted to the int data types.
   
Table of type casting.

| argument_type /Type_casting function |int arg | float arg | complex arg |bool arg | str arg | 
| :---: | :---: | :---: | :---: | :---: | :---: 
| int() | Yes | int(10.0) = 10 |No |int(True) = 1 & int(False) = 0| contains only int value with base 10|
| float() | float(10) = 10.0 | Yes | No|float(True) = 1.0 & float(False) = 0.0 |int or float value only  | 
| Complex() | complex(10) = 10+0j & complex(10,20) 10+20j| Yes | Yes |Yes |Yes |
| bool() | Yes | Yes | Yes| Yes |Yes(IMP) |
| str() | Yes | Yes | Yes| Yes |Yes |
