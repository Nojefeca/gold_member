import os

def funcion_insegura(user_input):
    # Vulnerabilidad de Command Injection detectada por Semgrep
    os.system(user_input)
