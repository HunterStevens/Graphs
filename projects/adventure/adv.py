from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

def short_traversal_path(traveler):
    path = []
    rooms = Stack()
    visited = set()
    rooms_left = len(literal_eval(open(map_file, "r").read()))
    # print(rooms_left)
    print(f"start: {traveler.current_room.name}")
    cur_room = traveler.current_room
    rooms.push([[cur_room, "start"]])

    while rooms_left > 0:
        r = rooms.pop()
        # print(f"r: {r}")
        last_r = r[-1][0]
        # print(f"last_r: {last_r}")
        if last_r not in visited:
            # print(r.id)
            visited.add(last_r)
            rooms_left -= 1

            found = False
            for nxt_rooms in last_r.get_exits():                
                check = last_r.get_room_in_direction(nxt_rooms)
                # print(check.id)
                if check is not None:
                    # print(f"check is not in visited:{check.name}")
                    print(nxt_rooms)
                    copy_r = r.copy()
                    copy_r.append([check, nxt_rooms])
                    # traveler.travel(nxt_rooms)
                    rooms.push(copy_r)
                    # path.append(nxt_rooms)
                    found = True
                    break
            # print("broke for loop")

            if found == False:
                # print("found == false")
                if rooms_left > 0:
                    copy_r = r.copy()
                    
                    bfs_from_room(visited, last_r, copy_r)
                    rooms.push(copy_r)

        else:
            copy_r = r.copy()
            bfs_from_room(visited, last_r, copy_r)
            rooms.push(copy_r)
            rooms_left -= 1
    
    final_list = rooms.pop()
    # print("\n")
    for i in final_list:
        # print(i[1])
        if i[1] != 'start':
            path.append(i[1])
    print(f"final path: {path}")
    return path

def bfs_from_room(visited, traveler, rooms):
    # print("\n")
    # print(f"bfs_from_room activated at: {traveler.name}")
    # add_path = []
    room_q = Queue()
    room_q.enqueue([[traveler, "start"]])
    new_visited = set()

    while room_q.size() > 0:
        q_list = room_q.dequeue()
        # print(f"q_list: {q_list}")
        last = q_list[-1][0]
        # print(f"last: {last.name}")
        if last not in new_visited:
            if last not in visited:
                visited.add(last)
                add_list = q_list.copy()
                # print(f"add_list {add_list}")
                for i in add_list:
                    rooms.append(i)
                return rooms
            else:
                new_visited.add(last)
                for nxt_rooms in last.get_exits():
                    new_room = last.get_room_in_direction(nxt_rooms)
                    if new_room is not None:
                        copy_q = q_list.copy()
                        copy_q.append([new_room,nxt_rooms])
                        room_q.enqueue(copy_q)

traversal_path = list(short_traversal_path(player))

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
