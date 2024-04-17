from fastapi import FastAPI, File
from starlette.background import BackgroundTasks
from fastapi.responses import FileResponse, StreamingResponse
from pytube import YouTube
import os
from io import BytesIO
# # Create an instance of the FastAPI class
app = FastAPI()

# # Define a route and a corresponding function
async def delete_file(file_path: str):
    # Delete the file
    os.remove(file_path)



def delete_file(file_path):
        os.remove(file_path)

@app.get("/")
async def read_root():
    return {"message": "Hello, World"}

@app.get("/{url_key}")
async def download_func(bg_task : BackgroundTasks, url_key :str):
    try:
         
        yt = YouTube(f"https://www.youtube.com/watch?v={url_key}")
        audio_stream = yt.streams.filter(file_extension='mp4')
        video_path = audio_stream.first().download()

        bg_task.add_task(delete_file, video_path)

        return FileResponse(video_path)
    except Exception as e :
         return {"message" : e}


# @app.get("/share")
# async def donaload_func(background_task: BackgroundTasks ):

#         yt = YouTube("https://youtu.be/JAmGzKFdzNU?si=TEBLzVBIhOVGlnLu")

#         audio_stream = yt.streams.filter(file_extension='mp4')

#         video = audio_stream.first().download()

#         # with open(video,"rb") as song_file :
#         #     return_response = song_file.read()
              
#         # os.remove(video)
#         # BackgroundTasks.add_task(delete_file, video)

#         return FileResponse(video,background= BackgroundTasks(os.remove,video))

        # print(video)
    

