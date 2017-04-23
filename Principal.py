import pygame

def main():
    pygame.init()
    pantalla = pygame.display.set_mode([600,500])
    pygame.display.set_caption("SEB'S")
    salir = False
    reloj = pygame.time.Clock()
    (x, y) = (100, 100)

    fondo = pygame.image.load ("Imagenes/Pasto.jpg")
    personaje = pygame.image.load("Imagenes/Persona_Frente.png")
    personaje1 = pygame.sprite.Sprite()
    personaje1.image = personaje
    personaje1.rect = personaje.get_rect()
    personaje1.rect.top = 50
    personaje1.rect.left = 50
    vx = 0
    vy = 0
    r1 = pygame.Rect (150,15,15,200)

    while salir != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    vx -= 5
                if event.key == pygame.K_RIGHT:
                    vx += 5
                if event.key == pygame.K_DOWN:
                    vy += 5
                if event.key == pygame.K_UP:
                    vy -= 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    vx = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    vy = 0

        oldx = personaje1.rect.left
        personaje1.rect.move_ip(vx, vy)
        if personaje1.rect.colliderect (r1):
            personaje1.rect.left = oldx
        reloj.tick (30)
        pantalla.blit (fondo, (0, 0))
        pantalla.blit (personaje1.image, personaje1.rect)
        pygame.draw.rect (pantalla, (0,0,0), r1)
        pygame.display.update ()
    pygame.quit ()

main ()

