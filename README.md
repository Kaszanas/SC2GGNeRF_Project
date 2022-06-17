# StarCraft 2 Game-engine Generated Neural Radiance Fields (SC2GGNeRF)

This repository contains a project that is under active research and development. Out goal was to generate data to train and benchmark NeRF models on previously unseen task.

## Dependencies

Our Proposed benchmark uses a fork of the original repository: [yashbhalgat/HashNeRF-pytorch](https://github.com/yashbhalgat/HashNeRF-pytorch)

## Reproduction instructions

If you do not have pre-recorded unit views that are used to train the model. Please make sure to record them by using the ```src/recorder```

Preview of the command that was used to crop the videos:

```
ffplay -vf "crop=1050:800:out_w/2-186:0" -i .\BroodLord_video.mkv
```

Command that was used to crop the videos:
```
ffmpeg -i .\BroodLord_video.mkv -vf "crop=1050:800:out_w/2-186:0" BroodLord_video_cropped.mkv
```