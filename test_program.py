from controller import Controller
import time

x = Controller(4)

print("\nPut car at stop sign 3")

x.new_car(2)

print(x.queue)

time.sleep(1)

print("\nPut car at stop sign 1")

x.new_car(0)

print(x.queue)

print("\nRemove car at front of queue")

x.remove_car()

print(x.queue)

print("\nCheck safety of sign 2")
x.check_safety(2)

print("\nCheck safety of sign 1")
x.check_safety(0)

time.sleep(3)
print("\nCheck safety of sign 1 after 3 secs")

x.check_safety(0)