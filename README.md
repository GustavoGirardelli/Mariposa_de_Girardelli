# 3D Clock Ant - Highway

4-state bisection-free 3D Langton's Ant.

- Rule: RLUD / DLUR - cyclic +3h rotation around triad (Diestra/Frente/Cielo)
- States: Derecha->Baja->Izquierda->Sube
- Implementation: triad rotation, infinite dict grid
- Measurements (4000 steps):
    0 pos=(0, 0, -1) dist=1.0 vel=0.0000 cells=1
    1000 pos=(44, 0, 43) dist=61.5 vel=0.0615 cells=457
    2000 pos=(89, 1, 89) dist=125.9 vel=0.0629 cells=912
    3000 pos=(135, -1, 135) dist=190.9 vel=0.0636 cells=1366
    4000 pos=(181, 1, 179) dist=254.6 vel=0.0636 cells=1821
- Highway vector: approx (45,0,45) per 1000 steps, constant velocity confirms highway
- Code: butterfly_3D.py headless + Blender optional

Compatible with mrcamoga/langton-s-ant rule format R L U D
