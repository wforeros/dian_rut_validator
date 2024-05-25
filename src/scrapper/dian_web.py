# import random
# from time import sleep
import random
from time import sleep
from selenium.webdriver.common.by import By
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

from scrapper.set_up import load_driver



class DianRutSearcher(): 
  def __init__(self):
    self.driver = load_driver()
    self.driver.get("https://muisca.dian.gov.co/WebRutMuisca/DefConsultaEstadoRUT.faces")
    self.reset_search()
    self.active_identifier = 'Registro Activo'

  def search_rut(self, rut):
    self.driver.find_element(By.ID, "vistaConsultaEstadoRUT:formConsultaEstadoRUT:numNit").send_keys(rut)
    self.__sleep_approx(1.2)
    self.driver.find_element(By.ID, "vistaConsultaEstadoRUT:formConsultaEstadoRUT:btnBuscar").click()
    if self.__is_valid_rut():
      print('RUT {rut} con estado "{status}"'.format(rut=rut, status=self.active_identifier))
    else:
      print('RUT inválido o no se encuentra en la página correcta ' + str(rut))

  def get_rut_info(self):
    self.__sleep_approx(1.2)
    if not self.__is_valid_rut():
      print('RUT inválido o no se encuentra en la página correcta')
      return {}
    try:
      self.driver.find_element(By.ID, 'vistaConsultaEstadoRUT:formConsultaEstadoRUT:primerApellido')
      return self.__process_person()
    except:
      return self.__process_company()
  
  def __process_person(self):
    apellido = self.driver.find_element(By.ID, 'vistaConsultaEstadoRUT:formConsultaEstadoRUT:primerApellido').text
    segundo_apellido = self.driver.find_element(By.ID, 'vistaConsultaEstadoRUT:formConsultaEstadoRUT:segundoApellido').text
    primer_nombre = self.driver.find_element(By.ID, 'vistaConsultaEstadoRUT:formConsultaEstadoRUT:primerNombre').text
    otros_nombres = self.driver.find_element(By.ID, 'vistaConsultaEstadoRUT:formConsultaEstadoRUT:otrosNombres').text
    return {
      'primer_nombre': primer_nombre,
      'otros_nombres': otros_nombres,
      'primer_apellido': apellido,
      'segundo_apellido': segundo_apellido
    }

  def __process_company(self):
    razon_social = self.driver.find_element(By.ID, 'vistaConsultaEstadoRUT:formConsultaEstadoRUT:razonSocial').text
    return {
      'primer_nombre': razon_social,
    }

  def reset_search(self):
    self.__sleep_approx(1.2)
    self.driver.find_element(By.ID, "vistaConsultaEstadoRUT:formConsultaEstadoRUT:numNit").clear()
    
  def __is_valid_rut(self):
    try:
      text = self.driver.find_element(By.XPATH, '//*[@id="vistaConsultaEstadoRUT:formConsultaEstadoRUT"]/table[2]/tbody/tr[2]/td/table/tbody/tr[4]/td/table/tbody/tr/td').text
      return self.active_identifier in text
    except:
      return False
     
  
  def __sleep_approx(self, seconds):
    """
    Randomizes sleep to avoid any blocker.
    """
    upperbound = (seconds+0.2)*10000
    if (seconds >= 1):
        lowerbound = (seconds-0.2)*10000
    else:
        lowerbound = seconds*10000

    lowerbound = int(lowerbound)
    upperbound = int(upperbound)

    sleeptime = random.randint(lowerbound, upperbound)
    sleeptime = sleeptime/10000
    sleeptime = sleeptime*.8

    print("Sleeping for", sleeptime, "seconds")
    sleep(sleeptime)