from .config import *

pygame.font.init()

font = pygame.font.SysFont("Arial", 20)


class Button:
    def __init__(self, text: str, pos: tuple[int, ...], font_size: int, bg_out_of_focus: str = "black",
                 bg_focus: str = "orange", is_focus: bool = False, is_locked: bool = False):
        self.is_focus = is_focus
        self.bg_out_of_focus = bg_out_of_focus
        self.bg_focus = bg_focus
        self.x, self.y = pos
        self.text = text
        self.font = pygame.font.SysFont("Arial", font_size)

        self.text = self.font.render(text, True, pygame.Color("White"))

        self.size = self.text.get_size()
        self.bg = bg_out_of_focus
        self.is_locked = is_locked
        self.change_text(text, bg_out_of_focus)

    def focusing(self):
        self.change_text(self.text, self.bg_focus)
        self.is_focus = True

    def out_of_focusing(self):
        self.change_text(self.text, self.bg_out_of_focus)
        self.is_focus = False

    def lock(self):
        self.is_locked = True
        self.change_text(self.text, COLOR_CHOSEN_AND_BLOCKED)

    def unlock(self):
        self.is_locked = False
        self.change_text(self.text, self.bg_out_of_focus)

    def manage_focus(self):
        x, y = pygame.mouse.get_pos()
        if self.is_locked:
            return self.lock()
        elif self.rect.collidepoint(x, y) and not self.is_focus:
            return self.focusing()
        elif not self.rect.collidepoint(x, y):
            return self.out_of_focusing()
        return self

    def change_text(self, text, bg="black"):
        """Change the text whe you click"""
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self, root):
        root.screen.blit(self.surface, (self.x, self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    return True


pos_continue = W // 3 - W // 20, H - H // 5 - H // 10
pos_start = W // 4 + W // 25, H - H // 2 - H // 10
pos_settings = W // 4 + W // 50, H - H // 10 - 40
pos_menu = W // 3 + 40, H - H // 15 - 40

button_menu = Button("To menu", pos_menu, H // 15, bg_out_of_focus="violet")

button_continue = Button("   Continue    ", pos_continue, font_size=H // 11, bg_out_of_focus="navy")

button_start = Button("   Start    ", pos_start, font_size=H // 8, bg_out_of_focus="navy")

button_settings = Button("   Settings    ", pos_settings, font_size=H // 10, bg_out_of_focus="green")

pos_small = 10, H // 24 + H // 11 + H // 18

button_small = Button("   Small    ", pos_small, font_size=H // 15, bg_out_of_focus="green")
pos_middle = 20 + button_small.size[0], H // 24 + H // 11 + H // 18
button_middle = Button("   Middle    ", pos_middle, font_size=H // 15, bg_out_of_focus="green")

pos_bigger = 30 + button_small.size[0] + button_middle.size[0], H // 24 + H // 11 + H // 18
button_bigger = Button("   Bigger    ", pos_bigger, font_size=H // 15, bg_out_of_focus="green")

pos_minus = 10, H // 4 + H // 11 + H // 18
button_minus = Button("   -   ", pos_minus, font_size=H // 15, bg_out_of_focus="green")

pos_plus = 5 + 3 * button_minus.size[0], H // 4 + H // 11 + H // 18

button_plus = Button("   +   ", pos_plus, font_size=H // 15, bg_out_of_focus="green")

pos_test = W // 15, pos_minus[1] + H // 10
button_test = Button("      Test sound     ", pos_test, font_size=H // 20, bg_out_of_focus="magenta")
