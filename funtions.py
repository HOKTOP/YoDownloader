from pytube import YouTube
from pytube import Playlist
import  sys
import  tkinter as tk
from  tkinter import  filedialog

#function process bar
def progess_fun(stream , chunk , bytes_remaining):
    curr = stream.filesize - bytes_remaining
    done = int(50* curr / stream.filesize)
    sys.stdout.write("\r [{}{}]".format('=' * done, '' * (50-done)) )
    sys.stdout.flush()



def download(file_path, filter=None,resolution=None,url=None):
    if(filter is None):
        listdownload = YouTube(url ,on_progress_callback=progess_fun).streams
        listdownload.get_highest_resolution().download(output_path=file_path)
    else:
        filter.get_by_resolution(resolution).download(output_path=file_path)

def infovideo(url):
    return  f"we start download {YouTube(url).title}"
def playlist():
    urlpalylist = input("enter you list video from youtube")
    palylist = Playlist(urlpalylist)
    urls = palylist.video_urls
    root = tk.Tk()
    root.withdraw()
    file_path = None
    if file_path is None:
        file_path = filedialog.askdirectory()
    for i in urls:
        print(f"\n {infovideo(i)} \n")
        download(file_path=file_path,url=i)
def video():
    url = input("enter url video:")
    arr_resolution = []

    hok = YouTube(url, on_progress_callback=progess_fun)

    print(f"THE Video name : {hok.title}")
    fliter = hok.streams.filter(progressive=True ,file_extension="mp4")
    if(fliter.get_by_resolution("360p")):
        arr_resolution.append("360p")
    if(fliter.get_by_resolution("720p")):
        arr_resolution.append("720p")
    if(fliter.get_by_resolution("1080p")):
        arr_resolution.append("1080p")
    print("you can download this video with this resolution ")
    for i in arr_resolution:
        print(f"enter {arr_resolution.index(i)} for download this resolution  {i}")

    inputres= int(input("what resolution you want download start?"))
    if(arr_resolution[inputres]):
        root = tk.Tk()
        root.withdraw()
        file_path = None
        if file_path is None:
           file_path = filedialog.askdirectory()
           download(file_path=file_path,filter=fliter,resolution=arr_resolution[inputres])

