import pygame

from .config import *
pygame.font.init()

font = pygame.font.SysFont("Arial", 20)


class Button:
    """Create a button, then blit the surface in the while loop"""

    def __init__(self, text,  pos, font, bg="black"):
        self.x, self.y = pos
        self.text = text
        self.font = pygame.font.SysFont("Arial", font)

        self.text = self.font.render(text, 1, pygame.Color("White"))

        self.size = self.text.get_size()
        self.bg = bg
        self.change_text(text, bg)

    def change_text(self, text, bg="black"):
        """Change the text whe you click"""
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


class ButtonContinue(Button):
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


class ButtonStart(Button):
    def __init__(self, text, pos, font, bg):
        super().__init__(text, pos, font, bg)
        self.focused = False

    def click(self, event, root):
        x, y = pygame.mouse.get_pos()
        if self.rect.collidepoint(x, y) and not self.focused:
            button_start_focus.show(root)
            self.focused = True
        elif not self.rect.collidepoint(x, y) and self.focused:
            button_start_unfocused.show(root)
            self.focused = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    return True


class ButtonSettings(Button):
    def __init__(self, text, pos, font, bg):
        super().__init__(text, pos, font, bg)
        self.focused = False

    def click(self, event, root):
        x, y = pygame.mouse.get_pos()
        if self.rect.collidepoint(x, y) and not self.focused:
            button_settings_focus.show(root)
            self.focused = True
        elif not self.rect.collidepoint(x, y) and self.focused:
            button_settings_unfocused.show(root)
            self.focused = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    return True



pos_continue = W//5, H-H//7-H//10
pos_start = W//4 + W//25, H-H//2-H//10
pos_settings = W//4 + W//50, H-H//10 - 40


button_continue_unfocused = ButtonContinue("   Continue    ", pos_continue, font=H // 8, bg="navy")
button_continue_focus = ButtonContinue("   Continue    ", pos_continue, font=H // 8, bg="orange")

button_start_unfocused = ButtonStart("   Start    ", pos_start, font=H // 8, bg="navy")
button_start_focus = ButtonStart("   Start    ", pos_start, font=H // 8, bg="orange")

button_settings_unfocused = ButtonSettings("   Settings    ", pos_settings, font=H // 10, bg="green")
button_settings_focus = ButtonSettings("   Settings    ", pos_settings, font=H // 10, bg="orange")


class ButtonSetSize(Button):
    def __init__(self, text, pos, font, bg,  is_locked=False, focused = False):
        super().__init__(text, pos, font, bg)
        self.text = text
        self.pos = pos
        self.font = font
        self.is_locked = is_locked
        self.focused = focused
        self.bg=bg

    def focusing(self):
        return ButtonSetSize(self.text, self.pos, self.font, "orange", False, True)

    def unfocusing(self):
        return ButtonSetSize(self.text, self.pos, self.font, "green", False)

    def have_focus(self):
        x, y = pygame.mouse.get_pos()
        if self.is_locked:
            return self.lock()
        elif self.rect.collidepoint(x, y) and not self.focused:
            return self.focusing()
        elif not self.rect.collidepoint(x, y):
            return self.unfocusing()
        return self

    def lock(self):
        return ButtonSetSize(self.text, self.pos, self.font, COLOR_CHOsZEN, True)

    def unlock(self):
        return ButtonSetSize(self.text, self.pos, self.font, "green", False)


class ButtonSetVolume(Button):
    def __init__(self, text, pos, font, bg,  is_locked=False, focused = False):
        super().__init__(text, pos, font, bg)
        self.text = text
        self.pos = pos
        self.font = font
        self.is_locked = is_locked
        self.focused = focused
        self.bg=bg

    def focusing(self):
        return ButtonSetSize(self.text, self.pos, self.font, "orange", False, True)

    def unfocusing(self):
        return ButtonSetSize(self.text, self.pos, self.font, "green", False)

    def have_focus(self):
        x, y = pygame.mouse.get_pos()
        if self.is_locked:
            return self.lock()
        elif self.rect.collidepoint(x, y) and not self.focused:
            return self.focusing()
        elif not self.rect.collidepoint(x, y):
            return self.unfocusing()
        return self

    def lock(self):
        return ButtonSetVolume(self.text, self.pos, self.font, COLOR_CHOsZEN, True)

    def unlock(self):
        return ButtonSetVolume(self.text, self.pos, self.font, "green", False)
