from controller import Controller

x = Controller(4)

print("Default State:")
print(x)

print("\nPut car at stop sign 3")

x.new_car(2)

print(x)
print(x.queue)

print("\nPut car at stop sign 1")

x.new_car(0)

print(x)
print(x.queue)

x.remove_car()

print(x)
print(x.queue)

print("\nCheck safety of sign 2")
x.check_safety(2)

print("\nCheck safety of sign 3")
x.check_safety(3)