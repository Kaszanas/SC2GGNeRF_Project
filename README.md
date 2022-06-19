# StarCraft 2 Game-engine Generated Neural Radiance Fields (SC2GGNeRF)

This repository contains a project that is under active research and development. Out goal was to generate data to train and benchmark NeRF models on previously unseen task.

## Dependencies

Our Proposed benchmark uses a fork of the original repository: [yashbhalgat/HashNeRF-pytorch](https://github.com/yashbhalgat/HashNeRF-pytorch)

## Reproduction instructions

### Recording Views

If you do not have pre-recorded unit views that are used to train the model. Please make sure to record them by using the ```src/recorder/main_recorder.py```

### Cropping Video

Videos recorded in the previous step contain UI elements which might lead to bad solve of the feature matching step which is required for instant-ngp using COLMAP.

Automatically cropping the videos that were produced in the Recording Views step can be done by using the ```src/pre_processor/main_pre_processor.py```

Preview of the command that was used to crop the videos:
```
ffplay -vf "crop=1050:800:out_w/2-186:0" -i .\BroodLord_video.mkv
```

Command that was used to crop the videos:
```
ffmpeg -i .\BroodLord_video.mkv -vf "crop=1050:800:out_w/2-186:0" BroodLord_video_cropped.mkv
```