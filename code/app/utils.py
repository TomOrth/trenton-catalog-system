
"""
General Utilities that could be used throughout the project, independent of folders

By: Tom Orth
"""
def convert_full_transcripts_to_json(transcripts):
    """
    Convert FullTranscript objects to a list of dictionarys of relevant info
    """
    maps = {}
    for transcript in transcripts:
        # If we already started using a transcript, update the map
        if transcript.transcript_id in maps:
            res = maps[transcript.transcript_id]
            res["locations"].add(transcript.street_name)
            res["participants"].add(transcript.name)
            res["keywords"].add(transcript.keyword)
            maps[transcript.transcript_id] = res
        # Otherwise, setup the dictionary for the transcript
        else:
            res = {}
            res["transcript_id"] = transcript.transcript_id
            res["title"] = transcript.title
            res["summary"] = transcript.summary
            res["locations"] = set([transcript.street_name])
            res["participants"] = set([transcript.name])
            res["keywords"] = set([transcript.keyword])
            maps[transcript.transcript_id] = res
    
    # Build the list
    res_list = []
    for key in maps.keys():
        maps[key]["locations"] = ", ".join(maps[key]["locations"])
        maps[key]["participants"] = ", ".join(maps[key]["participants"])
        maps[key]["keywords"] = ", ".join(maps[key]["keywords"])
        res_list.append(maps[key])
    
    return res_list

def check_if_parsed_transcripts_are_bookmarked(user_id, transcripts, conn):
    """
    Take a list of transcript dictionaries and add their bookmarked status to it
    """
    for index, transcript in enumerate(transcripts):
        _, count = conn.execute_and_return(f"SELECT COUNT(transcript_id) FROM user_transcript_view WHERE user_id={user_id} AND transcript_id={transcript['transcript_id']}")
        transcript["bookmarked"] = count[0][0] > 0
        transcripts[index] = transcript
    return transcripts

     