import pyautogui
import keyboard
import math
import time
import os

# Отключаем искусственные задержки
pyautogui.PAUSE = 0

is_spinning = False


def start_spinning():
    global is_spinning
    if not is_spinning:
        print("🌀 Поехали! Крутим круги...")
        is_spinning = True


def stop_spinning():
    global is_spinning
    if is_spinning:
        print("⏸ Стоп.")
        is_spinning = False


def emergency_exit():
    print("\n🚨 Аварийная остановка! Скрипт выключен.")
    os._exit(0)


# Регистрируем комбинации
keyboard.add_hotkey('alt+v', start_spinning)
keyboard.add_hotkey('tab+o', stop_spinning)
keyboard.add_hotkey('esc', emergency_exit)

print("ИНСТРУКЦИЯ:")
print("1. Alt + V — Запустить вращение")
print("2. Tab + O — Поставить на паузу")
print("3. Esc — ПОЛНЫЙ ВЫХОД")

# Настройки круга
width, height = pyautogui.size()
cx, cy = width // 2, height // 2  # Центр экрана
radius = height // 3  # Размер круга зависит от экрана
angle = 0

while True:
    if is_spinning:
        # Плавный расчет координат
        x = cx + radius * math.cos(angle)
        y = cy + radius * math.sin(angle)

        pyautogui.moveTo(x, y)

        angle += 0.05  # Чем меньше число, тем медленнее и плавнее круг
    else:
        time.sleep(0.1)
