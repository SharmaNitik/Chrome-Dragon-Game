def collision(playerX, playerY, grassX, grassY):
    dist = ( (playerX-grassX)**2 + (playerY-grassY)**2 )**(0.5)
    if dist < 27:
        return True
    else:
        return False
