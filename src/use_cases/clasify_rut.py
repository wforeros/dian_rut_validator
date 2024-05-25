def clasify_rut(rut_info):
  if not rut_info:
    print('RUT inválido o no se encuentra en la página correcta')
    return ''
      
  primer_nombre = rut_info.setdefault('primer_nombre', '')
  otros_nombres = rut_info.setdefault('otros_nombres')
  primer_apellido = rut_info.setdefault('primer_apellido')
  segundo_apellido = rut_info.setdefault('segundo_apellido')
  has_all_props = primer_nombre and otros_nombres and primer_apellido and segundo_apellido
  if has_all_props:
    return ''
  elif primer_nombre and primer_apellido and segundo_apellido:
    return 'A'
  elif primer_nombre and otros_nombres and primer_apellido and not segundo_apellido:
    return 'N'
  elif primer_nombre and primer_apellido:
    return ''
  elif primer_nombre:
    return 'RS'
  else:
    return 'Desconocido'

