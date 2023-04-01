import arcade

ROW_COUNT = 8
COLUMN_COUNT = 8

SPRITE_SCALING = 0.5


WIDTH = 80
HEIGHT = 80
MOVEMENT_SPEED = 20


MARGIN = 5

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Snail Game"


class Player(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        
        if self.left < 10:
            self.left = 10
        elif self.right > SCREEN_WIDTH - 10:
            self.right = SCREEN_WIDTH - 10

        if self.bottom < 15:
            self.bottom = 15
        elif self.top > SCREEN_HEIGHT - 15:
            self.top = SCREEN_HEIGHT - 15

class MyGame(arcade.Window):
    def __init__(self, width, height, title):

        super().__init__(width, height, title)
        self.grid = []
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0) 

        # self.player_list = None
        # self.player_sprite = None
        arcade.set_background_color(arcade.color.BLACK)
        
    def setup(self):
        self.playerList_1 = []
        self.playerList_2 = []
        self.player1_score = 0
        self.player2_score = 0
        
        self.player_list = arcade.SpriteList()
        self.turn = 0
        # Set up the player
        self.player_sprite = Player(":resources:images/animated_characters/female_person/femalePerson_idle.png", SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)
        # second sprite
        self.player_sprite = Player(":resources:images/animated_characters/female_person/femalePerson_idle.png", SPRITE_SCALING)
        self.player_sprite.center_x = 560
        self.player_sprite.center_y = 560
        self.player_list.append(self.player_sprite)
        
    def on_update(self, delta_time):
        self.player_list.update() 
        


    def on_draw(self):
        self.clear()
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                else:
                    color = arcade.color.WHITE
                    
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

        self.player_list.draw()
    
    def on_key_press(self, key, modifiers):
        if self.turn == 0:
            self.player_sprite = self.player_list[0]
            if key == arcade.key.UP:
                 self.player_sprite.center_y += (WIDTH + MARGIN)
                 self.player1_score += 1
                
            elif key == arcade.key.DOWN:
                self.player_sprite.center_y  -= (WIDTH + MARGIN)
                self.player1_score += 1
                
            elif key == arcade.key.LEFT:
                self.player_sprite.center_x -= (HEIGHT + MARGIN)
                self.player1_score += 1
                
            elif key == arcade.key.RIGHT:
                self.player_sprite.center_x += (HEIGHT + MARGIN)
                self.player1_score += 1
                
            print('Player 1 score is:',self.player1_score)
            self.turn=1
        else:
            self.player_sprite = self.player_list[1] 
            if key == arcade.key.UP:
                self.player_sprite.center_y += (WIDTH + MARGIN)
                self.player2_score += 1
                
            elif key == arcade.key.DOWN:
                self.player_sprite.center_y  -= (WIDTH + MARGIN)
                self.player2_score += 1
                
            elif key == arcade.key.LEFT:
                self.player_sprite.center_x -= (HEIGHT + MARGIN)
                self.player2_score += 1
                
            elif key == arcade.key.RIGHT:
                self.player_sprite.center_x += (HEIGHT + MARGIN)
                self.player2_score += 1
            print('Player 2 Score is:  ',self.player2_score)
            self.turn=0
                
def main():

    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    game.run()


if __name__ == "__main__":
    main()