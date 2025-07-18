import pygame
import sys
import random
import os
from cards import INFO, START, RANDOMEVENT, HEALTHMOMENT, DECISIONPOINT, FINISH

# ======= Config =========
# Initialize Pygame
pygame.init()

# Window settings
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Game of Life: Breast Health Edition")

# ======= Text Wrapping Helper =========

def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = ''

    for word in words:
        test_line = current_line + word + ' '
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line.strip())
            current_line = word + ' '
    if current_line:
        lines.append(current_line.strip())
    return lines

# ======= Board Objects =========
class Tile:
    def __init__(self, window, loc=(0, 0), title=None, description=None):
        self.window = window
        self.type = None
        self.active = False
        self.loc = loc
        self.edges = []
        self.colour = None
        self.cards = None

    def draw_edges(self, camera_offset):
        start_pos = (self.loc[0] + camera_offset[0], self.loc[1] + camera_offset[1])
        for target in self.edges:
            end_pos = (target.loc[0] + camera_offset[0], target.loc[1] + camera_offset[1])
            pygame.draw.line(self.window, (0, 0, 0), start_pos, end_pos, 3)

    def draw(self, camera_offset):
        screen_pos = (self.loc[0] + camera_offset[0], self.loc[1] + camera_offset[1])
        pygame.draw.circle(self.window, self.colour, screen_pos, 20)

    def get_card(self, card_no, card):
        self.card_no = card_no
        self.cards = card

    def create_tile_popup(self, window, decision=None):
        popup_rect = pygame.Rect(WIDTH//2 - 200, HEIGHT//2 - 150, 400, 300)
        pygame.draw.rect(window, self.colour, popup_rect)
        pygame.draw.rect(window, (0, 0, 0), popup_rect, 2)

        font = pygame.font.SysFont(None, 22)
        y_offset = 10

        title_surface = font.render(f"{self.type}", True, (0, 0, 0))
        window.blit(title_surface, (popup_rect.x + 10, popup_rect.y + y_offset))
        y_offset += 28

        if self.cards is not None:
            if decision is None:
                title = self.cards.get('title', '')
                description = self.cards.get('description', '')
                suggestion = self.cards.get('suggestion', '')
            else:
                title = self.cards.get('title', '')
                description = self.cards.get('description', '')
                suggestion_list = self.cards.get('suggestion', ['', ''])
                suggestion = suggestion_list[decision] if isinstance(suggestion_list, list) else suggestion_list

            for field_text in [title, description, suggestion]:
                lines = wrap_text(field_text, font, popup_rect.width - 20)
                for line in lines:
                    line_surface = font.render(line, True, (0, 0, 0))
                    window.blit(line_surface, (popup_rect.x + 10, popup_rect.y + y_offset))
                    y_offset += 22

    def create_decision_popup(self, window):
        popup_rect = pygame.Rect(WIDTH//2 - 175, HEIGHT//2 - 100, 350, 200)
        pygame.draw.rect(window, (230, 230, 230), popup_rect)
        pygame.draw.rect(window, (0, 0, 0), popup_rect, 2)

        font = pygame.font.SysFont(None, 24)
        title = self.cards['title'] if self.cards and 'title' in self.cards else "Choose your path:"

        lines = wrap_text(title, font, popup_rect.width - 20)
        y_offset = 15
        for line in lines:
            text_surface = font.render(line, True, (0, 0, 0))
            window.blit(text_surface, (popup_rect.x + 10, popup_rect.y + y_offset))
            y_offset += 26

        yes_button = pygame.Rect(popup_rect.x + 40, popup_rect.y + popup_rect.height - 60, 100, 40)
        no_button = pygame.Rect(popup_rect.x + popup_rect.width - 140, popup_rect.y + popup_rect.height - 60, 100, 40)

        pygame.draw.rect(window, (0, 200, 0), yes_button)
        pygame.draw.rect(window, (200, 0, 0), no_button)

        button_font = pygame.font.SysFont(None, 28)
        window.blit(button_font.render("Yes", True, (255, 255, 255)), (yes_button.x + 30, yes_button.y + 7))
        window.blit(button_font.render("No", True, (255, 255, 255)), (no_button.x + 35, no_button.y + 7))

        return yes_button, no_button

    def interact(self, player):
        if self.card_no not in player.drawn_cards[self.type]:
            player.drawn_cards[self.type].append(self.card_no)

# ======= Tile Subclasses =========

class Start(Tile):
    def __init__(self, window, loc=(0, 0), title=None, description=None):
        super().__init__(window, loc, title, description)
        self.type = "Start"
        self.colour = (28, 252, 43)

class Info(Tile):
    def __init__(self, window, loc=(0, 0), title=None, description=None):
        super().__init__(window, loc, title, description)
        self.type = "Info"
        self.colour = (21, 87, 186)

class HealthMoment(Tile):
    def __init__(self, window, loc=(0, 0), title=None, description=None):
        super().__init__(window, loc, title, description)
        self.type = "HealthMoment"
        self.colour = (153, 51, 255)

class RandomEvent(Tile):
    def __init__(self, window, loc=(0, 0), title=None, description=None):
        super().__init__(window, loc, title, description)
        self.type = "RandomEvent"
        self.colour = (255, 153, 51)

class DecisionPoint(Tile):
    def __init__(self, window, loc=(0, 0), title=None, description=None):
        super().__init__(window, loc, title, description)
        self.type = "DecisionPoint"
        self.colour = (255, 229, 204)

class Finish(Tile):
    def __init__(self, window, loc=(0, 0), title=None, description=None):
        super().__init__(window, loc, title, description)
        self.type = "Finish"
        self.colour = (153, 0, 0)

    def evaluate(self, player):
        if player.drawn_cards['Start'][0] in (1, 2, 3, 4, 5, 6):
            card_no = 1
        else:
            player.risk = 0
            for j, k in zip(player.drawn_cards['HealthMoment'], player.decisions['HealthMoment']):
                player.risk += HEALTHMOMENT[j]['effect'][k]
            for j, k in zip(list(DECISIONPOINT.keys()), player.decisions['DecisionPoint']):
                player.risk += DECISIONPOINT[j]['effect'][k]
            card_no = 2 if player.risk > player.threshold else 3
        self.cards = FINISH[card_no]

# ======= Player Object =========

class Player:
    # for animation of player -> also include emotional reactions and ageing (change of avatar when reaching different tiles)
    def __init__(self, window, start_tile, name=None, img = None):
        self.window = window
        self.current_tile = start_tile
        self.loc = list(start_tile.loc)
        self.target_tile = None
        self.speed = 3
        self.img = img
        self.name = name
        self.threshold = 2 # TODO: determine the threshold by considering how many tiles player would land on
        self.colour = (255, 192, 203)
        self.drawn_cards = {'Start': [],
                            'Info': [],
                            'RandomEvent': [],
                            'HealthMoment': [],}
        
        self.decisions = {'DecisionPoint': [],
                          'HealthMoment': [],}
        self.decision_point = False
        self.health_decision = False
        
    
    def move_to_tile(self, tile):
        # update target tile from move queue
        self.target_tile = tile

    def walk(self):
        if self.target_tile:
            dx = self.target_tile.loc[0] - self.loc[0]
            dy = self.target_tile.loc[1] - self.loc[1]
            dist = (dx ** 2 + dy ** 2) ** 0.5
            time = dist/self.speed 
            if dist < self.speed:
                self.loc = list(self.target_tile.loc)
                # update current position and wait for next iteration to move to the next tile 
                self.current_tile = self.target_tile
            else:
                self.loc[0] += self.speed * dx / dist
                self.loc[1] += self.speed * dy / dist
            
            return time

    def draw(self, camera_offset):
        screen_pos = (self.loc[0] + camera_offset[0], self.loc[1] + camera_offset[1])
        pygame.draw.circle(self.window, self.colour, screen_pos, 15)

# ======= Game Setup =========

def draw_instructions(window):
    popup_rect = pygame.Rect(WIDTH//2 - 200, HEIGHT//2 - 150, 400, 300)
    pygame.draw.rect(window, (240, 240, 240), popup_rect)
    pygame.draw.rect(window, (0, 0, 0), popup_rect, 2)

    font = pygame.font.SysFont(None, 26)
    instructions = (
        #"Welcome to The Game of Life: Breast Health Edition!\n"
        "Press SPACEBAR to roll the dice and move.\n"
        "Make choices and learn how different lifestyle factors affects your breast cancer risk."
    )

    lines = []
    for paragraph in instructions.split('\n'):
        lines.extend(wrap_text(paragraph, font, popup_rect.width - 20))

    y_offset = 15
    for line in lines:
        text_surface = font.render(line, True, (0, 0, 0))
        window.blit(text_surface, (popup_rect.x + 10, popup_rect.y + y_offset))
        y_offset += 28

    return pygame.time.get_ticks()

def get_card_generator():
        # generate random sequence for players to trigger content in tile pop up
        popup_seq = dict()
        for i, j in zip(['Start', 'Info', 'RandomEvent'], [START, INFO, RANDOMEVENT]):
            # shuffle keys
            seq = list(j.keys())
            random.shuffle(seq)
            popup_seq[i] = seq
        return popup_seq

def create_board(window, popup_seq):
    tiles = []
    card_no = popup_seq['Start'].pop(0)
    tile = Start(window, loc=(0, HEIGHT // 2))
    tile.get_card(card_no, START[card_no])
    tiles.append(tile)

    for i in range(1, 19):
        if i in (1, 6, 15, 17):
            card_no = popup_seq['Info'].pop(0)
            tile = Info(window, loc=(i * 150, HEIGHT // 2))
            tile.get_card(card_no, INFO[card_no])
        elif i in (3, 7, 10, 12, 13, 16, 18):
            tile = HealthMoment(window, loc=(i * 150, HEIGHT // 2))
            tile.get_card(i, HEALTHMOMENT[i])
        elif i in (2, 5, 8, 11, 14):
            card_no = popup_seq['RandomEvent'].pop(0)
            tile = RandomEvent(window, loc=(i * 150, HEIGHT // 2))
            tile.get_card(card_no, RANDOMEVENT[card_no])
        elif i in (4, 9):
            tile = DecisionPoint(window, loc=(i * 150, HEIGHT // 2))
            tile.get_card(i, DECISIONPOINT[i])
        else:
            tile = Tile(window, loc=(i * 150, HEIGHT // 2)) # temp filler tiles that does not trigger any actions, can be added later
        tiles.append(tile)
    
    tiles.append(Finish(window, loc=(19 * 150, HEIGHT // 2))) #

    # Link tiles as graph
    for i in range(len(tiles)-1):
        if i not in (4, 9):
            tiles[i].edges = [tiles[i+1]]  # Default path
        else:
            tiles[i].edges = [tiles[i+1], tiles[i+2]]

    return tiles


def link_branched_paths(tiles, branched_tiles = (5, 6), steps = 3):
    # Adjust locations of branching tiles for visible branching
    # Tiles in altering indices on upper and lower branch
    target = branched_tiles[0] + steps * 2
    for i, j in enumerate(branched_tiles):
        for k in range(j, target, 2):
            if k + 2 < target:
                tiles[k].edges = [tiles[k+2]] #i.e. 8 link to 10, 10 link to 12, 9 link to 11, 11 link to 12
            else:
                tiles[k].edges = [tiles[target]]

            if i % 2 == 0:                  # check whether tiles are assigned to upper or lower branch
                tiles[k].loc = (k * 140, HEIGHT // 2 - 100)  # Upper branch
            else:
                tiles[k].loc = ((k-1) * 140, HEIGHT // 2 + 100)  # lower branch   

# ======= Game Loop =========    

if __name__ == "__main__":
    popup_seq = get_card_generator()           
    tiles = create_board(window, popup_seq)
    link_branched_paths(tiles, branched_tiles=(5, 6), steps=2)
    link_branched_paths(tiles, branched_tiles=(10, 11), steps=3)

    player = Player(window, start_tile=tiles[0])
    clock = pygame.time.Clock()
    display_title = True
    running = True
    decision_pending = False
    remaining_steps = 0 
    current = tiles[0]
    player.target_tile = current
    dice_roll = False
    moving = False
    game_end = False
    game_start = pygame.time.get_ticks()


    while running:
        window.fill((255, 255, 255))
        # Display instructions 
        if pygame.time.get_ticks() - game_start < 5000: 
            display_title_time = draw_instructions(window)

        # Set camera centering on player
        camera_offset = (WIDTH // 2 - int(player.loc[0]), HEIGHT // 2 - int(player.loc[1]))

        # Draw edges and tiles for board (paths between tiles)
        for tile in tiles:
            tile.draw_edges(camera_offset)
            tile.draw(camera_offset)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not decision_pending and not moving and remaining_steps == 0 and not game_end and pygame.time.get_ticks() - display_title_time > 7000:
                        # throw dice and update remaining steps
                        dice_roll = random.randint(1, 4)
                        remaining_steps = dice_roll
                        display_dice_time = pygame.time.get_ticks()  
                        card_drawn = False
        
            elif event.type == pygame.MOUSEBUTTONDOWN and decision_pending:
                if isinstance(current, DecisionPoint):
                    if yes_button.collidepoint(event.pos):
                        next_tile = current.edges[0] # set next tile 
                        player.decisions['DecisionPoint'].append(0) # 0 for yes, 1 for no

                    elif no_button.collidepoint(event.pos):
                        next_tile = current.edges[1] # always default to current edge's [1] without update of pop up window
                        player.decisions['DecisionPoint'].append(1)

                    player.decision_point = True
            
                elif isinstance(current, HealthMoment):
                    # Health moment tile to interact 
                    if yes_button.collidepoint(event.pos):
                        player.decisions['HealthMoment'].append(0) # 0 for yes, 1 for no
                        
                    elif no_button.collidepoint(event.pos):
                        player.decisions['HealthMoment'].append(1)

                    player.health_decision = True
                
                decision_pending = False
    
        if remaining_steps > 0 and not moving: # this statement is evaluated at every frame, that means it reached decision point directly
            if current.edges:
                if current.type == "DecisionPoint" and not player.decision_point: # cannot use player.made_decision either as it 
                    decision_pending = True
                    moving = False
                    
                else: # throw the dice first, if in decision tile and not yet made decision
                    if not current.type == "DecisionPoint":
                        next_tile = current.edges[0]
                    elif player.decision_point:
                        current.create_tile_popup(window, player.decisions['DecisionPoint'][-1])
                        pygame.display.update()
                        pygame.time.wait(2000)  # Wait to display decision pop up 
                        
                    player.move_to_tile(next_tile) # set target tile to next tile
                    remaining_steps -= 1
                    current = next_tile
                    player.decision_point = False # once moved the previous decision tile flag is cleared
                    player.health_decision = False 
                    moving = True # does not run becuz moving is true 
            else: 
                game_end = True

        # set decision point as temp destination, set moving to false when reached destination
        if player.loc == list(player.target_tile.loc): 
            moving = False

        # Display dice roll
        if dice_roll and pygame.time.get_ticks() - display_dice_time < 1000:
            font = pygame.font.SysFont(None, 72)
            dice_surface = font.render(f'Dice: {dice_roll}', True, (0, 0, 0))
            window.blit(dice_surface, (WIDTH//2 - dice_surface.get_width()//2, 50))

        
        # Landing on tiles and trigger pop up  
        if remaining_steps == 0 and not isinstance(current, DecisionPoint) and not moving and not game_end:
            if isinstance(current, HealthMoment) and not player.health_decision: # cannot be set to false 
                decision_pending = True # 
            elif isinstance(current, Finish):
                game_end = True
            else:
                if player.health_decision:
                    current.create_tile_popup(window, player.decisions['HealthMoment'][-1])
                elif pygame.time.get_ticks() - display_title_time > 6000: # make sure title is displayed first before start pop up 
                    current.create_tile_popup(window)
                current.interact(player)
            pygame.time.wait(1000) # wait to allow time for reading tile instructions
        elif isinstance(current, DecisionPoint) and player.decision_point:
            # Display pop up tile after decision made in decision point player is still ongoing 
            current.create_tile_popup(window)
            pygame.time.wait(10000)

        # walk updates player position
        if moving:
            player.walk() 
            player.draw(camera_offset)

        # Draw decision popup when passing through health moment and decision point 
        if decision_pending and not moving:
            yes_button, no_button = current.create_decision_popup(window)

        # Game end and evaluate player's lifestyle choices and display pop up
        if game_end:
            current.evaluate(player) # if land on 
            current.create_tile_popup(window)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


