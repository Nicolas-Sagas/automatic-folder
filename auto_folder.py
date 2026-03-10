import os
from datetime import datetime
import ctypes # pop-up
import dotenv

def organizar_dia():
    # onde a pasta está. 
    diretorio_base = dotenv.get_key(dotenv.find_dotenv(), "diretorio_base")
    
    # Obtém a data atual formatada (ex: 10.03)
    hoje = datetime.now().strftime("%d.%m")
    caminho_completo = os.path.join(diretorio_base, hoje)

    if not os.path.exists(caminho_completo):
        try:
            os.makedirs(caminho_completo)
            # pop-up
            ctypes.windll.user32.MessageBoxW(0, f"Pasta {hoje} criada com sucesso!", "Automatizado", 64)
        except Exception as e:
            ctypes.windll.user32.MessageBoxW(0, f"Erro ao criar pasta: {e}", "Erro", 16)
    
    # O script encerra sozinho após a verificação/criação

if __name__ == "__main__":
    dotenv.load_dotenv()
    organizar_dia()