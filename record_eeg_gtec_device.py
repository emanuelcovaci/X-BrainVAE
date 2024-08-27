import time
from datetime import datetime
import os
import pandas as pd
from pylsl import StreamInlet, resolve_stream
from PIL import Image, ImageTk
import tkinter as tk
import threading


def record_data(inlet, duration=2):
    print("Start recording")
    columns = ['Time', 'FZ', 'C3', 'CZ', 'C4', 'PZ', 'PO7', 'OZ', 'PO8', 'AccX', 'AccY', 'AccZ',
               'Gyro1', 'Gyro2', 'Gyro3', 'Battery', 'Counter', 'Validation']
    data_dict = dict((k, []) for k in columns)
    start_time = time.time()

    while time.time() - start_time < duration:
        data, timestamp = inlet.pull_sample()
        all_data = [timestamp] + data

        for i, key in enumerate(columns):
            data_dict[key].append(all_data[i])

    data_df = pd.DataFrame.from_dict(data_dict)
    print("Done recording")
    return data_df


def show_image_fullscreen(image_path, duration=2):
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background='white')

    img = Image.open(image_path)
    img = ImageTk.PhotoImage(img)

    label = tk.Label(root, image=img)
    label.pack(expand=True)

    root.after(duration * 1000, root.destroy)
    root.mainloop()


def show_image_and_record(image_path, inlet, duration=2):
    display_thread = threading.Thread(target=show_image_fullscreen, args=(image_path, duration))
    display_thread.start()

    data_df = record_data(inlet, duration)

    display_thread.join()

    return data_df


if __name__ == "__main__":
    streams = resolve_stream()
    inlet = StreamInlet(streams[0])

    # Create directories if they do not exist
    os.makedirs('recordings/left_label', exist_ok=True)
    os.makedirs('recordings/right_label', exist_ok=True)

    number_of_pair_recordings = 20
    time.sleep(3)

    for i in range(number_of_pair_recordings):
        print("Showing left.png")
        left_data = show_image_and_record('left.png', inlet)
        left_filename = f"recordings/left_label/left_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        left_data.to_csv(left_filename, index=False)
        print(f"Saved {left_filename}")

        time.sleep(3)

        print("Showing right.png")
        right_data = show_image_and_record('right.png', inlet)
        right_filename = f"recordings/250824/right_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        right_data.to_csv(right_filename, index=False)
        print(f"Saved {right_filename}")
        time.sleep(3)

    print("Recording complete.")
