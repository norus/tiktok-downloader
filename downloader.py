#!/usr/bin/env python
import argparse
import sys
import yaml
import logging
from TikTokAPI import TikTokAPI

# Disable logging for `pyppeteer` unless WARNING
pyppeteer_logger = logging.getLogger('pyppeteer')
pyppeteer_logger.setLevel(logging.WARNING)


# Default logger
logger = logging.getLogger()
if logger.handlers:
    for handler in logger.handlers:
        logger.removeHandler(handler)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')


class TikTok:
    def __init__(self, config='cookie.yml'):
        cfg = yaml.load(open(config, 'r'), Loader=yaml.FullLoader)
        self.cfg = cfg

        # Load cookie values from the config
        cookie = {
            's_v_web_id': cfg['s_v_web_id'],
            'tt_webid': cfg['tt_webid']
        }

        self.api = TikTokAPI(cookie=cookie)


    def get_all_videos_username(self, username):
        user_videos = self.api.getVideosByUserName(username)

        if user_videos:
            return user_videos

        return None


    def download_video(self, video_id, download_path):
        download = self.api.downloadVideoById(
            video_id,
            '{}/{}.mp4'.format(download_path, video_id))

        return download


# Main code starts below

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script to download TikTok videos')
    parser.add_argument('--config', help='Path to config with cookie data')
    parser.add_argument('--input', help='Path to file with TikTok account names or individual video IDs')
    parser.add_argument('--outdir', help='Path to output directory')
    parser.add_argument('--mode', type=int, help='Put 1 to download all videos of an account. Put 0 to download a single video by ID')

    args = parser.parse_args()

    if not args.config:
        parser.print_help()
    else:
        tt = TikTok()

        # Mode 0 selected (download all videos by id)
        if args.mode == 0:
            with open(args.input) as videos_file:
                videos = videos_file.read().splitlines()

            # Loop through all video IDs
            for video in videos:
                logger.info('Downloading video: {}'.format(video))
                try:
                    tt.download_video(video, args.outdir)
                except Exception as e:
                    print(e)
                    logger.warning('Could not download video: {}'.format(video))
                
        # Mode 1 selected (download all videos of specific user/s)
        if args.mode == 1:
            with open(args.input) as accounts_file:
                accounts = accounts_file.read().splitlines()

            # Loop through all accounts
            for account in accounts:
                logger.info('Downloading all videos of account: {}'.format(account))
                account_videos = tt.get_all_videos_username(account)

                if account_videos['statusCode'] == 0:
                    for video in account_videos['items']:
                        logger.info('Downloading video: {}'.format(video['desc']))
                        try:
                            tt.download_video(video['id'], args.outdir)
                        except Exception as e:
                            print(e)
                            logger.warning('Could not download video: {}'.format(video['desc']))
                else:
                    logger.warning('Could not access account: {}'.format(account))
