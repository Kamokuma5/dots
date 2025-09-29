#!/bin/bash

# Dependencies: wf-recorder, slurp, ffmpeg, pgrep

PID_FILE="/tmp/wf-recording.pid"
TMP_MP4="/tmp/region_record.mp4"
OUT_GIF="$HOME/Videos/region_record_$(date +%Y%m%d_%H%M%S).gif"

if [ -f "$PID_FILE" ]; then
    # Stop recording
    PID=$(cat "$PID_FILE")
    kill "$PID"
    rm "$PID_FILE"

    # Convert to GIF
    echo "Converting to GIF..."
    ffmpeg -i "$TMP_MP4" -vf "fps=10,scale=640:-1:flags=lanczos" "$OUT_GIF"
    rm "$TMP_MP4"
    notify-send "Recording stopped. GIF saved to $OUT_GIF"
else
    # Start recording
    REGION=$(slurp)
    wf-recorder -g "$REGION" -f "$TMP_MP4" &
    echo $! > "$PID_FILE"
    notify-send "Recording started"
fi