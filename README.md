# Introduction

This script is used to download TikTok videos by account name (i.e. download all videos of a specific account) or individually by video id's.



# Requirements

* Cookie data: `s_v_web_id` and `tt_webid`
* Python 3



# Installation

Install requirements:

```shell
$ git clone https://github.com/norus/tiktok-downloader.git && cd tiktok-downloader
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Test that script can be run:

```shell
$ python3 downloader.py
usage: downloader.py [-h] [--config CONFIG] [--input INPUT] [--outdir OUTDIR]
                     [--mode MODE]

Script to download TikTok videos

optional arguments:
  -h, --help       show this help message and exit
  --config CONFIG  Path to config with cookie data
  --input INPUT    Path to file with TikTok account names or individual video
                   IDs
  --outdir OUTDIR  Path to output directory
  --mode MODE      Put 1 to download all videos of an account. Put 0 to
                   download a single video by ID
```

Before proceeding further, please read further instructions under *Usage* below.



# Usage

### Get cookie data

Before running the script, open tiktok.com in your browser, log in with your account and grab values for `s_v_web_id` and `tt_webid`

![Screen Shot 2021-02-09 at 9.00.20 AM](https://i.loli.net/2021/02/09/jPahTVeruFm9fYU.png)

Open `cookie.yml` in a text editor and put the values accordingly:

```shell
s_v_web_id: <INSERT VALUE>
tt_webid: <INSERT VALUE>
```



### Download individual videos

To download individual videos, open `video_ids.txt` in a text editor and put video IDs, one per line.

Example:

```shell
6926846576233041157
6919876827578109190
```

Create a folder where your videos will be stored.

Example:

```shell
$ mkdir output
```

Start the download by specifying `mode=0` which is for individual video downloads:

```shell
$ python3 downloader.py --config cookie.yml --input video_ids.txt --outdir output/ --mode 0
2021-02-09 08:52:05.067 INFO downloader: Downloading video: 6926846576233041157
2021-02-09 08:52:11.776 INFO downloader: Downloading video: 6919876827578109190
```

You can now find the videos in your `output` folder:

```shell
$ ls -l output/
total 7904
-rw-r--r--  1 norus  staff  1326874 Feb  9 08:52 6919876827578109190.mp4
-rw-r--r--  1 norus  staff  2717187 Feb  9 08:52 6926846576233041157.mp4
```



### Download all videos of a specific account

To download all videos of a specific TikTok account, open `accounts.txt` in a text editor and put account names, one per line.

Example:

```shell
0x41414141
```

Create a folder where your videos will be stored.

Example:

```shel
$ mkdir output
```

Start the download by specifying `mode=1` which is for downloading all videos of specific accounts:

```shell
$ python3 downloader.py --config cookie.yml --input accounts.txt --outdir output/ --mode 1
2021-02-09 08:52:26.588 INFO downloader: Downloading all videos of account: 0x41414141
2021-02-09 08:52:30.772 INFO downloader: Downloading video: Microchip implant = my hand is a key 👋 #cybersecurity #whitehat #hacker #fyp
2021-02-09 08:52:36.590 INFO downloader: Downloading video: Opening locks with a microchip implant #cyborg #future #tech #cybersecurity
2021-02-09 08:52:39.252 INFO downloader: Downloading video: What it’s like to get a microchip implant... aka becoming a cyborg. #future #technology #cybersecurity #hacker #fyp
2021-02-09 08:52:41.786 INFO downloader: Downloading video: Microchip implant = success. I envision a future where you can wave your hand to share info, open doors, & pay for things. #tech #implant #fyp #hacker
2021-02-09 08:52:43.790 INFO downloader: Downloading video: Hackers can easily take over your computer and spy on your webcam in a matter of seconds using only a USB drive. #whitehat #hacker #cybersecurity #fyp
'itemInfo'
2021-02-09 08:52:45.238 WARNING downloader: Could not download video: Hackers can easily take over your computer and spy on your webcam in a matter of seconds using only a USB drive. #whitehat #hacker #cybersecurity #fyp
2021-02-09 08:52:45.239 INFO downloader: Downloading video: Literal life hack: Think twice before plugging it in 😏 Hackers can take over your computer with a USB cable. #whitehat #hacker #cybersecurity #fyp
2021-02-09 08:52:48.300 INFO downloader: Downloading video: Using a proxmark3 to clone a RFID key in < 15 seconds. Its terrifying how many hotels still use this broken tech #cybersecurity #whitehat #hacker #fyp
2021-02-09 08:52:50.077 INFO downloader: Downloading video: My first TikTok! 🤓 A friendly reminder to never plug an unknown USB cable or drive into your computer. #cybersecurity #whitehat #hacker #technology
```

You can now find the videos in your `output` folder:

```shell
$ ls -l output/
total 33352
-rw-r--r--  1 norus  staff  1947404 Feb  9 08:52 6851787844927704325.mp4
-rw-r--r--  1 norus  staff  1894624 Feb  9 08:52 6855464516893838597.mp4
-rw-r--r--  1 norus  staff  2134902 Feb  9 08:52 6856139981035998469.mp4
-rw-r--r--  1 norus  staff  2341063 Feb  9 08:52 6868454371588443397.mp4
-rw-r--r--  1 norus  staff   896177 Feb  9 08:52 6870947408696691973.mp4
-rw-r--r--  1 norus  staff  1608427 Feb  9 08:52 6873609428931824902.mp4
-rw-r--r--  1 norus  staff  2193136 Feb  9 08:52 6883605799264963845.mp4
```

