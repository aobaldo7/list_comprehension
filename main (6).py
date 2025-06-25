def convert_to_snake_case(pascal_or_camel_case_string):
  converted_pascal_or_camel_sting=[
    '_'+char.lower() if char.isupper()
    else char 
    for char in pascal_or_camel_case_string
  ]
  return ''.join(converted_pascal_or_camel_sting).strip('_')

def main (pascal_or_camel_case_string):
  print('Snake Case Converter:')
  print(f'\nPascal or Camel case string: {pascal_or_camel_case_string}')
  print(f'\nCovertion to snake case: {convert_to_snake_case(pascal_or_camel_case_string)}')

main('Klk_los_mios')
