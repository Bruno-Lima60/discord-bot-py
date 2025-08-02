# discord-bot-py

Este é um bot multifuncional para Discord desenvolvido em Python, focado em ajudar com a moderação e gerenciamento de membros.

## Funcionalidades

O bot inclui os seguintes comandos e funcionalidades principais:

*   **`.addcargo <@membro> <nome-do-cargo>`**: Atribui um cargo a um membro do servidor.
*   **`.avisar <@usuário> <motivo>`**: Adiciona um aviso a um usuário. Os avisos são persistentes e armazenados em um arquivo JSON.
*   **`.ban <@membro> [razão]`**: Bane um membro do servidor.
*   **`.help`**: Retorna uma lista de todos os comandos disponíveis.
*   **`.kick <@membro> [razão]`**: Expulsa um membro do servidor.
*   **`.listavisos <@membro>`**: Exibe todos os avisos registrados para um usuário específico em um formato de embed.
*   **`.ping`**: Retorna a latência do bot, útil para verificar sua disponibilidade.
*   **`.removeraviso <@membro> <numero-do-aviso>`**: Remove um aviso específico de um usuário com base no índice.
*   **`.removercargo <@membro> <nome-do-cargo>`**: Remove um cargo de um membro específico.

## Pré-requisitos

*   Python 3.8+ instalado.
*   Uma conta de bot no [Discord Developer Portal](https://discord.com/developers/applications) e o token do bot.

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/Bruno-Lima60/discord-bot-py.git
    cd discord-bot-py
    ```

2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure o arquivo `.env`:**
    Crie um arquivo chamado `.env` na raiz do projeto e adicione o token do seu bot:
    ```
    DISCORD_TOKEN=SEU_TOKEN_DO_BOT_AQUI
    ```

5.  **Habilite as Intenções (Intents) no Discord Developer Portal:**
    No portal de desenvolvedores, vá para a página do seu bot, clique em "Bot" no menu lateral e ative as intenções (`Privileged Gateway Intents`) necessárias:
    *   `MESSAGE CONTENT INTENT`
    *   `MEMBERS INTENT`

6.  **Execute o bot:**
    ```bash
    python main.py
    ```

