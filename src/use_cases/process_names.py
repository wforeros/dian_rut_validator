from utils.arrays import replace_none_with_empty_str
from utils.words import count_words, remove_multiple_spaces


def unify_names(rut_info):
  normalized_rut = {}
  for item in rut_info.items():
    value = item[1]
    if value and len( value.split(' ')) > 1:
      value = value.replace(' ', '')
    normalized_rut[item[0]] = value
  return normalized_rut

def normalize(rut_info):
  rut_info.setdefault('primer_nombre', '')
  rut_info.setdefault('otros_nombres', '')
  rut_info.setdefault('primer_apellido', '')
  rut_info.setdefault('segundo_apellido', '')
  rut_info.setdefault('clasificación', '')
  rut_info = replace_none_with_empty_str(rut_info)
  if count_words(rut_info, 'rut') > 4:
    rut_info = __compact_props(rut_info)
    rut_info['compactado'] = True
  name =  remove_multiple_spaces(f"{rut_info['primer_nombre']} {rut_info['otros_nombres']} {rut_info['primer_apellido']} {rut_info['segundo_apellido']}")
  rut = {
    'clasificación': rut_info['clasificación'],
    'rut': rut_info['RUT'],
    'nombre': name,
  }
  return rut

def __compact_props(rut_info):
  for item in rut_info.items():
    value = item[1]
    if value and len(value.split(' ')) > 1:
      value = value.replace(' ', '')
    rut_info[item[0]] = value
  return rut_info
