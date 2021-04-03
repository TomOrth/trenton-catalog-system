import pandas as pd
import sys

# CHANGE THESE VALUES DEPENDING ON THE TRANSCRIPT

name = "Joel Millner"

summary = "Joel Millner is interviewed about the life of his father, Nathan. He talked about his livlihood, selling things like hotdogs and candy. His father lived in union street. He also owned a hardware store for a time on South Broad street. He had many family members."

audio_path = "joel.mp3"

text_path = "joel.pdf"

title = "Joel Millner Interview Transcription"

content = ""

with open(sys.argv[1]) as f:
    content = ''.join(f.readlines())

x = pd.DataFrame(columns=['title', 'text_file_path', 'audio_file_path', 'summary', 'text_content'], data=[[title, text_path, audio_path, summary, content.replace('"', '')]])
x.to_csv("insert_data_transcript.csv", sep="|", index=False)

participants = [[name]]

p = pd.DataFrame(columns=['name'], data=participants)
p.to_csv("insert_data_participants.csv", sep="|", index=False)

locations = [["Union Street"], ["South Broad Street"]]
l = pd.DataFrame(columns=['street_name'], data=locations)
l.to_csv("insert_data_locations.csv", sep="|", index=False)

keywords = [["millner"], ["indistinguishable"]]
k = pd.DataFrame(columns=['word'], data=keywords)
k.to_csv('insert_data_keywords.csv', sep="|", index=False)



