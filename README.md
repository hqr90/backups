# Sumário

- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Automatização do Backup](#automatização-do-backup)
- [Personalização](#personalização)
- [Considerações Adicionais](#considerações-adicionais)

---

## Pré-requisitos

- **Python 3.x** instalado no seu sistema.
- Permissões de leitura nas pastas de origem (`E:\flutter` e `E:\python`).
- Permissões de escrita no diretório de destino (`F:\backups`).

## Instalação

1. **Clone ou baixe** este repositório para o seu computador.
2. **Verifique** se os caminhos das pastas no script correspondem aos seus diretórios locais:
   ```python
   pastas_para_backup = [r'E:\flutter', r'E:\python']
   diretorio_backup = r'F:\backups'
   ```
3. **Certifique-se** de que o diretório de backup (`F:\backups`) existe. O script tentará criá-lo se não existir.

## Como Usar

1. **Abra** o prompt de comando ou terminal.

2. **Navegue** até o diretório onde o script está localizado:
   ```bash
   cd caminho\para\o\diretório\do\script
   ```

3. **Execute** o script:
   ```bash
   python backup_script.py
   ```
   - Se o Python não estiver adicionado ao PATH, você precisará fornecer o caminho completo para o interpretador Python:
     ```bash
     C:\Python39\python.exe backup_script.py
     ```

4. **Verifique** se o arquivo zip foi criado no diretório `F:\backups`. O arquivo terá um nome como `20231005_backupCode.zip`.

## Automatização do Backup

Para agendar a execução automática do script, siga os passos abaixo:

### Usando o Agendador de Tarefas do Windows

1. **Abra** o Agendador de Tarefas:
   - Pressione `Win + R`, digite `taskschd.msc` e pressione `Enter`.

2. **Crie** uma nova tarefa básica:
   - Clique em **Ação** > **Criar Tarefa Básica**.

3. **Configure** a tarefa:
   - **Nome**: "Backup Automático de Código".
   - **Disparador**: Defina a frequência (diariamente, semanalmente, etc.) e o horário em que o backup deve ser executado.
   - **Ação**: Selecione **Iniciar um programa**.
     - **Programa/script**: Caminho para o interpretador Python, por exemplo, `C:\Python39\python.exe`.
     - **Adicionar argumentos**: Caminho completo para o script, por exemplo, `C:\caminho\para\backup_script.py`.
   - **Finalizar** a configuração da tarefa.

4. **Permissões**:
   - Na guia **Geral** da tarefa, marque a opção **Executar com os privilégios mais altos**.
   - Certifique-se de que o usuário configurado para executar a tarefa tem as permissões necessárias.

## Personalização

### Adicionar Mais Pastas ao Backup

Para incluir mais pastas no backup, adicione os caminhos à lista `pastas_para_backup`:
```python
pastas_para_backup = [r'E:\flutter', r'E:\python', r'E:\meu_projeto']
```

### Alterar o Diretório de Backup

Para alterar onde o arquivo zip será salvo, modifique a variável `diretorio_backup`:
```python
diretorio_backup = r'G:\meus_backups'
```

## Considerações Adicionais

- **Espaço em Disco**: Verifique regularmente o espaço disponível em `F:\backups` para evitar falhas no backup devido a falta de espaço.
- **Integridade dos Dados**: Periodicamente, teste os arquivos de backup para garantir que estão íntegros e podem ser extraídos sem erros.
- **Segurança**: Se os arquivos contêm informações sensíveis, considere proteger o arquivo zip com senha ou usar métodos de criptografia.

### Logs de Execução

Para adicionar logs que registram o sucesso ou falha de cada execução:

1. Importe o módulo `logging` no início do script:
   ```python
   import logging
   ```

2. Configure o logging após os imports:
   ```python
   logging.basicConfig(filename='backup_log.txt', level=logging.INFO,
                       format='%(asctime)s - %(levelname)s - %(message)s')
   ```

3. Adicione mensagens de log no script:
   ```python
   logging.info("Backup iniciado.")
   # Após a conclusão do backup
   logging.info("Backup concluído com sucesso.")
   ```

Os logs serão salvos no arquivo `backup_log.txt` no mesmo diretório do script.

## Contato

Para dúvidas ou sugestões:

- **Email**: rebello.hiltonqueiroz@gmail.com
- **Telefone**: (27) 99578-2206
