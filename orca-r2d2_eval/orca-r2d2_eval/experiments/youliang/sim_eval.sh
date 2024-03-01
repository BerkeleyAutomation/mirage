# This serves as an example of how to run evaluation on a trained model.
# The script is currently configured to run evaluation on a WidowXSimEnv

PATHS=(
    "/mnt2/homer/checkpoints/oxe_vitb"
)

STEPS=(
    "300000"
)

CONDITIONING_MODE=""

TIMESTEPS="150"

TEMPERATURE="1.0"

HORIZON="1"

PRED_HORIZON="1"

EXEC_HORIZON="1"

CMD="python eval/eval_sim.py \
    --num_timesteps $TIMESTEPS \
    $(for i in "${!PATHS[@]}"; do echo "--checkpoint_weights_path ${PATHS[$i]} "; done) \
    $(for i in "${!PATHS[@]}"; do echo "--checkpoint_step ${STEPS[$i]} "; done) \
    --im_size 256 \
    --temperature $TEMPERATURE \
    --horizon $HORIZON \
    --pred_horizon $PRED_HORIZON \
    --modality $CONDITIONING_MODE \
    --exec_horizon $EXEC_HORIZON \
    --show_image
"

echo $CMD

$CMD
