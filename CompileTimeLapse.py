import cv2 as cv #OpenCV
import numpy as np
import os #allows us to interact with the operating system

def get_movie(date_folder, output_file, fps):
    """
    :param date_folder: str, the date folder
    :param output_file: str, file name of mp4, should end with '.mp4'
    :param fps: int, num frames per second
    :post: compiles jpg images in date_folder into mp4 file then saved to output_file
    """
    #dir = "D:/2026-10-14"
    pic_files = sorted(os.listdir(date_folder)) #list of all file names in path folder
    already_contains_timelapse = False

    for filename in pic_files:
        try:
            indx = filename.index('.mp4')
            already_contains_timelapse = True
        except ValueError:
            already_contains_timelapse = False
    '''
    dir:                         "D:/2026-10-14"
    filename:                    "skysphere_2026-10-14T18-10-34.jpg"
    os.path.join(dir, filename): "D:/2026-10-14/skysphere_2026-10-14T18-10-34.jpg"
    '''

    if not already_contains_timelapse:
    # read first image to get the dimensions
        first = cv.imread(os.path.join(date_folder, pic_files[0]))
        height, width, _ = first.shape

    # We need a VideoWriter object to build the mp4 frame by frame
        fourcc = cv.VideoWriter_fourcc(*'mp4v') #supposed to set video file type but currently giving warning
        video = cv.VideoWriter(output_file, fourcc, fps, (width, height))

        for filename in sorted(pic_files):
            full_path = os.path.join(date_folder, filename)
            frame = cv.imread(full_path)
            video.write(frame)

        video.release()
        cv.destroyAllWindows()
    else:
        print("This date already has a corresponding timelapse")


input_folder = 'D:/2026-10-14'
output_folder = 'D:/2026-10-14/2026-10-14.mp4'
frames_per_second = 24

get_movie(input_folder, output_folder, frames_per_second)

