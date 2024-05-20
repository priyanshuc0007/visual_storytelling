import os
from utils.frame_extractor import extract_key_frames
from utils.caption_generator import generate_caption
from utils.story_generator import generate_story

def visual_story_telling(video_path, photo_path):
    # Step 1: Extract key frames
    output_dir = 'output/frames'
    os.makedirs(output_dir, exist_ok=True)
    extract_key_frames(video_path, output_dir)
    
    # Step 2: Generate captions for frames and photo
    captions = [generate_caption(photo_path)]
    for frame in sorted(os.listdir(output_dir)):
        frame_path = os.path.join(output_dir, frame)
        captions.append(generate_caption(frame_path))
    
    # Step 3: Generate story from captions
    story = generate_story(captions)
    return story
