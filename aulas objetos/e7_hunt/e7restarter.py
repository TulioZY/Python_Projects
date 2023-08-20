import time
import keyboard
import Event
import cv2


print("How to use the program.")
print("First, let your LDPlayer window opened and maximized. \nStart your run normally, the program will restart it automatically later.")
print("When your inventory is full, the program will stop, so clear your inventory first before run the program again")
print("If you run out of energy, the program will stop, so you need to buy enough energy to let it farming for enough time.")
print("HOW TO STOP THE PROGRAM: \nPress 'q' on your keyboard to stop the program by yourself.")
print("The program is starting in 10 seconds.")
time.sleep(10)
print("Program running.")
Event.Screencheck()  # Is there a screen size problem?
# Defina a tecla específica que irá interromper o loop
stop_key = 'q'
while True:
    Event.Screencheckrun()
    Event.reiniciar_hunt()
    Event.invSpace()
    if Event.invSpace == 1:
        time.sleep(8)
        break
    Event.noEnergy()
    if Event.noEnergy == 1:
        time.sleep(8)
        break
    # Verifica se a tecla de parada foi pressionada
    if keyboard.is_pressed(stop_key):
        print("Done with hunts today. Closing the program.")
        time.sleep(8)
        break
