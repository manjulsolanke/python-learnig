#[being:end:steps] Steps values can be positive or negative value
# If steps value is positive then
  # left to right (Forward direction) - Begin to end - 1
# if steps value is negitive then
  # right to left (Backward direction)  - Begin to end + 1
string ='abcdefghij'
print(string[0:3])
print(string[1::2]) # print character after 2 iteration
#print(string[-1:-9:-0]) #slice step cannot be zero
print(string[-1:-9:-2])
print(string[:5]) # 0 is default value and its being value
print(string[0:]) # if end is not mentioned its will take all value
print(string[:]) # total value going to display
print(string[::2])