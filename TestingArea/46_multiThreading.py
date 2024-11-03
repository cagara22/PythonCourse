import threading
import time


def walk_the_dog(name, loc):
    time.sleep(8)
    print(f"You finished walking {name} the dog from the {loc}!")


def take_out_trash():
    time.sleep(2)
    print("You took out the trash!")


def get_mail():
    time.sleep(4)
    print("You got the mail!")


thread1 = threading.Thread(target=walk_the_dog, args=("John", "Park"))
thread1.start()
thread2 = threading.Thread(target=take_out_trash)
thread2.start()
thread3 = threading.Thread(target=get_mail)
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print("All chores are complete!")

# walk_the_dog()
# take_out_trash()
# get_mail()
