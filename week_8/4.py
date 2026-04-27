import pygame

pygame.init() # Инициализация всех модулей Pygame
screen = pygame.display.set_mode((400, 300)) # Создаем окно
done = False

while not done:
    for event in pygame.event.get(): # Проверяем, что сделал пользователь
        if event.type == pygame.QUIT:
            done = True
            
    screen.fill((0, 0, 255)) # Закрашиваем экран белым
    pygame.display.flip() # Обновляем экран
    