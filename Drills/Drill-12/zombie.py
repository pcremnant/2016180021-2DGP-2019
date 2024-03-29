import random
import math
import game_framework
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
from pico2d import *
import main_state

# zombie Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# zombie Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10

animation_names = ['Attack', 'Dead', 'Idle', 'Walk']


class Zombie:
    images = None

    def load_images(self):
        if Zombie.images is None:
            Zombie.images = {}
            for name in animation_names:
                Zombie.images[name] = [load_image("./zombiefiles/female/" + name + " (%d)" % i + ".png") for i in
                                       range(1, 11)]

    def __init__(self):
        positions = [(43, 750), (1118, 750), (1050, 530), (575, 220), (235, 33), (575, 220), (1050, 530), (1118, 750)]
        self.patrol_positions = []
        for p in positions:
            self.patrol_positions.append((p[0], 1024 - p[1]))
        self.patrol_order = 1
        self.target_x, self.target_y = None, None
        self.x, self.y = self.patrol_positions[0]

        self.x, self.y = 1280 / 4 * 3, 1024 / 4 * 3
        self.load_images()
        self.dir = random.random() * 2 * math.pi  # random moving direction
        self.speed = 0
        self.timer = 1.0  # change direction every 1 sec when wandering
        self.frame = 0
        self.build_behavior_tree()
        self.hp = 0

    def calculate_current_position(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time
        self.x = clamp(50, self.x, 1280 - 50)
        self.y = clamp(50, self.y, 1024 - 50)

    def wander(self):
        self.speed = RUN_SPEED_PPS
        self.calculate_current_position()
        self.timer -= game_framework.frame_time
        if self.timer < 0:
            self.timer += 1.0
            self.dir = random.random() * 2 * math.pi
        return BehaviorTree.SUCCESS
        # fill here
        pass

    def find_player(self):
        boy = main_state.get_boy()
        distance = (boy.x - self.x) ** 2 + (boy.y - self.y) ** 2
        if distance < (PIXEL_PER_METER * 10) ** 2:
            self.dir = math.atan2(boy.y - self.y, boy.x - self.x)
            return BehaviorTree.SUCCESS
        else:
            self.speed = 0
            return BehaviorTree.FAIL
        # fill here
        pass

    def move_to_player(self):
        self.speed = RUN_SPEED_PPS
        self.calculate_current_position()
        return BehaviorTree.SUCCESS
        # fill here
        pass

    def get_next_position(self):
        self.target_x, self.target_y = self.patrol_positions[self.patrol_order % len(self.patrol_positions)]
        self.patrol_order += 1
        self.dir = math.atan2(self.target_y - self.y, self.target_x - self.x)
        return BehaviorTree.SUCCESS
        # fill here
        pass

    def move_to_target(self):
        self.speed = RUN_SPEED_PPS
        self.calculate_current_position()

        distance = (self.target_x - self.x) ** 2 + (self.target_y - self.y) ** 2

        if distance < PIXEL_PER_METER ** 2:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING
        # fill here
        pass

    def find_BigBall(self):
        balls = main_state.get_balls()

        if balls is None:
            return BehaviorTree.FAIL

        big_balls = []
        is_BigBall = False
        for ball in balls:
            if ball.type == 'big':
                is_BigBall = True
                big_balls += [ball]
        if not is_BigBall:
            return BehaviorTree.FAIL

        distance = []
        for ball in big_balls:
            distance += [(self.x - ball.x) ** 2 + (self.y - ball.y) ** 2]
        count = 0
        min_distance = None
        min_index = 0
        for d in distance:
            if min_distance is None:
                min_distance = d
                min_index = count
            elif d < min_distance:
                min_index = count
                min_distance = d
            count += 1

        self.target_x, self.target_y = big_balls[min_index].x, big_balls[min_index].y
        self.dir = math.atan2(self.target_y - self.y, self.target_x - self.x)

        return BehaviorTree.SUCCESS

    def move_to_BigBall(self):
        self.speed = RUN_SPEED_PPS
        self.calculate_current_position()

        distance = (self.target_x - self.x) ** 2 + (self.target_y - self.y) ** 2

        if distance < PIXEL_PER_METER ** 2:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING
        # fill here
        pass

    def eat_BigBall(self):
        balls = main_state.get_balls()

        if balls is None:
            return BehaviorTree.FAIL

        big_balls = []
        for ball in balls:
            if ball.type == 'big':
                big_balls += [ball]

        for ball in big_balls:
            if main_state.collide(main_state.get_zombie(), ball):
                ball.is_delete = True
                self.hp += ball.hp
        pass

    def find_SmallBall(self):
        balls = main_state.get_balls()

        if balls is None:
            return BehaviorTree.FAIL

        Small_balls = []
        is_SmallBall = False
        for ball in balls:
            if ball.type == 'small':
                is_SmallBall = True
                Small_balls += [ball]
        if not is_SmallBall:
            return BehaviorTree.FAIL

        distance = []
        for ball in Small_balls:
            distance += [(self.x - ball.x) ** 2 + (self.y - ball.y) ** 2]
        count = 0
        min_distance = None
        min_index = 0
        for d in distance:
            if min_distance is None:
                min_distance = d
                min_index = count
            elif d < min_distance:
                min_index = count
                min_distance = d
            count += 1

        self.target_x, self.target_y = Small_balls[min_index].x, Small_balls[min_index].y
        self.dir = math.atan2(self.target_y - self.y, self.target_x - self.x)

        return BehaviorTree.SUCCESS

    def move_to_SmallBall(self):
        self.speed = RUN_SPEED_PPS
        self.calculate_current_position()

        distance = (self.target_x - self.x) ** 2 + (self.target_y - self.y) ** 2

        if distance < PIXEL_PER_METER ** 2:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING
        # fill here
        pass

    def eat_SmallBall(self):
        balls = main_state.get_balls()

        if balls is None:
            return BehaviorTree.FAIL

        small_balls = []
        for ball in balls:
            if ball.type == 'small':
                small_balls += [ball]

        for ball in small_balls:
            if main_state.collide(main_state.get_zombie(), ball):
                ball.is_delete = True
                self.hp += ball.hp
        pass

    # def find_player(self):
    #     pass

    # def move_to_player(self):
    #     pass

    def build_behavior_tree(self):
        # wander_node = LeafNode("Wander", self.wander)
        #
        find_player_node = LeafNode("Find Player", self.find_player)
        move_to_player_node = LeafNode("Move to Player", self.move_to_player)
        #
        chase_player_node = SequenceNode("Chase Player")
        chase_player_node.add_children(find_player_node, move_to_player_node)
        #
        # wander_chase_node = SelectorNode("WanderChase")
        # wander_chase_node.add_children(chase_node, wander_node)

        find_BigBall_node = LeafNode("Find BigBall", self.find_BigBall)
        move_to_BigBall_node = LeafNode("Move to BigBall", self.move_to_BigBall)
        eat_BigBall_node = LeafNode("Eat BigBall", self.eat_BigBall)

        find_SmallBall_node = LeafNode("Find SmallBall", self.find_SmallBall)
        move_to_SmallBall_node = LeafNode("Move to SmallBall", self.move_to_SmallBall)
        eat_SmallBall_node = LeafNode("Eat SmallBall", self.eat_SmallBall)

        chase_BigBall_node = SequenceNode("Chase BigBall")
        chase_BigBall_node.add_children(find_BigBall_node, move_to_BigBall_node, eat_BigBall_node)

        chase_SmallBall_node = SequenceNode("Chase SmallBall")
        chase_SmallBall_node.add_children(find_SmallBall_node, move_to_SmallBall_node, eat_SmallBall_node)

        eat_ball_node = SelectorNode("Eat Balls")
        eat_ball_node.add_children(chase_BigBall_node, chase_SmallBall_node)

        chase_node = SelectorNode("Chase")
        chase_node.add_children(eat_ball_node, chase_player_node)

        # self.bt = BehaviorTree(wander_chase_node)
        self.bt = BehaviorTree(chase_node)
        pass

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def update(self):
        self.bt.run()
        # fill here
        pass

    def draw(self):
        if math.cos(self.dir) < 0:
            if self.speed == 0:
                Zombie.images['Idle'][int(self.frame)].composite_draw(0, 'h', self.x, self.y, 100, 100)
            else:
                Zombie.images['Walk'][int(self.frame)].composite_draw(0, 'h', self.x, self.y, 100, 100)
        else:
            if self.speed == 0:
                Zombie.images['Idle'][int(self.frame)].draw(self.x, self.y, 100, 100)
            else:
                Zombie.images['Walk'][int(self.frame)].draw(self.x, self.y, 100, 100)

        print(self.hp)

    def handle_event(self, event):
        pass
