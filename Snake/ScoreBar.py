
from pygame import Surface, font


class ScoreBar:
    """A bar that displays the score at the top of the screen"""

    # Member variables
    __score = 0              # The score to be displayed
    __font = None            # The font that the score is displayed with
    __score_bar_text = None  # The text object for the words in front of the score
    __score_text = None      # The text object for the score

    def __init__(self, score=0):
        """Constructor"""
        self.__score = score
        self.__font = font.SysFont("Verdana", 20)
        self.__score_bar_text = self.__font.render("Score: ", False, (255, 255, 255))
        self.__score_text = self.__font.render(str(score), False, (255, 255, 255))

    def draw(self, surface):
        """Draws the scorebar to the given surface"""
        Surface.blit(surface, self.__score_bar_text, (15, 10))
        Surface.blit(surface, self.__score_text, (25 + self.__font.size("Score")[0], 10))

    def get_score(self):
        """Returns the score"""
        return self.__score

    def increment(self):
        """Adds 1 to the score"""
        self.__score += 1
        self.set_score(self.__score)

    def set_score(self, new_score):
        """Sets the score to the given value"""
        self.__score_text = self.__font.render(str(new_score), False, (255, 255, 255))
