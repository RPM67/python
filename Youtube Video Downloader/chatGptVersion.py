import os
import urllib
from pytube import YouTube, Playlist
from tqdm import tqdm  # tqdm is a library for displaying progress bars

# Install tqdm if you haven't already
# pip install tqdm

def video_downloader():
    def yt_video_download(yt_video, totalVideoFormatsAvailable):
        while True:
            try:
                stream = input("\nEnter the format number from above to download ('q' to exit): ")
                if stream.lower() == 'q':
                    exit("program exit successfully")
                if not stream.isdigit():
                    raise ValueError
                if int(stream) < 1 or int(stream) > totalVideoFormatsAvailable:
                    raise IndexError

                chosen_stream = yt_video.streams.filter(progressive=True)[int(stream) - 1]

                print(f"Downloading video {yt_video.title}. Please wait...")
                # Use tqdm for a progress bar during download
                with tqdm(total=chosen_stream.filesize, unit='B', unit_scale=True, desc=f'Downloading {yt_video.title}') as progress_bar:
                    def progress_callback(chunk, file_handle, bytes_remaining):
                        progress_bar.update(chunk)

                    chosen_stream.download(output_path='.', filename=yt_video.title, on_progress_callback=progress_callback)

                print(f'Your video - {yt_video.title} has been downloaded successfully')
                print("Thank You for using our services.\nPlease Come Again")
                break

            except ValueError:
                print("Please enter a valid video format number from above")
            except IndexError:
                print("Please enter the video format number from above available options")
            except KeyboardInterrupt:
                exit("\nProgram exit successfully")
            except urllib.error.URLError:
                print("Please Check your Internet Connection and try again.")
            except Exception as e:
                print(f"Some error occurred as {e}. Please Try Again")

    # ... (rest of the functions)

#if __name__ == "__main__":
    # ... (rest of the main script)
