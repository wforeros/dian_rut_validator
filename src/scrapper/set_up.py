
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Configurar las opciones de Chrome

def load_driver():
  print('Loading options...')
  chrome_options = Options()
  chrome_options.add_argument("--window-size=1920,1080")
  chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
  print('Loading driver...')

  # Crear una instancia del controlador de Chrome
  driver = webdriver.Chrome(options=chrome_options)
  print('Driver loaded')
  return driver