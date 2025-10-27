
import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        """Initializing the game, and creating game assets and behaviour."""
        pygame.init()
        self.settings = Settings()

        #Setting the display ratio
        self.screen=pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width=self.screen.get_rect().width
        self.settings.screen_height=self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets=pygame.sprite.Group()

        #Setting background color.
        self.bg_color=self.settings.bg_color
    
    def run_game(self):
        """start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            
            #watch for keyboard and mouse events.
    def _check_events(self):
        """Respomdm to key press and mouse event"""
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            #move the ship
            elif event.type==pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type==pygame.KEYUP:
                self._check_keydup_events(event)

    #Key down event:
    def _check_keydown_events(self,event):
        """responds to keypresses."""
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key==pygame.K_q:
            sys.exit()
        elif event.key==pygame.K_SPACE:
            self.fire_bullet()

    #Key up event:
    def _check_keydup_events(self,event):
        """responds to keyrelease."""
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left = False

    
    def fire_bullet(self):
        """Creating a new bullet and add it to the bullet group."""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Updates the psotions of bullets amd get rid of old bullets."""
        #upddate bullet positions.
        self.bullets.update()
        #getting rid of of old bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom<=0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        #Redraw the screen during each pass through the loop
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Make the most recently drawn display 
        pygame.display.flip()

if __name__ =='__main__':
    #make a game instance, and run the game.
    ai=AlienInvasion()
    ai.run_game()