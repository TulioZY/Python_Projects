import time
import pyautogui
import Localization
import cv2
from win32con import *


def reiniciar_hunt():
    # Obtém as dimensões da tela
    screen_width, screen_height = pyautogui.size()
    
    # Define as coordenadas do objeto desejado em uma tela de referência (por exemplo, 1920x1080)
    reference_width = 1920
    reference_height = 1080
    reference_x = 1633
    reference_y = 928
    reference_x2 = 1561
    reference_y2 = 921

    # Calcula as proporções relativas com base na resolução atual da tela
    x_ratio = screen_width / reference_width
    y_ratio = screen_height / reference_height

    # Calcula as coordenadas adaptativas para a resolução atual da tela
    adapted_x = int(reference_x * x_ratio)
    adapted_y = int(reference_y * y_ratio)
    adapted_x2 = int(reference_x2 * x_ratio)
    adapted_y2 = int(reference_y2 * y_ratio)

    # Calcula as coordenadas proporcionais com base nas dimensões da tela
    coordenadas_reiniciar = (adapted_x, adapted_y)  
    coordenadas_reiniciar2 = (adapted_x2, adapted_y2)

    # Verifica se a imagem alvo está na tela
    imagem_alvo = 'confirm.png' 
    posicao_imagem = pyautogui.locateOnScreen(imagem_alvo, grayscale=True, confidence=0.65)

    if posicao_imagem is not None:
        # Clique no botão de reiniciar
        time.sleep(6)
        pyautogui.doubleClick(coordenadas_reiniciar)
        time.sleep(2)  # Aguarda um segundo para dar tempo de reiniciar a ação
        pyautogui.click(coordenadas_reiniciar2)
        time.sleep(2)
        pyautogui.click(coordenadas_reiniciar2)
        
def Screencheck():
    check = 0
    W_Screen = Localization.main()[2] 
    while W_Screen > 1270:
        W_Screen = Localization.main()[2] 
        if check < 1:
            print("Screen check notification: Your screen size is too big")
            check +=1 
    while W_Screen < 1160:
        W_Screen  =Localization.main()[2] 
        if check < 1:
            print("Screen check notification: Your screen size is too small")
            check +=1
    print("Screen check notification: You are good to go now!")
    
def Screencheckrun():
    check = 0
    W_Screen = Localization.main()[2]
    if W_Screen < 1160 or W_Screen > 1270: 
        while W_Screen > 1270:
            W_Screen = Localization.main()[2] 
            if check < 1:
                print("Screen check notification: Your screen size is too big")
                check +=1 

        while W_Screen < 1160:
            W_Screen  =Localization.main()[2] 
            if check < 1:
                print("Screen check notification: Your screen size is too small")
                check +=1
        print("Screen check notification: You are good to go now!")
        for i in range(3):
            print("System will resume in: "+ str(3-i) + "   [Please do not change LDPlayer resolution while program is still running]")
            time.sleep(1)    
    else:
        pass
    
def invSpace():
    # Verifica se a imagem alvo está na tela
    img_arrange = 'Arrange.png' 
    arrange_position = pyautogui.locateOnScreen(img_arrange, grayscale=True, confidence=0.85)

    if arrange_position is not None:
        check = 1
        return check
def noEnergy():
    # Verifica se a imagem alvo está na tela
    img_arrange = 'noEnergy.png' 
    arrange_position = pyautogui.locateOnScreen(img_arrange, grayscale=True, confidence=0.85)

    if arrange_position is not None:
        check = 1
        return check