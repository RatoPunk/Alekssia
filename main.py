import tkinter as tk
import speech_recognition as sr
import pyttsx3
import threading
import pygame
import os as sys
import random




# Inicializar pygame
pygame.init()

# Configurar a engine de voz
engine = pyttsx3.init()
engine.setProperty("rate", 150)

# Função para falar
def falar(texto):
    engine.say(texto)
    engine.runAndWait()




# função para tocar as musicas
def tocar_red():
    caminho_red = "C:/Assets/red.mp3"
    if sys.path.exists(caminho_red):
        pygame.mixer.music.load(caminho_red)
        pygame.mixer.music.play(-1)

    else:
        label_text.set("Arquivo de música não encontrado!")

def tocar_anarquia():
    caminho_anarquia = "C:/Assets/anarquia.mp3"  
    if sys.path.exists(caminho_anarquia):
        pygame.mixer.music.load(caminho_anarquia)
        pygame.mixer.music.play(-1)
    else:
        label_text.set("Arquivo de música não encontrado!")


def tocar_dongo():
    caminho_dongo = "C:/Assets/dongo.mp3"  
    if sys.path.exists(caminho_dongo):
        pygame.mixer.music.load(caminho_dongo)
        pygame.mixer.music.play(-1)
    else:
        label_text.set("Arquivo de música não encontrado!")

# Função que escuta a voz em uma thread separada
def ouvir_comando():
    def callback():
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            label_text.set("Ouvindo...")
            janela.update()
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            comando = recognizer.recognize_google(audio, language="pt-BR").lower()
            label_text.set(f"Você disse: {comando}")
            falar(f"Você disse {comando}")

            # Verificar comandos
            if "dongo" in comando:
                falar("Claro, vou tocar dongo")
                tocar_dongo()
            if "mãe anarquia" in comando:
                falar("Claro, vou tocar mother anarchy")
                tocar_anarquia()
            if "stop" in comando:
                falar("Claro, vou parar a musica atual")
                pygame.mixer.music.stop()    
            if "reiniciar" in comando:
                falar("Reiniciando o sistema")
                sys.system("shutdown /r /t 1")
            if "red" in comando:
                falar("Claro, vou tocar you aint done nothing if you aint been called a red")
                tocar_red()
            if "desligar" in comando:
                falar("ok, desligando")
                sys.system("shutdown /s /t 1")
                


        
        except sr.UnknownValueError:
            label_text.set("Ou, calma lá paizão, não tenho capacidade cognitiva para entender mais que uma palavra ainda.")
            falar("Ou, calma lá paizão, não tenho capacidade cognitiva para entender mais que uma palavra ainda")
        except sr.RequestError as e:
            label_text.set(f"Erro ao se comunicar com o serviço de reconhecimento de fala: {e}")
            falar(f"Erro ao se comunicar com o serviço de reconhecimento de fala: {e}")



            
    

    # Criar e rodar uma thread separada para evitar travamentos
    thread = threading.Thread(target=callback)
    thread.start()

# Criar a janela principal
janela = tk.Tk()
janela.title("Alekssia")
janela.geometry("400x300")

# Criar um label para mostrar o texto reconhecido
label_text = tk.StringVar()
label_text.set("Clique para falar")
label = tk.Label(janela, textvariable=label_text, font=("Arial", 12), wraplength=300)
label.pack(pady=20)

# Criar um botão para ativar a escuta
botao = tk.Button(janela, text="Falar", font=("Arial", 14), command=ouvir_comando)
botao.pack(pady=20)



# codes
codes = ["desligar", "reiniciar", "stop", "dongo", "red", "anarquia"]

# tkinter label
label = tk.Label(janela, text="codes:", font=("Arial", 14))
label.pack(pady=21) 
# tkinter label
label = tk.Label(janela, text=codes, font=("Arial", 14))
label.pack(pady=20)  


# loop tkinter
janela.mainloop()