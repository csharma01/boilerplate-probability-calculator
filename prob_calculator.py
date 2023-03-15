import random
from collections import Counter

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            self.contents += [key] * value
    
    def draw(self, num):
        if num >= len(self.contents):
            return self.contents
        
        drawn_balls = random.sample(self.contents, num)
        for ball in drawn_balls:
            self.contents.remove(ball)
        
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    
    for i in range(num_experiments):
        hat_copy = Hat(**dict(Counter(hat.contents)))
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_balls_counter = Counter(drawn_balls)
        
        success = True
        for key, value in expected_balls.items():
            if drawn_balls_counter[key] < value:
                success = False
                break
        
        if success:
            count += 1
    
    return count / num_experiments
