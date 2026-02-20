from tacta.control.gym_env.flexiv_env.reset_action_provider import (
    ResetActionProvider,
    ResetActionProviderConfig,
)
from tacta.control.gym_env.flexiv_env.teleop_wrapper import (
    SpaceMouseWrapper,
)

def get_reset_action_provider(env, config: ResetActionProviderConfig):
    # Build reset action provider (finds SpaceMouseWrapper for intervention support)
    spacemouse_wrapper = env
    while spacemouse_wrapper is not None and not isinstance(spacemouse_wrapper, SpaceMouseWrapper):
        spacemouse_wrapper = getattr(spacemouse_wrapper, "env", None)

    if config.enabled:
        reset_provider = ResetActionProvider(
            config=config,
            motion_interface=env.unwrapped.motion_interface,
            tacta_hand=env.unwrapped.tacta_hand,
            teleop_wrapper=spacemouse_wrapper,
        )
    else:
        reset_provider = None
    return reset_provider