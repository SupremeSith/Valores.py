import tkinter as tk
import pyautogui
import os

# Função para minimizar a janela atual
def minimizar_janela():
    pyautogui.hotkey('win', 'down')

# Função para abrir o aplicativo correspondente
def abrir_aplicativo(aplicativo):
    if aplicativo == 'Chrome':
        os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
    elif aplicativo == 'VS Code':
        os.startfile('C:\Program Files\Microsoft VS Code\Code.exe')
    elif aplicativo == 'Calculadora':
        os.startfile('C:\Windows\System32\calc.exe')
    elif aplicativo == 'Bloco de Notas':
        os.startfile('C:\Windows\System32\notepad.exe')
    elif aplicativo == 'Discord':
        os.startfile('C:\Program Files\Discord\Discord.exe')
    elif aplicativo == 'Explorador de Arquivos':
        os.startfile('C:\Windows\explorer.exe')

# Configuração da janela principal
root = tk.Tk()
root.title('Launcher')
root.geometry('300x400')

# Criar botões para os aplicativos
apps = ['Chrome', 'VS Code', 'Calculadora', 'Bloco de Notas', 'Discord', 'Explorador de Arquivos']
for i, app in enumerate(apps):
    # Carregar o ícone correspondente
    icon_path = f'icons/{app.lower()}.png'  # Certifique-se de ter os ícones correspondentes na pasta 'icons'
    icon = tk.PhotoImage(file=icon_path)
    
    # Criar botão com o ícone e o nome do aplicativo
    button = tk.Button(root, image=icon, text=app, compound=tk.TOP, command=lambda a=app: abrir_aplicativo(a))
    button.pack(pady=10)
    
    # Configurar função de minimizar janela ao clicar no botão
    button.configure(command=minimizar_janela)
    
    # Armazenar a referência para o ícone para evitar garbage collection
    button.image = icon

root.mainloop()
