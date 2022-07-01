from metadrive.component.vehicle.vehicle_type import DefaultVehicle
from metadrive.envs.metadrive_env import MetaDriveEnv
from metadrive.utils import setup_logger

length_factor = 2
width_factor = 2
height_factor = 2

x_offset=0
y_offset=0
z_offset=1

heading = 90

DefaultVehicle.path = ['', (length_factor, width_factor, height_factor), (x_offset, y_offset, z_offset), heading]

if __name__ == "__main__":
    setup_logger(True)
    env = MetaDriveEnv(
        {
            "environment_num": 10,
            "traffic_density": 0,
            "traffic_mode": "trigger",
            "start_seed": 22,
            # "_disable_detector_mask":True,
            # "debug_physics_world": True,
            "global_light": True,
            # "debug_static_world":True,
            "cull_scene": False,
            # "offscreen_render": True,
            # "controller": "joystick",
            "manual_control": True,
            "use_render": True,
            "decision_repeat": 5,
            "need_inverse_traffic": True,
            "rgb_clip": True,
            "debug": False,
        }
    )
    import time

    start = time.time()
    o = env.reset()
    env.vehicle.set_velocity([1, 0.1], 10)
    print(env.vehicle.speed)

    for s in range(1, 10000):
        o, r, d, info = env.step(env.action_space.sample())
        # if s % 100 == 0:
        #     env.close()
        #     env.reset()
        # info["fuel"] = env.vehicle.energy_consumption
        # env.render(
        #     text={
        #         "heading_diff": env.vehicle.heading_diff(env.vehicle.lane),
        #         "engine_force": env.vehicle.config["max_engine_force"],
        #         "current_seed": env.current_seed,
        #         "lane_width": env.vehicle.lane.width
        #     }
        # )
        # # assert env.observation_space.contains(o)
        # if (s + 1) % 100 == 0:
        #     print(
        #         "Finish {}/10000 simulation steps. Time elapse: {:.4f}. Average FPS: {:.4f}".format(
        #             s + 1,f
        #             time.time() - start, (s + 1) / (time.time() - start)
        #         )
        #     )
        if d:
            #     # env.close()
            #     print(len(env.engine._spawned_objects))
            env.reset()
