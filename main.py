import math

class Voxel:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def get_voxel_traversal(start_x, start_y, start_z, target_x, target_y, target_z):
  
    SHIFTED_EYE_DISTANCE = 1.600045
    distance = round(math.hypot(start_x - target_x, (start_y + SHIFTED_EYE_DISTANCE - target_y - SHIFTED_EYE_DISTANCE) + SHIFTED_EYE_DISTANCE, start_z - target_z))
    
    voxel_traversal = []
    
    delta_x = (target_x - start_x) / distance
    delta_y = (target_y - 1 - start_y) / distance
    delta_z = (target_z - start_z) / distance
    
    for _ in range(distance + 1):
        voxel = Voxel(round(start_x), round(start_y), round(start_z))
        voxel_traversal.append(voxel)
    
        start_x += delta_x
        start_y += delta_y
        start_z += delta_z
    
    return voxel_traversal
