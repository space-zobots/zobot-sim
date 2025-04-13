import omni.ext
from isaacsim import SimulationApp


simulation_app = SimulationApp({
    "headless": False,
    "renderer": "RayTracedLighting",
    "exts": [
        "isaacsim.ros2.bridge"
    ]
})
ext_manager = omni.kit.app.get_app().get_extension_manager()
ext_manager.set_extension_enabled_immediate("isaacsim.ros2.bridge", True)
# ext_manager.set_extension_enabled_immediate("isaacsim.ros2.bridge.ROS2BridgeExtension", True)
from isaacsim.ros2.bridge import ROS2BridgeExtension

ros2_bridge = ROS2BridgeExtension()

# ros2_bridge.create_primitive_spawner()

while simulation_app.is_running():
    simulation_app.update()

# Graceful shutdown
simulation_app.close()
