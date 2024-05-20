import streamlit as st
from main import visual_story_telling

def main():
    st.title("Visual Storytelling")
    st.write("Upload a video and a photo to generate a story.")

    video_file = st.file_uploader("Upload Video", type=["mp4", "avi", "mov"])
    photo_file = st.file_uploader("Upload Photo", type=["jpg", "jpeg", "png"])

    if video_file is not None and photo_file is not None:
        video_path = f"temp_video.{video_file.type.split('/')[1]}"
        photo_path = f"temp_photo.{photo_file.type.split('/')[1]}"
        
        # Save the uploaded files to the temp directory
        with open(video_path, "wb") as f:
            f.write(video_file.getbuffer())
        
        with open(photo_path, "wb") as f:
            f.write(photo_file.getbuffer())

        # Generate story
        story = visual_story_telling(video_path, photo_path)
        
        # Display the story
        st.header("Generated Story")
        st.write(story)

if __name__ == "__main__":
    main()
