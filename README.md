
# SoundPadPobre - Controle de Áudio Remoto via App

**SoundPadPobre** é um projeto que permite controlar a reprodução de áudio no seu PC a partir de um aplicativo no celular. Ele utiliza sockets para se conectar entre o programa Python rodando no PC e o app no celular. O app no celular possui botões que são convertidos em teclas de atalho no PC, permitindo controlar a reprodução de sons no **SoundPad**.

## Funcionalidades

- **Controle Remoto de Áudio:** Controle a reprodução de áudio do PC a partir do seu celular.
- **Mapeamento de Botões:** Botões no app do celular são mapeados para atalhos de teclado (exemplo: Botão 1 no celular = `Ctrl+1` no PC).
- **Integração com o SoundPad:** O SoundPad precisa estar instalado no PC para que o app possa controlar os áudios adicionados.
- **Conexão via Socket:** Comunicação entre o app e o PC através de sockets, usando o IP da máquina.

## Tecnologias Utilizadas

- **Python** (versão X.X)
- **Sockets**: Comunicação entre o app e o PC via rede.
- **SoundPad**: Ferramenta instalada no PC para reprodução de áudio.
- **App Mobile**: Interface com botões de controle que enviam comandos para o PC.
- **Bibliotecas**: `socket`, `pygame` (ou outras dependências do projeto)

## Como Funciona

### Arquitetura:

1. **No PC:**
   - Um programa Python é executado no PC.
   - O programa se conecta ao aplicativo móvel via socket, escutando em uma porta específica.
   - O programa Python no PC controla a reprodução de áudio através do **SoundPad** usando atalhos de teclado.

2. **No Celular:**
   - O app envia comandos via socket para o programa Python no PC, mapeando botões para atalhos de teclado.
   - Exemplo: O botão 1 no app envia o comando `Ctrl+1` para o programa Python, que é interpretado como um atalho para o **SoundPad**.

## Instalação

### 1. **No PC**

1. Clone o repositório para o seu PC:

   ```bash
   git clone https://github.com/Dididiego007/GGSound.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd GGSound
   ```

3. Crie um ambiente virtual e ative-o (opcional, mas recomendado):

   ```bash
   python -m venv .venv
   .\.venv\Scriptsctivate  # No Windows
   source .venv/bin/activate  # No Linux/macOS
   ```

4. Instale as dependências do projeto:

   ```bash
   pip install -r requirements.txt
   ```

   Caso o arquivo `requirements.txt` ainda não tenha sido criado, você pode instalar manualmente as bibliotecas necessárias, como `pygame` para controle de áudio e `socket` para comunicação.

5. Instale o **SoundPad** no PC. Você pode baixar o SoundPad diretamente no site oficial ou seguir as instruções de instalação, caso tenha algum repositório específico para isso.

6. Execute o programa Python no seu PC:

   ```bash
   python main.py
   ```

   Isso iniciará o servidor que ficará aguardando conexões do app móvel.

### 2. **No Celular**

1. Baixe o aplicativo móvel desenvolvido para este projeto. O aplicativo está disponível na Google Play Store ou na App Store, conforme a plataforma em que você deseja executar.
2. Abra o aplicativo e insira o **IP** do seu PC para estabelecer a conexão via rede local (Wi-Fi).
3. Após a conexão ser estabelecida, você poderá controlar a reprodução de áudio no **SoundPad** usando os botões do app, que são mapeados para atalhos de teclado.

## Uso

### No PC

1. Ao rodar o programa Python no PC, ele ficará ouvindo as conexões do app. Ele é responsável por interpretar os comandos recebidos via socket e executá-los como comandos de teclado, que vão controlar a reprodução do **SoundPad**.
2. Certifique-se de que o **SoundPad** esteja aberto no PC e com áudios carregados para reproduzir.

### No App

1. Após a conexão ser estabelecida entre o app e o programa Python no PC, pressione os botões no app para enviar comandos de atalho para o PC.
   - Exemplo: Pressionar o **Botão 1** no app enviará `Ctrl+1` para o PC, e o programa Python irá controlar a reprodução de áudio conforme a tecla de atalho configurada.

## Contribuindo

Se você deseja contribuir para o projeto, fique à vontade para fazer um fork, criar uma nova branch e enviar um pull request. Para isso, siga estas etapas:

1. Faça um **fork** do repositório.
2. Crie uma branch para as alterações que você deseja fazer.
3. Faça suas alterações e faça o commit.
4. Envie suas alterações para o repositório remoto.
5. Abra um **pull request** para análise.

## Licença

Este projeto está licenciado sob a **MIT License** - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
