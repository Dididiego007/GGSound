import socket
import pyautogui
from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw
import threading
import sys


# Função para criar o ícone da bandeja
def create_icon():
    # Cria uma imagem de ícone simples (você pode substituir por um ícone personalizado)
    icon_image = Image.new('RGB', (64, 64), color=(255, 255, 255))
    draw = ImageDraw.Draw(icon_image)
    draw.rectangle([16, 16, 48, 48], fill="blue")

    # Função de ação para fechar o aplicativo
    def on_quit(icon, item):
        icon.stop()
        sys.exit(0)

    # Cria o menu da bandeja com a opção de sair
    menu = Menu(MenuItem('Sair', on_quit))

    # Cria o ícone da bandeja
    icon = Icon("test", icon_image, menu=menu)
    icon.run()


# Função que contém a lógica do servidor
def start_server():
    # Configurações do servidor
    HOST = '0.0.0.0'  # Escuta em todas as interfaces de rede
    PORT = 6986  # Porta para a conexão TCP

    # Cria o socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)  # Aguarda por uma conexão (pode aceitar apenas uma conexão por vez)

    # Obtém o IP da máquina para exibir para o cliente
    ip_address = socket.gethostbyname(socket.gethostname())  # IP local
    print(f'Servidor TCP ouvindo na porta {PORT} no IP {ip_address}...')



    while True:
        # Aceita uma conexão do cliente
        client_socket, client_address = server_socket.accept()
        print(f'Conexão recebida de {client_address}.')
        try:
            while True:
                # Recebe uma mensagem do cliente
                data = client_socket.recv(1024)
                if not data:
                    break  # Se não houver dados, sai do loop
                message = data.decode('utf-8').strip()

                print(f'Mensagem recebida de {client_address}: {message}')

                # Verifica se a mensagem é um número de 0 a 7
                if message in '01234567':
                    # Executa o atalho correspondente (Ctrl+0 até Ctrl+7)
                    pyautogui.hotkey('ctrl', message)
                    print(f'Executando: Ctrl+{message}')
                else:
                    print(f'Dado inválido recebido: {message}')
        except Exception as e:
            print(f'Ocorreu um erro com o cliente {client_address}: {e}')
        finally:
            # Fecha a conexão com o cliente após o término
            client_socket.close()


# Função principal
def main():
    # Inicia o ícone na bandeja do sistema
    icon_thread = threading.Thread(target=create_icon)
    icon_thread.daemon = True
    icon_thread.start()

    # Inicia o servidor em uma thread separada
    start_server()


if __name__ == "__main__":
    main()