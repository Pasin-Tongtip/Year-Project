from config import Config
import pygame
import random
import operator


class Snake:
    def __init__(self):
        self.body = [[Config.get('WIDTH') // 2, Config.get('HEIGHT') // 2]]
        self.dx = 0
        self.dy = 0
        self.grow = False

    def move(self):
        head = self.body[-1][:]
        head[0] += self.dx
        head[1] += self.dy
        self.body.append(head)
        if not self.grow:
            self.body.pop(0)
        else:
            self.grow = False

    def change_direction(self, dx, dy):
        if (dx, dy) != (-self.dx, -self.dy):
            self.dx, self.dy = dx, dy

    def collide_with_self(self):
        return self.body[-1] in self.body[:-1]

    def grow_snake(self):
        self.grow = True

    def get_head_position(self):
        return self.body[-1]

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen,
                             Config.get('BLACK'),
                             [segment[0], segment[1], Config.get('BLOCK_SIZE'), Config.get('BLOCK_SIZE')])


class Food:
    def __init__(self, position, value):
        self.position = position
        self.value = value

    def random_position(self):
        x = random.randrange(0, Config.get('WIDTH') - Config.get('BLOCK_SIZE'), Config.get('BLOCK_SIZE'))
        y = random.randrange(0, Config.get('HEIGHT') - Config.get('BLOCK_SIZE'), Config.get('BLOCK_SIZE'))
        return [x, y]

    def draw(self, screen, font):
        pygame.draw.rect(screen,
                         Config.get('GREEN'),
                         [self.position[0], self.position[1], Config.get('BLOCK_SIZE'), Config.get('BLOCK_SIZE')])
        label = font.render(str(self.value), True, Config.get('BLACK'))
        screen.blit(label, (self.position[0] + 2, self.position[1] + 2))


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Config.get('WIDTH'), Config.get('HEIGHT')))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("bahnschrift", 30)
        self.snake = Snake()
        self.generate_equation()
        self.running = True
        self.game_over = False
        self.score = 0
        self.generate_equation()
        self.max_health = 100
        self.health = self.max_health
        self.start_time = pygame.time.get_ticks()
        self.elapsed_time = 0
        self.flash_duration = 50
        self.flash_start_time = None

    def show_message(self, message, color):
        self.screen.fill(Config.get('BLUE'))
        msg = self.font.render(message, True, color)
        self.screen.blit(msg, [Config.get('WIDTH') // 6, Config.get('HEIGHT') // 3])
        pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.snake.change_direction(-Config.get('BLOCK_SIZE'), 0)
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction(Config.get('BLOCK_SIZE'), 0)
                elif event.key == pygame.K_UP:
                    self.snake.change_direction(0, -Config.get('BLOCK_SIZE'))
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction(0, Config.get('BLOCK_SIZE'))

    def check_collisions(self):
        head_x, head_y = self.snake.get_head_position()
        if (head_x < 0
                or head_x >= Config.get('WIDTH')
                or head_y < 0
                or head_y >= Config.get('HEIGHT')
                or self.snake.collide_with_self()):
            self.game_over = True
            self.show_message("Game Over! Press R to Restart", Config.get('BLACK'))
            return

        head_pos = self.snake.get_head_position()
        for food in self.food_items:
            if head_pos == food.position:
                if food.value == self.correct_answer:
                    self.snake.grow_snake()
                    self.score += 1
                else:
                    self.health -= 25
                    self.flash_start_time = pygame.time.get_ticks()
                    if self.health <= 0:
                        self.game_over = True
                        self.show_message("Out of health! Press R to Restart", Config.get('BLACK'))
                self.generate_equation()
                break

    def show_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, Config.get('WHITE'))
        self.screen.blit(score_text, [10, 10])

    def reset(self):
        self.snake = Snake()
        self.generate_equation()
        self.score = 0
        self.game_over = False
        self.generate_equation()

    def generate_equation(self):
        ops = {'+': operator.add,
               '-': operator.sub,
               '*': operator.mul}
        op_symbol = random.choice(list(ops.keys()))
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        answer = ops[op_symbol](a, b)
        self.current_equation = f"{a} {op_symbol} {b} = ?"
        self.correct_answer = answer

        answers = [answer]
        while len(answers) < Config.get('NUM_FOOD'):
            fake = random.randint(answer - 10, answer + 10)
            if fake != answer and fake not in answers:
                answers.append(fake)

        random.shuffle(answers)
        self.food_items = []
        for val in answers:
            pos = [random.randrange(0, Config.get('WIDTH') - Config.get('BLOCK_SIZE'), Config.get('BLOCK_SIZE')),
                   random.randrange(40, Config.get('HEIGHT') - Config.get('BLOCK_SIZE'), Config.get('BLOCK_SIZE'))]
            self.food_items.append(Food(pos, val))

    def show_equation(self):
        eq_text = self.font.render(self.current_equation, True, Config.get('WHITE'))
        self.screen.blit(eq_text, [Config.get('WIDTH') // 2 - 50, 10])

    def draw_health_bar(self):
        bar_x, bar_y = 10, 40
        bar_width, bar_height = 100, 10
        fill_width = int((self.health / self.max_health) * bar_width)

        pygame.draw.rect(self.screen, Config.get('WHITE'), [bar_x, bar_y, bar_width, bar_height], 2)
        pygame.draw.rect(self.screen, Config.get('RED'), [bar_x, bar_y, fill_width, bar_height])

    def draw_elapsed_time(self):
        timer_text = self.font.render(f"Time: {self.elapsed_time}s", True, Config.get('WHITE'))
        self.screen.blit(timer_text, (Config.get('WIDTH') - 120, 10))

    def run(self):
        while self.running:
            self.handle_events()
            if not self.game_over:
                self.snake.move()
                self.elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000
                self.check_collisions()
                self.screen.fill(Config.get('BLUE'))
                self.snake.draw(self.screen)

                for food in self.food_items:
                    food.draw(self.screen, self.font)

                self.show_score()
                self.show_equation()
                self.draw_health_bar()
                self.draw_elapsed_time()

                if self.flash_start_time:
                    elapsed = pygame.time.get_ticks() - self.flash_start_time
                    if elapsed < self.flash_duration:
                        flash_surface = pygame.Surface((Config.get('WIDTH'), Config.get('HEIGHT')))
                        flash_surface.set_alpha(200)
                        flash_surface.fill(Config.get('RED'))
                        self.screen.blit(flash_surface, (0, 0))
                    else:
                        self.flash_start_time = None

                pygame.display.update()
                self.clock.tick(Config.get('SPEED'))
            else:
                self.show_message("Game Over! Press R to Restart", Config.get('BLACK'))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            self.reset()
        pygame.quit()


if __name__ == "__main__":
    Game().run()
