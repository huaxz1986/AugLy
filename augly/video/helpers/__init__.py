#!/usr/bin/env python3
# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from augly.video.helpers.ffmpeg import (
    add_silent_audio,
    combine_frames_and_audio_to_file,
    extract_audio_to_file,
    extract_frames_to_dir,
    get_audio_info,
    get_video_fps,
    get_video_info,
    has_audio_stream,
)
from augly.video.helpers.intensity import (
    add_noise_intensity,
    apply_lambda_intensity,
    audio_swap_intensity,
    augment_audio_intensity,
    blend_videos_intensity,
    blur_intensity,
    brightness_intensity,
    change_aspect_ratio_intensity,
    change_video_speed_intensity,
    color_jitter_intensity,
    concat_intensity,
    contrast_intensity,
    crop_intensity,
    encoding_quality_intensity,
    fps_intensity,
    grayscale_intensity,
    hflip_intensity,
    hstack_intensity,
    insert_in_background_intensity,
    insert_in_background_multiple_intensity,
    loop_intensity,
    meme_format_intensity,
    overlay_dots_intensity,
    overlay_emoji_intensity,
    overlay_intensity,
    overlay_onto_background_video_intensity,
    overlay_onto_screenshot_intensity,
    overlay_shapes_intensity,
    overlay_text_intensity,
    pad_intensity,
    perspective_transform_and_shake_intensity,
    pixelization_intensity,
    remove_audio_intensity,
    replace_with_background_intensity,
    replace_with_color_frames_intensity,
    rotate_intensity,
    scale_intensity,
    shift_intensity,
    time_crop_intensity,
    time_decimate_intensity,
    trim_intensity,
    vflip_intensity,
    vstack_intensity,
)
from augly.video.helpers.metadata import (
    compute_changed_segments,
    compute_segments,
    compute_time_crop_segments,
    compute_time_decimate_segments,
    get_func_kwargs,
    get_metadata,
)
from augly.video.helpers.utils import (
    create_color_video,
    create_video_from_image,
    get_local_path,
    identity_function,
    validate_input_and_output_paths,
)


__all__ = [
    # -- ffmpeg --
    "add_silent_audio",
    "combine_frames_and_audio_to_file",
    "extract_audio_to_file",
    "extract_frames_to_dir",
    "get_audio_info",
    "get_video_fps",
    "get_video_info",
    "has_audio_stream",
    # -- intensity --
    "add_noise_intensity",
    "apply_lambda_intensity",
    "audio_swap_intensity",
    "augment_audio_intensity",
    "blend_videos_intensity",
    "blur_intensity",
    "brightness_intensity",
    "change_aspect_ratio_intensity",
    "change_video_speed_intensity",
    "color_jitter_intensity",
    "concat_intensity",
    "contrast_intensity",
    "crop_intensity",
    "encoding_quality_intensity",
    "fps_intensity",
    "grayscale_intensity",
    "hflip_intensity",
    "hstack_intensity",
    "insert_in_background_intensity",
    "insert_in_background_multiple_intensity",
    "loop_intensity",
    "meme_format_intensity",
    "overlay_intensity",
    "overlay_dots_intensity",
    "overlay_emoji_intensity",
    "overlay_onto_background_video_intensity",
    "overlay_onto_screenshot_intensity",
    "overlay_shapes_intensity",
    "overlay_text_intensity",
    "pad_intensity",
    "perspective_transform_and_shake_intensity",
    "pixelization_intensity",
    "remove_audio_intensity",
    "replace_with_background_intensity",
    "replace_with_color_frames_intensity",
    "rotate_intensity",
    "scale_intensity",
    "shift_intensity",
    "time_crop_intensity",
    "time_decimate_intensity",
    "trim_intensity",
    "vflip_intensity",
    "vstack_intensity",
    # -- metadata --
    "compute_changed_segments",
    "compute_segments",
    "compute_time_crop_segments",
    "compute_time_decimate_segments",
    "get_func_kwargs",
    "get_metadata",
    # -- utils --
    "create_color_video",
    "create_video_from_image",
    "get_local_path",
    "identity_function",
    "validate_input_and_output_paths",
]
