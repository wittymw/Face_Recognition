# Face Recognition Project

A Python-based face recognition system that uses OpenCV and dlib to detect and recognize faces in images or video streams. This project provides an easy-to-use implementation for face detection and recognition tasks.

## Features
- Real-time face detection in video streams
- Face recognition using pre-trained models
- Support for multiple face detection
- Easy integration with webcam
- User-friendly interface
- High accuracy detection and recognition

## Prerequisites
- Python 3.7+
- OpenCV
- dlib
- numpy
- face_recognition

## Installation

1. Clone the repository:
```bash
git clone https://github.com/wittymw/Face_Recognition.git
cd Face_Recognition
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. (Optional) Install dlib separately if needed:
```bash
pip install dlib
```

## Usage

1. Run the face detection script:
```bash
python face_detection.py
```
2. Run the train model script:
```bash
python train_model.py
```

3. Run the face recognition script:
```bash
python face_recognition.py
```

To use your own images:
   - Run the face_detection.py to capture and store your face images
   - Update the image paths in the script accordingly
   - Run the script to detect and recognize faces

## Project Structure
```
Face_Recognition/
│
├── dataset/                               # Folder for storing test images
├── auto.py                                # Script for automating all the scripts
├── face_shot.py       		    # Script for detecting faces
├── face_rec.py                   	    # Script for recognizing faces
├── haarcascade_frontalface_default.xml    # Model File
├── LICENSE                                # License file
├── README.md                              # Project documentation
├── requirements.txt                       # List of dependencies
└── train_model.py                         # Script for model training
```

## How It Works
1. **Face Detection**: The system uses OpenCV's Haar Cascade classifier to detect faces in images or video streams.
2. **Face Recognition**: Uses dlib's facial recognition model to identify and match faces with known samples.
3. **Real-time Processing**: Processes video streams in real-time for immediate face detection and recognition.

## Configuration
You can modify the following parameters in the scripts:
- Detection sensitivity
- Recognition threshold
- Input source (webcam/video file)
- Output display options

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- OpenCV community
- dlib library developers
- Face recognition library contributors

## Contact
Twitter - [@0xwittymw](https://twitter.com/0xwittymw)
Project Link: [https://github.com/wittymw/Face_Recognition](https://github.com/wittymw/Face_Recognition)

## Support
If you found this project helpful, please give it a ⭐️!
