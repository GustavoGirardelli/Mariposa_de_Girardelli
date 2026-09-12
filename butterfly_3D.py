import sys
# butterfly_3D.py

# python3 butterfly_3D.py
# blender --python ./butterfly_3D.py

# 3D Langton's Ant - Clock rule +3h (4 states)
# Rule: Right(3h)->Down(6h)->Left(9h)->Up(12h)->Right
# Hamann notation: R D L U (DLUR permutation)
# Highway measurable: velocity ~0.0636, displacement ~ (45,0,45) per 1000 steps
# chaos exit ~52 steps, internal period ~40


import math

try:
    import bpy
    from mathutils import Vector, Matrix
    HAS_BLENDER = True
except ImportError:
    HAS_BLENDER = False

# Directions: 0:+X 1:-X 2:+Y 3:-Y 4:+Z 5:-Z
DIRECTIONS = {0:(1,0,0), 1:(-1,0,0), 2:(0,1,0), 3:(0,-1,0), 4:(0,0,1), 5:(0,0,-1)}
OPPOSITE = {0:1, 1:0, 2:3, 3:2, 4:5, 5:4}
def opposite_of(d): return OPPOSITE[d]

# 4-state clock rule
RULES_4 = {'Right':'Down','Down':'Left','Left':'Up','Up':'Right'}
RULES = RULES_4

# Transform orientation triad (right, front, up)
def transform_orientation(right, front, up, action):
    if action == 'Right':
        return (opposite_of(front), right, up)
    elif action == 'Left':
        return (front, opposite_of(right), up)
    elif action == 'Up':
        return (right, up, opposite_of(front))
    elif action == 'Down':
        return (right, opposite_of(up), front)

def advance_position(pos, front):
    v = DIRECTIONS[front]
    return (pos[0]+v[0], pos[1]+v[1], pos[2]+v[2])

def execute_step(pos, orient, cell_state):
    r,f,u = orient
    action = RULES[cell_state]
    new_orient = transform_orientation(r,f,u, action)
    return advance_position(pos, new_orient[1]), new_orient

# Grid
cells = {}
def query_voxel(pos):
    k = (int(pos[0]), int(pos[1]), int(pos[2]))
    return cells.get(k, list(RULES.keys())[0])
def set_voxel(pos, state):
    k = (int(pos[0]), int(pos[1]), int(pos[2]))
    cells[k] = state

def run_headless(steps=int(sys.argv[1]) if len(sys.argv)>1 else 4000):
    global cells
    cells = {}
    pos = (0,0,0)
    orient = (0,2,4) # right +X, front +Y, up +Z
    for i in range(steps):
        s = query_voxel(pos)
        set_voxel(pos, RULES[s])
        pos, orient = execute_step(pos, orient, s)
        if i % 1000 == 0:
            dist = (pos[0]**2+pos[1]**2+pos[2]**2)**0.5
            vel = dist/(i+1) if i>0 else 0
            print(f"{i} pos={pos} dist={dist:.1f} vel={vel:.4f} cells={len(cells)}")

if __name__ == "__main__":
    run_headless(int(sys.argv[1]) if len(sys.argv)>1 else 4000)
