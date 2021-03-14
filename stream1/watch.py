
import time,vlc

player = vlc.MediaPlayer('rtsp://localhost:8554/livestream')
player.play()

i = 0
while True:
	time.sleep(1/24) # 24fps #
	try:
		player.video_take_snapshot(0, './result/snapshot-%03d.png' % i, 0, 0)
	except Exception:
		break
	i = i+1
