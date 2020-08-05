from robot_app.models import robot


def talk_about_restaurant():
    # 레스토랑 로봇 생성(모델에서 객체 생성)
    my_robot = robot.Robot()
    # 로봇 헬로(객체에서 헬로함수 불러오기)
    my_robot.hello()
    # 로봇 추천(객체에서 추천함수 불러오기)
    # 유저 좋아하는 것 물어보기(추천 받아와 모델에서 저장)
    # 고맙습니다(모델 바이함수 불러오기)