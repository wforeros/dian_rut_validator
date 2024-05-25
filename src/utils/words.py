from typing import Dict, List
import re

def count_words(dictionary: Dict, ignore: List[str]) -> int:
  ignore = ignore if isinstance(ignore, List) else [ignore]
  ignore = [item.lower() for item in ignore]
  words = 0
  print(dictionary)
  for item in dictionary.items():
    value = item[1]
    if item[0].lower() not in ignore and value:
      words += len(value.split(' '))
  return words

def remove_multiple_spaces(value: str) -> str:
  return re.sub(r'\s+', ' ', value)