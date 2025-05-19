import numpy as np
from isaacsim.core.api import world
from isaacsim.core.api.objects import DynamicCuboid

# from isaacsim.core import World
# from isaacsim.core.objects import DynamicCuboid

world = World()
world.scene.add_default_ground_plane()

cube = DynamicCuboid(
    prim_path="/World/Cube",
    name="my_cube",
    position=[0, 0, 1.0],
    size=0.5,
    color=np.array([0.2, 0.6, 1.0]),  
)

world.reset()