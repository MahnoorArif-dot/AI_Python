def reverse_string(a):
  if len(a) == 0:
    return ""
  else:
    return a[-1] + reverse_string(a[:-1])

a=input('Enter a string:')
reverse = reverse_string(a)
print('Reverse String:',reverse)  
