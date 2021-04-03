# File that prepares the transcripts into CSV for insertion into the database
# Created by Thomas Orth

import pandas as pd
import sys

# CHANGE THESE VALUES DEPENDING ON THE TRANSCRIPT

name = "Joel Millner"

summary = "Joel Millner is interviewed about the life of his father, Nathan. He talked about his livlihood, selling things like hotdogs and candy. His father lived in union street. He also owned a hardware store for a time on South Broad street. He had many family members."

audio_path = "joel.mp3"

text_path = "joel.pdf"

title = "Joel Millner Interview Transcription"

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
locations = [["Union Street"], ["South Broad Street"]]
l = pd.DataFrame(columns=['street_name'], data=locations)
l.to_csv("insert_data_locations.csv", sep="|", index=False)

# Prepare the keywords CSV
keywords = [["millner"], ["indistinguishable"]]
k = pd.DataFrame(columns=['word'], data=keywords)
k.to_csv('insert_data_keywords.csv', sep="|", index=False)



