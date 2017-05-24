def palindrome(string):
    result = True
    str_len = len(string)
    for i in range(0, int(str_len/2)):
      if string[i] != string[str_len-i-1]:
            result = False
            break
    return result


s = input("enter the string:")
string = palindrome(s)
print(string)
