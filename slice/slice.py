#[being:end:steps] Steps values can be positive or negative value
# If steps value is positive then
  # left to right (Forward direction) - Begin to end - 1
# if steps value is negitive then
  # right to left (Backward direction)  - Begin to end + 1
string ='abcdefghij'
print(string[1:6:2]) # begin from 1 and end 6 that is begin with -1
print(string[::1]) # Default value is begin and end is by default in increment with 1
print(string[::-1]) # this is a negative steps that means backward direction
print(string[3:7:-1]) # 3 to 8 value should print but as this is backward direction we are not going to get 8 value in backward direction so its empty string, 
print(string[7:4:-1]) # we are going to get result
print(string[0:1000:1]) # print all slice 
print(string[-4:1:-1]) # begine to end + 1 and backward direction
print(string[0:3])
print(string[1::2]) # print character after 2 iteration
#print(string[-1:-9:-0]) #slice step cannot be zero
print(string[-1:-9:-2])
print(string[:5]) # 0 is default value and its being value
print(string[0:]) # if end is not mentioned its will take all value
print(string[:]) # total value going to display
print(string[::2])
