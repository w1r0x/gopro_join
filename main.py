from os import listdir
from os.path import isfile, join

gopro_dir = '/home/w1r0x/Desktop/gopro_2021-09-20'
ffmpeg_resize = 'ffmpeg -i {0} -vf "hflip,vflip,scale=1920:1080" -metadata:s:v rotate=0 -codec:v libx265 -codec:a copy rotated/{0}'


def split_videos(video_list):
    videos = []
    ids = get_video_ids(video_list)
    for id in ids:
        video = []
        for i in range(1, 9):
            for video_name in video_list:
                if f'{i}{id}' in video_name:
                    video.append(video_name)
        videos.append(video)
    return(videos)


def get_video_ids(video_list):
    ids = []
    for filename in video_list:
        id = filename[4:-4]
        if id not in ids:
          ids.append(id)
    return sorted(ids)


if __name__ == '__main__':
    gopro_files = [f for f in listdir(gopro_dir) if isfile(join(gopro_dir, f))]

    videos = split_videos(gopro_files)
    print('!#/bin/bash')
    for video in videos:
        for v in video:
            print(ffmpeg_resize.format(v))
