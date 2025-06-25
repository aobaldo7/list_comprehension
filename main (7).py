def convert_to_snake_case(pascal_or_camel_case_string):
  converted_pascal_or_camel_sting=[
    '_'+char.lower() if char.isupper()
    else char 
    for char in pascal_or_camel_case_string
  ]
  return ''.join(converted_pascal_or_camel_sting).strip('_')

def main():
  print('Welcome to my Snake Case Converter!\n')
  pascal_or_camel_case_string=input('Type your Pascal or Camel case sting: ')
  print(f'Here is your convertion {convert_to_snake_case(pascal_or_camel_case_string)}')
  
main()
