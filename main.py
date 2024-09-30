import zipfile
import os
from datetime import datetime


def zipar_pastas(pastas_para_backup, caminho_zip):
    with zipfile.ZipFile(caminho_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for pasta in pastas_para_backup:
            pasta_base = os.path.basename(pasta.rstrip(os.sep))
            for raiz, dirs, arquivos in os.walk(pasta):
                for arquivo in arquivos:
                    caminho_arquivo = os.path.join(raiz, arquivo)
                    arcname = os.path.join(pasta_base, os.path.relpath(caminho_arquivo, pasta))
                    zipf.write(caminho_arquivo, arcname)
    print(f"Backup criado com sucesso em: {caminho_zip}")


if __name__ == "__main__":
    pastas_para_backup = [r'E:\flutter', r'E:\python']  # Liste aqui as pastas que deseja fazer backup
    diretorio_backup = r'F:\backups'  # Diretório onde o backup será salvo

    # Garantir que o diretório de backup existe
    if not os.path.exists(diretorio_backup):
        os.makedirs(diretorio_backup)

    # Gerar o nome do arquivo zip com o formato yyyyMMdd_backupCode.zip
    data_atual = datetime.now().strftime('%Y%m%d')
    nome_zip = f"{data_atual}_backupCode.zip"
    caminho_zip = os.path.join(diretorio_backup, nome_zip)

    # Realizar o backup
    zipar_pastas(pastas_para_backup, caminho_zip)
