"""Defined a robot model """
from robot_app.views import console


DEFAULT_ROBOT_NAME = 'Ronaldo'


class Robot(object):
    """Base model for Robot."""

    def __init__(self, name=DEFAULT_ROBOT_NAME, user_name='',
                 speak_color='green'):
        self.name = name
        self.user_name = user_name
        self.speak_color = speak_color

    def hello(self):
        """Returns words to the user that the robot speaks at the beginning."""

        # view 에서 설정한 것을 불러오기(사용자에게 보여줄 것은 view에 저장하기 때문)
        while True:
            template = console.get_template('hello.txt', self.speak_color)
            user_name = input(template.substitute({
                'robot_name': self.name}))

            if user_name:
                self.user_name = user_name.title()
                break

class RestaurantRobot(Robot):

    def __init__(self, name=DEFAULT_ROBOT_NAME):
        super().__init__()
