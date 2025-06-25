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
  print(f'\nHere is your convertion {convert_to_snake_case(pascal_or_camel_case_string)}\n')
  while True:     
    choice=input('Do you wish to try again. Type "yes" or "no": ')
      
    if choice=='yes':
      print('\nWelcome to my Snake Case Converter!\n')
      pascal_or_camel_case_string=input('Type your Pascal or Camel case sting: ')
      print(f'\nHere is your convertion {convert_to_snake_case(pascal_or_camel_case_string)}\n')
      
    elif choice == 'no':
      print('\nThank you for participating')
      break  
    
main()
