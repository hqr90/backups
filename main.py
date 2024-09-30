import zipfile
import os
from datetime import datetime
import yaml


def zipar_pastas(pastas_para_backup, caminho_zip):
    try:
        with zipfile.ZipFile(caminho_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for pasta in pastas_para_backup:
                pasta_base = os.path.basename(pasta.rstrip(os.sep))
                for raiz, dirs, arquivos in os.walk(pasta):
                    for arquivo in arquivos:
                        caminho_arquivo = os.path.join(raiz, arquivo)
                        arcname = os.path.join(pasta_base, os.path.relpath(caminho_arquivo, pasta))
                        zipf.write(caminho_arquivo, arcname)
        print(f"Backup criado com sucesso em: {caminho_zip}")
        return True, None  # Retorna sucesso e nenhum erro
    except Exception as e:
        print(f"Erro ao criar backup: {e}")
        return False, str(e)  # Retorna falha e a mensagem de erro


def atualizar_log(arquivo_log, entrada_log):
    if os.path.exists(arquivo_log):
        with open(arquivo_log, 'r', encoding='utf-8') as f:
            logs = yaml.safe_load(f)
            if logs is None:
                logs = []
    else:
        logs = []

    logs.append(entrada_log)

    with open(arquivo_log, 'w', encoding='utf-8') as f:
        yaml.safe_dump(logs, f, default_flow_style=False, allow_unicode=True)


if __name__ == "__main__":
    pastas_para_backup = [r'E:\flutter', r'E:\python']  # Pastas que deseja fazer backup
    diretorio_backup = r'F:\backups'  # Diretório onde o backup será salvo

    # Garantir que o diretório de backup existe
    if not os.path.exists(diretorio_backup):
        os.makedirs(diretorio_backup)

    # Gerar o nome do arquivo zip com o formato yyyyMMdd_backupCode.zip
    data_atual = datetime.now()
    data_formatada = data_atual.strftime('%Y%m%d')
    nome_zip = f"{data_formatada}_backupCode.zip"
    caminho_zip = os.path.join(diretorio_backup, nome_zip)

    # Realizar o backup
    sucesso, erro = zipar_pastas(pastas_para_backup, caminho_zip)

    # Criar entrada de log
    entrada_log = {
        'data': data_atual.strftime('%Y-%m-%d %H:%M:%S'),
        'pastas_backup': pastas_para_backup,
        'arquivo_backup': caminho_zip,
        'status': 'Sucesso' if sucesso else 'Falha',
        'erro': erro
    }

    # Atualizar o arquivo de log YAML
    arquivo_log = os.path.join(diretorio_backup, 'backup_log.yaml')
    atualizar_log(arquivo_log, entrada_log)
