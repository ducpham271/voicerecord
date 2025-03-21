import streamlit as st
from audiorecorder import audiorecorder
import datetime

st.title("Audio Recorder")
audio = audiorecorder("Click to record", "Click to stop recording", custom_style={"backgroundColor": "lightblue"})

if len(audio) > 0:
    # To play audio in frontend:
    st.audio(audio.export().read())

    # To save audio to a file, use pydub export method:
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")  # Format: YYYYMMDD_HHMMSS
    filename = f"audio_{timestamp}.wav"

    audio.export(filename, format="wav")
    print(filename)

    # To get audio properties, use pydub AudioSegment properties:
    st.write(f"Frame rate: {audio.frame_rate}, Frame width: {audio.frame_width}, Duration: {audio.duration_seconds} seconds")