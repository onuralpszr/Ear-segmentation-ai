MODELNAME = "earsegmentation_model_v1_46.pth"
REPOURL = "https://github.com/umitkacar/Ear-segmentation-ai"
MODELURL = f"{REPOURL}/releases/download/v1.0.0/{MODELNAME}"
MODEL_PATH = f"./earsegmentationai/model_ear/{MODELNAME}"
ENCODER = "resnet18"
ENCODER_WEIGHTS = "imagenet"
CLASSES = ["ear"]
ACTIVATION = "sigmoid"
