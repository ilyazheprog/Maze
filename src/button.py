import pygame

from .config import *
pygame.font.init()

font = pygame.font.SysFont("Arial", 20)


class Button:
    """Create a button, then blit the surface in the while loop"""

    def __init__(self, text,  pos, font, bg="black"):
        self.x, self.y = pos
        self.text = text
        self.bg = bg
        self.font = pygame.font.SysFont("Arial", font)
        self.change_text(text, bg)

    def change_text(self, text, bg="black"):
        """Change the text whe you click"""
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self, root):
        root.screen.blit(self.surface, (self.x, self.y))

    def click(self, event, root):
        x, y = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    return True


class Button_continue(Button):
    def __init__(self, text, pos, font, bg):
        super().__init__(text, pos, font, bg)
        self.focused = False

    def click(self, event, root):
        x, y = pygame.mouse.get_pos()
        if self.rect.collidepoint(x, y) and not self.focused:
            button_continue_focus.show(root)
            self.focused = True
        elif not self.rect.collidepoint(x, y) and self.focused:
            button_continue_unfocused.show(root)
            self.focused = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    return True


pos_continue = W//5, H-H//7-H//10
button_continue_unfocused = Button_continue("   Continue    ", pos_continue, font=H//8, bg="navy")
button_continue_focus = Button_continue("   Continue    ", pos_continue, font=H//8, bg="orange")

