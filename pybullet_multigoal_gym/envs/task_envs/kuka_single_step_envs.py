from pybullet_multigoal_gym.envs.base_envs.kuka_single_step_base_env import KukaBulletMGEnv


class KukaPickAndPlaceEnv(KukaBulletMGEnv):
    def __init__(self, render=True, binary_reward=True, joint_control=False,
                 image_observation=False, goal_image=False, depth_image=False, visualize_target=True,
                 camera_setup=None, observation_cam_id=0, goal_cam_id=0,
                 gripper_type='parallel_jaw'):
        KukaBulletMGEnv.__init__(self, render=render, binary_reward=binary_reward,
                                 image_observation=image_observation, goal_image=goal_image, depth_image=depth_image,
                                 visualize_target=visualize_target,
                                 camera_setup=camera_setup, observation_cam_id=observation_cam_id,
                                 goal_cam_id=goal_cam_id,
                                 gripper_type=gripper_type, obj_range=0.15, target_range=0.15,
                                 target_in_the_air=True,
                                 grasping=True, joint_control=joint_control, has_obj=True)


class KukaPushEnv(KukaBulletMGEnv):
    def __init__(self, render=True, binary_reward=True, joint_control=False,
                 image_observation=False, goal_image=False, depth_image=False, visualize_target=True,
                 camera_setup=None, observation_cam_id=0, goal_cam_id=0,
                 gripper_type='parallel_jaw'):
        KukaBulletMGEnv.__init__(self, render=render, binary_reward=binary_reward,
                                 image_observation=image_observation, goal_image=goal_image, depth_image=depth_image,
                                 visualize_target=visualize_target,
                                 camera_setup=camera_setup, observation_cam_id=observation_cam_id,
                                 goal_cam_id=goal_cam_id,
                                 gripper_type=gripper_type, obj_range=0.15, target_range=0.15,
                                 target_in_the_air=False, end_effector_start_on_table=True,
                                 grasping=False, joint_control=joint_control, has_obj=True)


class KukaReachEnv(KukaBulletMGEnv):
    def __init__(self, render=True, binary_reward=True, joint_control=False,
                 image_observation=False, goal_image=False, depth_image=False, visualize_target=True,
                 camera_setup=None, observation_cam_id=0, goal_cam_id=0,
                 gripper_type='parallel_jaw'):
        KukaBulletMGEnv.__init__(self, render=render, binary_reward=binary_reward,
                                 image_observation=image_observation, goal_image=goal_image, depth_image=depth_image,
                                 visualize_target=visualize_target,
                                 camera_setup=camera_setup, observation_cam_id=observation_cam_id,
                                 goal_cam_id=goal_cam_id,
                                 gripper_type=gripper_type, obj_range=0.15, target_range=0.15,
                                 target_in_the_air=True,
                                 grasping=False, joint_control=joint_control, has_obj=False)


class KukaSlideEnv(KukaBulletMGEnv):
    def __init__(self, render=True, binary_reward=True, joint_control=False,
                 # unused args, just to make it compatible with the make_env() method
                 image_observation=False, goal_image=False, depth_image=False, visualize_target=True,
                 camera_setup=None, observation_cam_id=0, goal_cam_id=0,
                 gripper_type='parallel_jaw'):
        KukaBulletMGEnv.__init__(self, render=render, binary_reward=binary_reward,
                                 image_observation=False,
                                 gripper_type=gripper_type, obj_range=0.1, target_range=0.2,
                                 table_type='long_table', target_in_the_air=False, end_effector_start_on_table=True,
                                 grasping=False, joint_control=joint_control, has_obj=True)
