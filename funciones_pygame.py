import pygame

def dibujar_boton(texto, x, y, alto, ancho, color_principal, pantalla, color_texto=(255, 255, 255)):
    '''
    ¿Qué hace?: Dibuja un botón en la pantalla.
    ¿Qué recibe?: El texto del botón, las coordenadas x e y, el alto y ancho del botón, la pantalla y el color del texto.
    ¿Qué retorna?: El rectángulo del botón.
    '''
    fuente = pygame.font.Font(None, 32)
    pygame.draw.rect(pantalla, color_principal, (x, y, ancho, alto))
    texto_renderizado = fuente.render(texto, True, color_texto)
    texto_rect = texto_renderizado.get_rect(center=(x + ancho // 2, y + alto // 2))
    pantalla.blit(texto_renderizado, texto_rect)
    return pygame.Rect(x, y, ancho, alto)
