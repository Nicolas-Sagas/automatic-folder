import os
from datetime import datetime
import ctypes  # Para criar um alerta visual simples se desejar
import dotenv

def organizar_dia():
    # onde a pasta está. 
    diretorio_base = os.getenv("diretorio_base")
    
    # 2. tem a data de hoje.
    hoje = datetime.now().strftime("%d.%m")
    caminho_completo = os.path.join(diretorio_base, hoje)

    if not os.path.exists(caminho_completo):
        try:
            os.makedirs(caminho_completo)
            # pop-up
            ctypes.windll.user32.MessageBoxW(0, f"Pasta {hoje} criada com sucesso!", 64)
        except Exception as e:
            ctypes.windll.user32.MessageBoxW(0, f"Erro ao criar pasta: {e}", 16)
    
    # O script encerra sozinho após a verificação/criação

if __name__ == "__main__":
    dotenv.load_dotenv()
    organizar_dia()