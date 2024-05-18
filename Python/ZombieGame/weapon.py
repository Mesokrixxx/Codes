import drawing

class Weapon():
    def __init__(self, bulletSpeed, bulletDamage, shootDelay, recoil, reloadTime, width, height):
        self.bulletSpeed = bulletSpeed
        self.bulletDamage = bulletDamage
        self.shootDelay = shootDelay
        self.recoil = recoil
        self.reloadTime = reloadTime
        self.width = width
        self.height = height
                
        self.timer = 0
    
    def shoot(self):
        pass
    
    def draw(self, surface, x, y, playerSize, angle):
        drawing.glockDrawing(surface, (x - self.width / 2) , (y + playerSize / 1.4), self.width, self.height, angle)