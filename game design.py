def welcome():
    print('You have been enchanted as a mermaid by the villain wanting '
          'you to die in the sea. You must swim through a maze trying to'
          ' figure out how to escape from the enchantment placed upon you.'
          ' Your ally is waiting for you past the last gate. '
          'Your foe is blocking this gate, stopping you from escaping '
          'with the ingredients with which you need to cancel the enchantment.')


player_name = input()


def show_instructions():
    print(' INSTRUCTIONS ',
          'To move about, type commands: go South, go North, go East, go West',
          'To pick up an item, type: pick up item name',
          'To get the current game status, type: status',
          'To show the instructions again, type: instructions',
          'To quit the game, type: quit or exit')


def game_start():
    print('GAME START')


def rooms():
    rooms={'Entrance', 'Coral', 'Kelp', 'Clams', 'Reef', 'Abyss', 'Cave', 'Sandbar', 'Villain', 'Ally'}
directions = ['North', 'South', 'East', 'West']


def main():
    rooms = {
        'Entrance': {
            'name': 'Entrance', 'South': 'Coral', 'East': 'Clams',
        },
        'Coral': {
            'name': 'Coral', 'North': 'Entrance', 'East': 'Kelp', 'South': 'Sandbar', 'item': 'Purple Coral',
        },
        'Kelp': {
            'name': 'Kelp', 'East': 'Cave', 'West': 'Coral', 'item': 'Kelp Piece',
        },
        'Clams': {
            'name': 'Clams', 'East': 'Abyss', 'North': 'Reef', 'South': 'Cave', 'West': 'Entrance',
            'item': 'Black Pearl',
        },
        'Reef': {
            'name': 'Reef', 'South': 'Clams', 'item': 'Starfish',
        },
        'Abyss': {
            'name': 'Abyss', 'West': 'Clams', 'South': 'Villain',
        },
        'Cave': {
            'name': 'Cave', 'East': 'Villain', 'North': 'Clams', 'West': 'Kelp', 'item': 'Pieces of Stone',
        },
        'Sandbar': {
            'name': 'Sandbar', 'North': 'Coral',
        },
        'Villain': {
            'name': 'Villain', 'South': 'Ally',
        },
        'Ally': {
            'name': 'Ally',
        }
    }
    current_room = 'Entrance'

current_room = 'Entrance'
def move_between_rooms(current_room,  rooms):
    current_room = rooms[current_room]
    return current_room


def pick_up(current_room, rooms, inventory):
    inventory.append(rooms[current_room]['item'])
    del rooms[current_room]['item']

command = input('Which way do you want to go?')
if current_room: move_between_rooms(current_room, rooms)
print('You are in {}'.format(current_room['rooms']))
if command in directions:
    if command in current_room:
        current_room = rooms[current_room[command]]
    else:
        print('You are unable to go that way. Go another way')
elif command == 'quit':
    print('Thanks for playing!')
if current_room['name'] == 'Villain':
    print(
'Watch out! You found the villain! You have a way get past! \n'
'Use your [Knife] and [Pieces of Stone] to get past!'
    )
elif current_room['name'] == 'Ally':
    print('Congratulations! Your Ally will help you disenchant your mermaid tail \n '
          'and help you regrow your human legs! You must have [Purple Coral], [Starfish],\n'
          '[Black Pearl], and [Kelp Piece] for them to make the potion!')
