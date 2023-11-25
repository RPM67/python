import os
import urllib # this library is used here to give specific error to user when user is not connected to Internet
import pytube
from pytube import YouTube
from pytube import Playlist


# LINK TO TEST SINGLE YOUTUBE VIDEO DOWNLOADER - https://youtu.be/OKuiyX5k6zg?feature=shared

#   SINGLE YOUTUBE VIDEO DOWNLOAD PROGRAM
def video_downloader():


    def user_url_input():
        while True:
            try:
                link = input("Enter the youtube video link here : ")
                yt_video = YouTube(link)  # it will store the actual YouTube video and all its features from the link into this 'yt_video' variable

                print(f"VIDEO TITLE - {yt_video.title}")
                print(f"visit this link to download the get thumbnail of video - {yt_video.thumbnail_url}")
                return yt_video
            except pytube.exceptions.RegexMatchError:
                print("Enter a valid YouTube video link")
            except KeyboardInterrupt:
                exit("\nprogram exit successfully")
            except urllib.error.URLError:
                print("Please Check your Internet Connection and try again.")
            except Exception as e:
                print(f"Some error occurred as {e}, please try again")



    def display_video_formats(yt_video):
        print("\navailable video formats :- \n")
        availableVideoFormats = yt_video.streams.filter(progressive=True)  # it will store all the video quality streams into this 'videos' variable
        for i, j in enumerate(availableVideoFormats,start=1):
            print(f"{i} -  Resolution - {j.resolution}  fps - {j.fps}   Format - {j.mime_type}")
        return len(availableVideoFormats)



    def yt_video_download(yt_video, totalVideoFormatsAvailable):
        while True:
            try:
                stream = input("\nEnter the format number from above to download ('q' to exit): ")
                if stream == 'q':
                    exit("program exit successfully")
                if not int(stream):
                    raise ValueError
                if int(stream) < 1 or int(stream) > totalVideoFormatsAvailable:
                    raise IndexError
                print(f"downloading video{yt_video.title}. please wait..............")
                yt_video.streams.filter(progressive=True)[int(stream) - 1].download() # it will download the yt_video with the specified format
                print(f"your video - {yt_video.title} has been Download successfully")
                break
            except ValueError:
                print("Please enter a valid video format number from above")
            except IndexError:
                print("Please enter the video format number from above available options")
            except KeyboardInterrupt:
                exit("\nprogram exit successfully")
            except urllib.error.URLError:
                print("Please Check your Internet Connection and try again.")
            except Exception as e:
                print(f"Some error occurred as {e}. Please Try Again")

    yt_video = user_url_input()
    totalVideoFormatsAvailable = display_video_formats(yt_video)
    yt_video_download(yt_video,totalVideoFormatsAvailable)






# LINK TO TEST YOUTUBE PLAYLIST DOWNLOADER - https://youtube.com/playlist?list=PLu0W_9lII9agqZuv_XJen_BEHycIh-FmG&feature=shared

#   YOUTUBE PLAYLIST DOWNLOADER PROGRAM
def playList_downloader():


    def user_url_input():
        while True:
            try:
                url = input("Enter the URL of the playlist ('q' to exit): ")
                if url.lower() == 'q':
                    exit("Program Exit Successfully")
                playlst = Playlist(url)  # the 'playlst' variable will store the actual Playlist here
                print(f"PLAYLIST TITLE - {playlst.title}")
                print(f"Total Videos in Playlist - {len(playlst.videos)}")
                return playlst
            except KeyError:
                print("Either you are not connected to Internet or you have provided a wrong Youtube Playlist Link. Please Try Again")
            except urllib.error.URLError:
                print("Please Check your Internet Connection and try again.")
            except KeyboardInterrupt:
                exit("Program Exit Successfully")
            except Exception as e:
                print(f"Some error occurred as {e}. Please Try Again")


    def display_playlist_video_format():
        playlst = user_url_input()
        try:
            print("Available Video Formats of Playlist :- ")
            first_video_stream = playlst.videos[0].streams.filter(progressive=True)
            for i,stream in enumerate(first_video_stream,start=1):
                print(f"{i} - Resolution - {stream.resolution}   fps - {stream.fps}   Format - {stream.mime_type}") # we will show the video format of first video only and user will select the resolution to download of first video and rest other videos of playlist will be downloaded in same resolution.
            return len(first_video_stream)
        except KeyboardInterrupt:
            exit("Program Exit Successfully")
        except urllib.error.URLError:
            print("Please Check your Internet Connection and try again.")
            user_url_input()
        except Exception as e:
            print(f"Some error occurred as {e}. Please Try Again")
            user_url_input()


    def playList_videos_download(playlst,totalVideoFormatsAvailable):
        while True:
            try:
                res = input("\nchoose the resolution in which you wanna download playlist ('q' to exit) : ")
                if res.lower() == 'q':
                    exit("Program Exit Successfully")
                if not int(res):
                    raise ValueError
                if int(res) < 1 or int(res) > totalVideoFormatsAvailable:
                    raise IndexError
                for i, video in enumerate(playlst.videos, start=1):
                    print(f"Downloading video {i} - {video.title}...........")
                    video.streams.filter(progressive=True)[int(res) - 1].download()
                    print("Downloaded Successfully")
                    os.system('cls')
                print(f"\nYour Playlist - {playlst.title} has been downloaded successfully.")
            except ValueError:
                print("please enter a valid video format number from above")
            except IndexError:
                print("Please enter video format number only from above options")
            except KeyboardInterrupt:
                exit("Program Exit Successfully")
            except urllib.error.URLError:
                print("Please Check your Internet Connection and try again.")
            except Exception as e:
                print(f"Some error occurred as {e}. Please Try Again")

    playlst = user_url_input()
    totalVideoFormatsAvailable = display_playlist_video_format()
    playList_videos_download(playlst, totalVideoFormatsAvailable)


if __name__ == "__main__":

    print("Welcome to YouTube Video Downloader by RPM\n")
    print("note : the videos will be saved at the destination where this program is running. so please save this program in the folder where you wanna save the videos and run from there.\n")
    print("1 - SINGLE YOUTUBE VIDEO DOWNLOAD")
    print("2 - YOUTUBE PLAYLIST DOWNLOAD\n")
    while True:
        try:
            choose = input("choose an option from above options ('q' to exit): ")
            print()
            if choose == 'q':
                exit("Program Exit Successfully")

            if not int(choose):
                raise ValueError

            if int(choose) == 1:
                video_downloader()
                exit("Thank You for using our services.\nPlease Come Again")
            if int(choose) == 2:
                playList_downloader()
                exit("Thank You for using our services.\nPlease Come Again")

        except ValueError:
            print("Please enter a valid option from above")
        except IndexError:
            print("Please enter an option from above available options only")
        except KeyboardInterrupt:
            exit("Program Exit Successfully")
        except Exception as e:
            print(f"Some error occurred as {e}. Please Try Again")
