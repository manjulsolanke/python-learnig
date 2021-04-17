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



Immunitability 

- fundamental data types provide immutability to re-use the object. However, complex data-type doesn't perovide object re-usability, its provide only immunitability.


### Collection related data types: 

- List 
- Tuple
- Set
- Frozenset
- Dist
- Range
- Byte 
- Byterange

[10,20,30] - list
{10,20,30} - set
(10,20,30) - Tuple
{100:'Manjul', 200:'Solanke'} dist

### List: 
 
 1) Orders perserved.
 2) Duplicate objects are allowed.
 3) heterogeneous objects are allowed.
 4) indexing concept are applicable.
 5) Slice operators also applicable.
 6) We can append and remove the objects in list. It also called "growable list".
 7) List is mutable.

### Tuple: 

  1) Same as list except that it is an     immutable data type.
  2) Read only version of list is tuple
  3) 

Difference between List and Tuple

| List          | Tuple         |
| ------------- | ------------- |
| Mutable       | immutable     |
| []            | ().           |
| More memory.  | Less memory.  |
| slow performace| fast performance|   


### set
  - Oder doesn't matter.
  - Duplicates are not allowed.
  - Indexing and slicing not possible
  - Heterogeneous objects are allowed.
  - Add can be added in set.
  - Set is growable.
  - Set is mutable.

### Frozenset
  - Its immutable 
  - Duplicate not allowed
  - Order is not applicable


### Dict
   - Meant to represent the group of keys and values.
   - Order not preserved.
   - Duplicate key are not allowed.
   - Duplicate value are allowed.
   - Heterogeneouse object allowed.
   - Dict is muteable.
   - Indexing and slacing not applicable.

### Range   
   - Oder is preserved 
   - Indexing and slicing is applicable
   - Range is immutiable
   - Three form is available 1) range(10) 2) range(10,21) 3) range(10,20,30)

### Bytes 
   - Immuteable data types

### Bytearray
    - muteable
    - Values should be range betweem 0 - 255

### None



## Python operator

###  Arithmetic operator

1) Addition (+)
2) Substraction (-)
3) Mutiplications (*)
4) Division operator(/) # Alway doing to provide floating point value 
5) Modulo operator (%)
6) Floor Division operator(//) # "//" is going to provide integral and floating values.
7) Exponent operator or Power operator(**)

###  Relational operator
1) Relational operator can be applied for numbers, string and boolean value as well. 
2) Chaining of relational operator is possible. In the chaining, if all  comparisons return True then only result is True. If atleast one  comparison returns False then the results is False

#### BitWise operator
  
  & -> bitwise and
  | -> bitwise or
  ^ -> bitwise x-or 
  ~ -> bitwise complement operator
  << -> bitwise left shift operator
  >> -> bitwise right shift operator

