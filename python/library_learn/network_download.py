#!/usr/bin/env python3

"""https://www.geeksforgeeks.org/downloading-files-web-using-python/"""

import os

geeksforgeeks_download_dir: str = None

def download_files() -> None:
    # imported the request library
    import requests

    image_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"

    # URL of the image to be downloaded is defined as image_url
    r = requests.get(image_url) # create HTTP response object

    # send a HTTP request to the server and save the HTTP response in a response object called r
    file_path = "python_logo.png" if geeksforgeeks_download_dir is None else os.path.join(geeksforgeeks_download_dir, "python_logo.png")

    with open(file_path, "wb") as f:

        # Saving received content as a png file in binary format

        # write the contents of the response (r.content) to a new file in binary mode
        f.write(r.content)

def download_large_files() -> None:
    import requests
    file_url = "https://codex.cs.yale.edu/avi/db-book/db4/side-dir/ch1-2.pdf"

    r = requests.get(file_url, stream=True, verify=False)
    
    file_path = "python.pdf" if geeksforgeeks_download_dir is None else os.path.join(geeksforgeeks_download_dir, "python.pdf")

    with open(file_path, "wb") as pdf:
        for chunk in r.iter_content(chunk_size=1024):
        
            # writting one chunk at a time to pdf file
            if chunk:
                pdf.write(chunk)

def download_vides() -> None:
    import requests
    from bs4 import BeautifulSoap

    '''
    URL of the archive web-page which provides link to  
    all video lectures. It would have been tiring to  
    download each video manually.  
    In this example, we first crawl the webpage to extract  
    all the links and then download videos.  
    '''

    # specify the URL of the archive here
    archive_url = "http://www-personal.umich.edu/~csev/books/py4inf/media/"

    def get_video_links() -> List[str]:

        # create response object
        r = requests.get(archive_url)

        # create beautiful-soup object
        soup = BeautifulSoup(r.content, 'html5lib')

        # find all links on web-page
        links = soup.findAll('a')

        # filter the link sending with .mp4
        video_links = [archive_url + link['href'] for link in links if link['href'].endswith('mp4')]

        return video_links

    def download_video_series(video_links: str):

        for link in video_links:

            '''iterate through all links in video_links
            and download them one by one'''

            # obtain filename by splitting url and getting last string
            file_name = link.split('/')[-1]
            if not (geeksforgeeks_download_dir is None):
                file_name = os.path.join(geeksforgeeks_download_dir, file_name)

            print("Downloading file:%s" % file_name)

            # create response object
            r = requests.get(link, stream=True)

            # download started
            with open(file_name, 'wb') as f:
                for chunk in r.iter_content(chunk_size = 1024 * 1024):
                    if chunk:
                        f.write(chunk)

            print("%s downloaded!\n" % file_name)

        print("All videos downloaded!")
        return

    # getting all video links
    video_links = get_video_links()

    # download all videos
    download_video_series(video_links)


if __name__ == "__main__":
    geeksforgeeks_download_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    download_files()
    #download_large_files()
    #download_videos()


