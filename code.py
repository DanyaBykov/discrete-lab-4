"""
This module represents a state machine that represents my day.
"""
import random

def prime(fn):
    """
    This function is a decorator that initializes the generator function.
    """
    def wrapper(*args, **kwargs):
        v = fn(*args, **kwargs)
        v.send(None)
        return v
    return wrapper

class MyDay:
    """
    This class represents my day.
    """
    def __init__(self):
        self.start = self._create_start()
        self.q1 = self._create_q1()
        self.q2 = self._create_q2()
        self.q3 = self._create_q3()
        self.q4 = self._create_q4()
        self.q5 = self._create_q5()
        self.q6 = self._create_q6()
        self.q7 = self._create_q7()
        self.q8 = self._create_q8()
        self.q9 = self._create_q9()
        self.q10 = self._create_q10()
        self.q11 = self._create_q11()
        self.q12 = self._create_q12()
        self.q13 = self._create_q13()
        self.q14 = self._create_q14()
        self.q15 = self._create_q15()
        self.q16 = self._create_q16()
        self.current_state = self.start
        self.hour = 8
        self.end = False

    @prime
    def _create_start(self):
        while True:
            _ = yield
            random_number = random.random()
            print(f"--Current time is {int(self.hour)}:{int((self.hour % 1) * 60):02d}--")
            if self.hour == 8 and random_number > 0.3:
                print('Wakey wakey eggs and bakey!')
                self.current_state = self.q1
            elif self.hour == 8 and random_number <= 0.3:
                self.current_state = self.q2
                self.hour += 2

    @prime
    def _create_q1(self):
        while True:
            _ = yield
            print(f"--Current time is {int(self.hour)}:{int((self.hour % 1) * 60):02d}--")
            print('I woke up at 8 and want to sleep more!')
            self.current_state = self.q6
            self.hour += 0.25

    @prime
    def _create_q2(self):
        while True:
            _ = yield
            random_number = random.random()
            print('Zzzzzzz')
            print(f"--Current time is {int(self.hour)}:{int((self.hour % 1) * 60):02d}--")
            if self.hour == 10 and random_number > 0.3:
                print('Zzzzzzz')
                self.current_state = self.q4
            elif self.hour == 10 and random_number <= 0.3:
                print('Zzzzzzz')
                self.current_state = self.q3
                self.hour += 1.5

    @prime
    def _create_q3(self):
        while True:
            _ = yield
            print(f"--Current time is {int(self.hour)}:{int((self.hour % 1) * 60):02d}--")
            print('Oh no! I missed all my classes today!')
            self.current_state = self.q8
            self.hour += 0.5

    @prime
    def _create_q4(self):
        while True:
            _ = yield
            print('Oh no! I overslept and missed my first class!')
            self.current_state = self.q5
            self.hour += 0.5

    @prime
    def _create_q5(self):
        while True:
            _ = yield
            print(f"--Current time is {int(self.hour)}:{int((self.hour % 1) * 60):02d}--")
            print('Time to study!')
            self.current_state = self.q8
            self.hour += 1.5

    @prime
    def _create_q6(self):
        while True:
            _ = yield
            print(f"--Current time is {int(self.hour)}:{int((self.hour % 1) * 60):02d}--")
            print('Yay! Coffee time!')
            self.current_state = self.q7
            self.hour += 0.25

    @prime
    def _create_q7(self):
        while True:
            _ = yield
            print(f"--Current time is {int(self.hour)}:{int((self.hour % 1) * 60):02d}--")
            print('Time to study!')
            self.current_state = self.q8
            self.hour += 3.5

    @prime
    def _create_q8(self):
        while True:
            _ = yield
            print(f"--Current time is {int(self.hour)}:{int((self.hour % 1) * 60):02d}--")
            print('Time to eat!')
            random_number = random.random()
            if self.hour == 12 and random_number <= 0.3:
                self.current_state = self.q10
                self.hour += 0.5
            elif self.hour == 12 and random_number > 0.3:
                self.current_state = self.q9

    @prime
    def _create_q9(self):
        while True:
            _ = yield
            print(f"--Current time is {int(self.hour)}:{int((self.hour % 1) * 60):02d}--")
            print('Yay time for more coffee!')
            self.current_state = self.q10
            self.hour += 0.5

    @prime
    def _create_q10(self):
        while True:
            _ = yield
            print(f"--Current time is {int(self.hour)}:{int((self.hour % 1) * 60):02d}--")
            print('Time to rest a little bit')
            self.current_state = self.q11
            self.hour += 1.5

    @prime
    def _create_q11(self):
        while True:
            _ = yield
            random_number = random.random()
            print(f"--Current time is {int(self.hour)}:{int((self.hour % 1) * 60):02d}--")
            print('Time to go to for a walk!')
            if self.hour == 14 and random_number == 0.1:
                print('Oh no not the car')
                print('With great power comes great responsibility')
                self.current_state = self.q12
            elif self.hour == 14 and random_number != 0.1:
                self.current_state = self.q13
                self.hour += 2

    @prime
    def _create_q12(self):
        while True:
            _ = yield
            self.hour += 1
            print(f"--Current time is {int(self.hour)}:{int((self.hour % 1) * 60):02d}--")
            print('Man, I`m dead')
            self.current_state = self.end

    @prime
    def _create_q13(self):
        while True:
            _ = yield
            print(f"--Current time is {int(self.hour)}:{int((self.hour % 1) * 60):02d}--")
            print('Time to go to study again!')
            self.current_state = self.q14
            self.hour += 3

    @prime
    def _create_q14(self):
        while True:
            _ = yield
            print(f"--Current time is {int(self.hour)}:{int((self.hour % 1) * 60):02d}--")
            print('Time to eat!')
            self.current_state = self.q15
            self.hour += 1

    @prime
    def _create_q15(self):
        while True:
            _ = yield
            print(f"--Current time is {int(self.hour)}:{int((self.hour % 1) * 60):02d}--")
            print('It`s time for some rest!')
            self.current_state = self.q16
            self.hour += 3

    @prime
    def _create_q16(self):
        while True:
            _ = yield
            print(f"--Current time is {int(self.hour)}:{int((self.hour % 1) * 60):02d}--")
            print('Time to go to bed!')
            self.current_state = self.end
            self.hour += 1

day = MyDay()
while not day.end:
    try:
        day.current_state.send(None)
    except AttributeError:
        break
