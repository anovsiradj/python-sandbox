
# Instalasi

```sh
source ./venv/bin/activate
pip3 install python-vlc
```

download <https://github.com/aler9/rtsp-simple-server>
lalu extract ke `cwd`.

```sh
tar -zxvf ./rtsp-simple-server_v0.15.0_linux_amd64.tar.gz
```

# Eksekusi

setiap perintah dijalankan pada tab berbeda di terminal.

```sh
./rtsp-simple-server

# versi 1
ffmpeg -f v4l2 -i /dev/video0 -f rtsp rtsp://localhost:8554/livestream
# versi 2
ffmpeg -re -stream_loop -1 -i /dev/video0 -f rtsp -rtsp_transport tcp rtsp://localhost:8554/livestream

# entah kenapa, setelah sekian lama, selalu gagal.
python3 ./watch.py
# padahal kalo pake ini, bisa:
ffplay -rtsp_transport tcp rtsp://localhost:8554/livestream
```
