# importando as duas bibliotecas
import pyautogui as pa
import time

time.sleep(1)
pa.press("win")
time.sleep(1)
pa.write("chrome")
time.sleep(4)
pa.press("enter")
time.sleep(5)
pa.write("https://outlook.com/login")
time.sleep(1)
pa.press("enter")
time.sleep(4)
pa.write("rodineywan@outlook.com")
time.sleep(3)
pa.press("enter")
time.sleep(4)

# Caso não tenha a senha salva.
# pa.write("*********")
# time.sleep(3)
# pa.press("enter")

pa.click(x=131, y=191)
time.sleep(2)
pa.write("rodineyw@yahoo.com.br")
time.sleep(1)
pa.press("enter")
time.sleep(1)
pa.press("tab")
time.sleep(1)
pa.write("Rodiney Wanderson")
time.sleep(1)
pa.press("tab")
pa.write("""
Temos informações importantes.
""")

time.sleep(3)
pa.click(x=449, y=255)
