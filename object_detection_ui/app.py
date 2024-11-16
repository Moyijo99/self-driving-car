from flask import Flask, Response, render_template
import cv2

app = Flask(__name__)
cap = cv2.VideoCapture(0)  # Change to a video file path if needed

def generate_frames():
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Run object detection here (example: add a dummy rectangle)
        cv2.rectangle(frame, (50, 50), (200, 200), (0, 255, 0), 2)
        cv2.putText(frame, "Detected Object", (60, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # Encode the frame as JPEG
        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
