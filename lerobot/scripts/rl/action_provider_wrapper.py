def make_il_action_provider(model_server_url: str):
    from tacta.control.gym_env.flexiv_env.action_provider import ModelInferenceProviderConfig, ModelInferenceProvider
    action_transform = {"type": "snap_joints", "enabled": True}
    # action_transform = {"type": "deadband", "enabled": True}
    provider_cfg = ModelInferenceProviderConfig(model_server_url=model_server_url, action_transform=action_transform)
    return ModelInferenceProvider(provider_cfg)
