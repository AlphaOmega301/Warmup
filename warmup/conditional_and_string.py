#data type
"""
digit1 = 10
digit2 = 2.2
string1 = "something"
print(type(digit1))
print(type(digit2))
print(type(string1))
"""
#\n : 줄바꿈, \t : 간격(tab)
"""
print('123456\n1234567\t12345678\t123456')
#if~elif~else
num1 = input()
num2 = input()
if int(num1) > int(num2) : #int로 type변환
    print(num1)
else :
    print(num2)
    """
#strip : 문자열 양 끝 제거(lstrip은 좌측 rstrip은 우측)
"""
mystr = "a man. goes into the room..."
print(mystr.strip())
code = '     000660\n      '
print(code.strip(' \n'))
"""
#count
"""
python_desc = "Python is an interpreted high-level programming language or general-purpose programming. Created by Guido van Rossum and First released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant witespace"
ct_Python = python_desc.count("Python")
print (ct_Python)
print (python_desc.count("p"))
"""
#find
"""
letters = input()
if letters.find("n") >= 0 :
    print("n 이 들어있습니다.")
else :
    print("n 이 들어있지 않습니다.")
"""
#split
"""
letters = "Dave,David,Andy,222,3123123,LLL"
letter_list = letters.split(",")
print (letter_list)
print (letter_list[1])
for letter in letter_list:
    print(letter)

filename = "exercise01.docx"
print(filename.split(".")[0])
"""