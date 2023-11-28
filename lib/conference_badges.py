def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    new_list = [f"Hello, my name is {name}." for name in names]
    return new_list

def assign_rooms(speakers):
    rooms = [1, 2, 3, 4, 5, 6, 7]
    assigned_rooms = []

    for idx, name in enumerate(speakers):
        assigned_rooms = []
    for idx, speaker in enumerate(speakers, start=1):
        assigned_rooms.append(f"Hello, {speaker}! You'll be assigned to room {idx}!")
    return assigned_rooms

def printer(names):
    badges = batch_badge_creator(names)
    rooms = assign_rooms(names)

    for badge in badges:
        print(badge)
    for room_assignment in rooms:
        print(room_assignment)

