""" lo voy a guardar ya que siempre se me olvida como crear un entorno virtual.
python -m venv venv          # crea un entorno virtual llamado 'venv'
source venv/bin/activate     # activa el entorno virtual (Linux/Mac)
venv\Scripts\activate        # activa el entorno virtual (Windows)""" 
"""
requirements.txt:
pip install matplotlib          # instala la ultima version publicada
pip install matplotlib==3.9.0   # instala una version exacta
pip list                        # lista lo instalado en este interprete
pip freeze                      # lo mismo, en el formato que espera requirements.txt
"""
def es_primo(numero: int) -> bool:
    """Determina si un numero es primo."""
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True
 
 
def main() -> None:
    """Punto de entrada del script."""
    print(es_primo(17))
 
 
if __name__ == "__main__":
    main()