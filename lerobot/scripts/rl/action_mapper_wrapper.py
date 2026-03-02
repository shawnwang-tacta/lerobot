import torch
import numpy as np

def map_action(action: torch.Tensor, action_mapper):
    # Map from 4D [eef_pos (3), hand_open_close (1)] to 21D [eef_pos (3), eef_ori (3), finger_joints (15)]
    # Expect: action.size()=torch.Size([1, 4])
    action_np = action.squeeze().cpu().numpy()
    action_arm_pos = action_np[:3]
    action_arm_ori = np.zeros_like(action_arm_pos)
    action_hand = action_np[[3]]
    action_hand_mapped = action_mapper.map(action_hand)
    action_mapped_np = np.concatenate([action_arm_pos, action_arm_ori, action_hand_mapped])
    action = torch.Tensor(action_mapped_np).unsqueeze(0)
    return action