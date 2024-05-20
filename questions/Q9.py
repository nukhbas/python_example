
def is_member(ele, lst):
  for e in lst:
    if ele == e:
      return True
  return False
if __name__ == '__main__':
  print(is_member("e", ['a', 'e', 'i', 'o', 'u']))
  print(is_member(67, [1,7,4,8,23,20]))


