
from pygame import font, Surface


class ScoreBar:
    """
    A bar that displays the score at the top of the screen
    """
    # Member variables
    __pos = None           # A tuple of integers containing the xy coordinates of the score bar on the screen
    __score = None         # The score to be displayed
    font = None            # The font that the score is displayed with
    score_bar_text = None  # The text object for the words in front of the score
    score_text = None      # The text object for the score

    def __init__(self, pos, score=0):
        """
        Constructor.

        :param pos:    A tuple of integers containing the xy coordinates of the score bar on the screen
        :param score:  The score to be displayed
        """
        self.__pos = pos
        self.__score = score
        self.font = font.SysFont("Verdana", 20)
        self.score_bar_text = self.font.render("Score: ", False, (255, 255, 255))
        self.score_text = self.font.render(str(score), False, (255, 255, 255))

    def draw(self, surface):
        """
        Draws the score bar to the given surface.

        :param surface:  The surface to draw the score bar onto
        """
        x, y = self.__pos
        Surface.blit(surface, self.score_bar_text, (x, y))
        Surface.blit(surface, self.score_text, (x + self.score_bar_text.get_width(), y))

    def get_pos(self):
        """
        Returns the position of the score bar.

        :return:  A tuple of integers containing the xy coordinates of the score bar on the screen
        """
        return self.__pos

    def get_score(self):
        """
        Returns the current score.

        :return:  An int representing the current score
        """
        return self.__score

    def increment(self):
        """
        Adds 1 to the score.
        """
        self.__score += 1
        self.set_score(self.__score)

    def set_pos(self, new_pos):
        """
        Sets the position of the score bar to the given value.

        :param new_pos:  The new position to set the score bar's position to
        """
        self.__pos = new_pos

    def set_score(self, new_score):
        """
        Sets the score to the given value.

        :param new_score:  The value to set the score to
        """
        self.__score = new_score
        self.score_text = self.font.render(str(new_score), False, (255, 255, 255))


class HighScoreBar(ScoreBar):
    """
    A bar that shows the high score.

    The high score is saved in a file in the Snake directory.
    """
    def __init__(self, pos):
        """
        Constructor.

        :param pos:  A tuple of integers containing the xy coordinates of the high score bar on the screen
        """
        super(HighScoreBar, self).__init__(pos)

        self.score_bar_text = self.score_bar_text = self.font.render("Highscore: ", False, (255, 255, 255))

        # Check for the high score file and create one if there isn't one
        try:
            with open('score.txt', 'r') as file:
                self.set_score(int(file.read()))
        except FileNotFoundError:
            pass

    def draw(self, surface):
        """
        Draws the score bar to the given surface.

        :param surface:  The surface to draw the score bar onto
        """
        x, y = self.get_pos()
        Surface.blit(surface, self.score_bar_text, (x, y))
        Surface.blit(surface, self.score_text, (x + self.score_bar_text.get_width(), y))

    def save(self):
        """
        Saves the high score to the score.txt file.
        """
        with open('score.txt', 'w+') as file:
            file.write(str(self.get_score()))

    def update(self, current_score):
        """
        Sets the high score to the current score if the current score is higher than the high score.

        :param current_score:  The current score of the player
        """
        if current_score > self.get_score():
            self.set_score(current_score)
