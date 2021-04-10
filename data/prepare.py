# File that prepares the transcripts into CSV for insertion into the database
# Created by Thomas Orth

import pandas as pd
import sys

# CHANGE THESE VALUES DEPENDING ON THE TRANSCRIPT

name = "Charles Terry"

summary = "Charles Terry is interviewed about his life in old trenton and other aspects such as working for the Board of Education."

audio_path = "https://archive.org/download/CharlesTerryInterview415115/Charles%20Terry%20Interview%204%EF%80%A215%EF%80%A215.MP3"

text_path = "charles.pdf"

title = "Charles Terry Interview Transcription"

content = ""

# Read raw transcript data
with open(sys.argv[1]) as f:
    content = ''.join(f.readlines())

# Prepare the transcript csv
x = pd.DataFrame(columns=['title', 'text_file_path', 'audio_file_path', 'summary', 'text_content'], data=[[title, text_path, audio_path, summary, content.replace('"', '')]])
x.to_csv("insert_data_transcript.csv", sep="|", index=False)


# Prepare the participants csv
participants = [[name]]

p = pd.DataFrame(columns=['name'], data=participants)
p.to_csv("insert_data_participants.csv", sep="|", index=False)

# Prepare the locations CSV
locations = [["Mercer Street"]]
l = pd.DataFrame(columns=['street_name'], data=locations)
l.to_csv("insert_data_locations.csv", sep="|", index=False)

# Prepare the keywords CSV
keywords = [["charles"], ["neighborhood"]]
k = pd.DataFrame(columns=['keyword'], data=keywords)
k.to_csv('insert_data_keywords.csv', sep="|", index=False)



