import pygame

class BoardVisualizer:
    def __init__(self, rows=8, size=600):
        self.rows = rows
        self.size = size
        self.cell = size // rows

        pygame.init()
        self.screen = pygame.display.set_mode((size, size))
        pygame.display.set_caption("Breakthrough")

        self.bg = (139, 69, 19)
        self.grid = (80, 40, 10)

    def draw(self, board):
        self.screen.fill(self.bg)

        for i in range(self.rows):
            for j in range(self.rows):
                rect = pygame.Rect(
                    j * self.cell,
                    i * self.cell,
                    self.cell,
                    self.cell
                )

                color = self.bg

                if board[i][j] == "o":
                    color = (200, 255, 200)

                pygame.draw.rect(self.screen, color, rect)
                pygame.draw.rect(self.screen, self.grid, rect, 1)

                piece = board[i][j]

                if piece == "W":
                    pygame.draw.circle(
                        self.screen,
                        (255, 255, 255),
                        rect.center,
                        self.cell // 3
                    )

                elif piece == "B":
                    pygame.draw.circle(
                        self.screen,
                        (30, 30, 30),
                        rect.center,
                        self.cell // 3
                    )

        pygame.display.flip()   

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True