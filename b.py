current_floor = 0  # Assuming the person starts on the ground floor

while True:
    user_input = input("Enter input (up/down/()): ")

    if "(" in user_input:
        current_floor += 1
    elif ")" in user_input:
        current_floor -= 1
    elif user_input.lower() == "()":
        pass  # If the input is (), do nothing (stay on the same floor)
    else:
        print("Invalid input. Please enter 'up', 'down', or '()'.")
        continue

    print("Current floor:", current_floor)


