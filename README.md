# Backups

**Backups** é uma aplicação Python com interface gráfica desenvolvida usando PyQt5, destinada a facilitar a configuração e gerenciamento de backups automáticos de pastas específicas no seu sistema. A aplicação permite selecionar pastas para backup, definir o diretório de destino para os backups, e especificar a quantidade de dias para manter os backups. Os backups são armazenados em arquivos ZIP, e logs das operações são mantidos em arquivos YAML.

## 🛠️ **Recursos**

- **Interface Gráfica Intuitiva:** Configure facilmente as pastas a serem incluídas no backup e o diretório de destino.
- **Configuração Flexível:** Defina quantos dias deseja manter os backups, garantindo a gestão eficiente do espaço em disco.
- **Automatização de Backups:** Automatize a criação de backups e a limpeza de backups antigos.
- **Logs Detalhados:** Mantenha registros das operações de backup para monitoramento e auditoria.

## 📋 **Instalação**

### 1. Clone o Repositório

```bash
git clone https://github.com/hqr90/backups.git
cd backup-manager
```

### 2. Crie e Ative um Ambiente Virtual (Recomendado)

#### **No Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### **No Linux/Mac:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instale as Dependências

Com o ambiente virtual ativado, instale as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

**Nota:** Se o arquivo `requirements.txt` não estiver disponível, instale as bibliotecas manualmente:

```bash
pip install PyQt5 ruamel.yaml
```

## 🏃 **Uso**

### 1. Executando o Script

Com o ambiente virtual ativado e as dependências instaladas, execute o script:

```bash
python main.py
```

### 2. Configuração Inicial

- **Adicionar Pastas para Backup:** Clique em "Adicionar Pasta para Backup" e selecione as pastas que deseja incluir no backup.
- **Remover Pastas Selecionadas:** Selecione uma pasta na lista e clique em "Remover Pasta Selecionada" para removê-la.
- **Selecionar Diretório de Backup:** Clique em "Selecionar Diretório de Backup" e escolha onde os backups serão armazenados.
- **Definir Dias para Manter os Backups:** Use o campo "Dias para manter os backups" para definir quantos dias deseja manter os backups. O valor padrão é 365 dias.
- **Salvar Configuração:** Após configurar, clique em "Salvar Configuração". O arquivo `backup_config.yaml` será salvo no diretório de backup especificado, e o backup será realizado automaticamente.

### 3. Execuções Futuras

Nas próximas execuções, o script utilizará as configurações existentes sem exibir a janela de configuração, a menos que o arquivo `backup_config.yaml` seja removido do diretório de backup.

## 📂 **Estrutura dos Arquivos**

- **`main.py`:** Script principal da aplicação.
- **`backup_config.yaml`:** Arquivo de configuração contendo:
  - `pastas_para_backup`: Lista de pastas a serem incluídas no backup.
  - `diretorio_backup`: Diretório onde os backups e logs serão armazenados.
  - `dias_para_manter`: Número de dias para manter os backups.
- **`backup_log.yaml`:** Log das operações de backup realizadas.
- **`requirements.txt`:** (Opcional) Lista de dependências do projeto.

## 🔧 **Criação de um Executável**

Para facilitar a distribuição e execução da aplicação sem a necessidade de um ambiente Python configurado, você pode transformar o script em um executável, siga o passo-a-passo de como fazer isso em [py2exe](https://github.com/hqr90/py2exe/edit/master/README.md), ou se preferir utilize a biblioteca PyInstaller.

### 3. Executando o Executável

Navegue até a pasta `dist` e execute o arquivo `main.exe` (no Windows) ou correspondente no seu sistema operacional.

## 🗓️ **Agendamento com o Agendador de Tarefas do Windows**

Para automatizar a execução do backup, você pode agendar o executável criado para rodar em intervalos regulares usando o **Agendador de Tarefas do Windows**.

### Passo a Passo:

1. **Abrir o Agendador de Tarefas:**
   - Pressione `Win + R`, digite `taskschd.msc` e pressione `Enter`.

2. **Criar uma Nova Tarefa:**
   - No painel direito, clique em **"Criar Tarefa"**.

3. **Configurar a Tarefa:**
   - **Geral:**
     - Dê um nome para a tarefa, por exemplo, "Backup Manager".
     - Marque "Executar com privilégios mais altos".
   - **Disparadores:**
     - Clique em "Novo..." e defina quando a tarefa deve ser executada (diariamente, semanalmente, etc.).
   - **Ações:**
     - Clique em "Novo...", selecione "Iniciar um programa" e navegue até o executável `main.exe` na pasta `dist`.
   - **Condições e Configurações:**
     - Ajuste conforme necessário (por exemplo, iniciar a tarefa apenas se o computador estiver ocioso).

4. **Salvar a Tarefa:**
   - Clique em **"OK"** para salvar a tarefa.

Agora, o Agendador de Tarefas executará automaticamente o Backup Manager conforme a programação definida.

## 🛠️ **Personalização e Extensões**

- **Alterar o Intervalo de Dias para Manter Backups:**
  - Edite o arquivo `backup_config.yaml` no diretório de backup e ajuste o valor de `dias_para_manter` conforme necessário.

- **Adicionar Mais Pastas para Backup:**
  - Execute a aplicação, exclua o arquivo `backup_config.yaml`, e configure novamente para adicionar novas pastas.

## 📝 **Contribuição**

Contribuições são bem-vindas! Se você deseja melhorar este projeto, siga os passos abaixo:

1. **Fork o Repositório**
2. **Crie uma Branch para sua Feature:**

   ```bash
   git checkout -b feature/nova-feature
   ```

3. **Commit suas Alterações:**

   ```bash
   git commit -m "Adiciona nova feature"
   ```

4. **Push para a Branch:**

   ```bash
   git push origin feature/nova-feature
   ```

5. **Abra um Pull Request**

## 📄 **Licença**

Este projeto está licenciado sob a licença [MIT](LICENSE).

## 🤝 **Contato**

Se tiver dúvidas, sugestões ou feedback, sinta-se à vontade para abrir uma issue ou entrar em contato através do [hqr90](https://github.com/hqr90/backups).
