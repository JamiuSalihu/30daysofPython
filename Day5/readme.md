# Day-5 of 30daysofPython

# Output Statements
.print( ) statement
.end( ) attribute
.sep( ) attribute
# print statement with '{ }' Replacement operator
- print statement with formatted string
print( ) statement
print( ) statement is used to print the output print('a') # Since 'a' is string it prints 'a' but print(a) gives error if a is not initialised

a = 10 print(a)

- end() attribute
This attribute is used if we need the output in a single line. Example a =[10,20,30,40,50,60] for i in a: print(i)

- sep( ) attribute
This attribute used to seperate two different outputs

# Examples

print('09','30','1999', sep='-')

Using end( ) and sep( ) in a single line
print(9,30,1999,sep=':',end='!')

print( ) statement with replacemenet operator {}

# Examples

a = 'Salihu' b = 'Hello' print("{} {}!,how are you?".format(a,b))

Replacement Operator based on Index

# Example:

Age = 26 Goal = 'Data Scientist' Name = 'Salihu' print("Hello {2}, your age is {1}, your goal is to become a {0}".format(Goal,Age,Name))

print( ) with formatted string
'%i' (Signed Decimal Value) 
'%d' (Signed Decimal Value) 
'%f' (Signed float Value) '
%s' (String, list, set type)