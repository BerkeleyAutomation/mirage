import torch
import torch.nn as nn

class ForwardDynamicsModel(nn.Module):
    def __init__(self, model_path='/home/lawrence/xembody/robomimic/forward_dynamics/forward_dynamics_bc_img_300.pth'):
        super(ForwardDynamicsModel, self).__init__()
        # hidden_dims=[256, 256, 256]
        hidden_dims=[32]
        layers = []
        layers.append(nn.Linear(16, hidden_dims[0]))
        layers.append(nn.ReLU())
        for l in range(len(hidden_dims)):
            if l == len(hidden_dims) - 1:
                layers.append(nn.Linear(hidden_dims[l], 9))
            else:
                layers.append(nn.Linear(hidden_dims[l], hidden_dims[l + 1]))
                layers.append(nn.ReLU())
        self.forward_dynamics_model = nn.Sequential(*layers)
        self.forward_dynamics_model.load_state_dict(torch.load(model_path))
        self.forward_dynamics_model.to("cuda")
        
    def forward(self, state, action):
        # assume state and action are numpy arrays
        state_action = torch.cat((torch.tensor(state, dtype=torch.float), torch.tensor(action)), dim=-1).unsqueeze(0).to("cuda")
        next_state = self.forward_dynamics_model(state_action)
        return next_state.cpu().detach().numpy()[0]