import os
import cv2


def record_video(duration, output_path):
    # Open the webcam
    cap = cv2.VideoCapture(0)

    # Define the video codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_file = os.path.join(output_path, 'output5.mp4')
    output = cv2.VideoWriter(output_file, fourcc, 20.0, (640, 480))

    # Record video for the specified duration
    start_time = cv2.getTickCount()
    while (cv2.getTickCount() - start_time) / cv2.getTickFrequency() < duration:
        ret, frame = cap.read()
        if ret:
            # Write the frame to the output file
            output.write(frame)
            # Display the resulting frame
            cv2.imshow('Webcam Recording', frame)

            # Check for 'q' key press to stop recording
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # Release the resources
    cap.release()
    output.release()
    cv2.destroyAllWindows()

    # Open the saved video file and play it
    saved_video = cv2.VideoCapture(output_file)
    while saved_video.isOpened():
        ret, frame = saved_video.read()
        if not ret:
            break
        cv2.imshow('Recorded Video', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    saved_video.release()
    cv2.destroyAllWindows()


# Specify the duration (in seconds) to record
duration = 10

# Specify the output folder path
output_folder = 'E:/Repo/1. Python'

# Call the function to start recording
record_video(duration, output_folder)
