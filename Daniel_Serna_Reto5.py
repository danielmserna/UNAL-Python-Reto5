def tipos_lamina(tipoTodasLaminas):
  tiposLamina = []
  for i in range(0, len(tipoTodasLaminas)):
    if(not tipoTodasLaminas[i] in tiposLamina):
        tiposLamina.append(str(tipoTodasLaminas[i]))
  print(tiposLamina)
  return 

def laminas_faltantes_tipo(numeroLaminasFaltan, listaTiposCadaLamina, tipoLamina):
  listaNumerosDichaClaseQueFalta = []
  for i in range(0, len(listaTiposCadaLamina)):
    if(listaTiposCadaLamina[i] == tipoLamina and i in numeroLaminasFaltan):
      listaNumerosDichaClaseQueFalta.append(str(i))
  print(listaNumerosDichaClaseQueFalta)
  return 

def me_faltan(laminasIntercambiablesOtraPersona, laminasQueTengo):
  meFaltan = []
  for i in range(0, len(laminasIntercambiablesOtraPersona)):
    if(not laminasIntercambiablesOtraPersona[i] in laminasQueTengo):
      meFaltan.append(str(laminasIntercambiablesOtraPersona[i]))
  print(meFaltan)
  return

def cambiar(laminasQueTieneOtraPersona, laminasQueTengo):
  puedoCambiar = []
  for i in range(0, len(laminasQueTengo)):
    if(not laminasQueTengo[i] in laminasQueTieneOtraPersona):
      puedoCambiar.append(str(laminasQueTengo[i]))
  print(str(len(puedoCambiar)))
  return

laminas_faltantes_tipo([4, 10, 14, 22, 7, 5, 13, 6],[3, 2, 2, 1, 2, 2, 4, 1, 3, 3, 2, 3, 2, 2, 4, 3, 4, 1, 3, 1, 3, 1, 3],4)
tipos_lamina([3, 3, 2, 3, 3, 1, 3, 2, 1, 3, 1, 3])
me_faltan([7, 5, 13, 16, 10, 17, 6, 2, 18, 9],[10, 8, 4, 16, 5, 11, 0])
cambiar([12, 1, 8, 9, 10, 3],[12, 9, 13, 2, 8])