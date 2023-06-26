# 2023international-online-competition-of-auto-running-robots
2023国际机器人线上赛 分数为51 可优化
***
其实第四题有高分的程序，与我这个版本的差距较大，但是还是希望有人能把我这个优化优化，应该也可以取得高分。
对于其余的题目 飞桨上开源的项目也完全够用，优化也相对容易很多。
等之后机器人到了再记录线下赛的日常~~~

Start
├─ Initialize the application and main window
│  ├─ Connect signals to respective slots
│  ├─ Set up the UI
│  ├─ Create a timer and an elapsed timer
│  └─ Initialize variables and objects
├─ Handle button clicks
│  ├─ Start the video capture and timer when "Sure" button is clicked
│  └─ Stop the video capture and timer when "Cancel" button is clicked
├─ Display video frames
│  ├─ Read the next frame from the video capture
│  ├─ Flip the frame horizontally
│  ├─ Display the frame with various object detection options
│  │  ├─ If "Random Target" checkbox is checked, perform random target detection
│  │  ├─ If "Face" checkbox is checked, perform face detection
│  │  └─ If "Eye" checkbox is checked, perform eye detection
│  ├─ Draw the target trajectory on the frame
│  ├─ Show the last known target position
│  └─ Display the frame in the main window
├─ Perform random target detection
│  ├─ Apply image preprocessing operations
│  ├─ Perform background subtraction
│  ├─ Find contours in the resulting foreground mask
│  ├─ Find the largest contour that meets the size threshold
│  ├─ Draw a bounding box around the target
│  ├─ Add the target position to the trajectory list
│  └─ Reset the elapsed timer
├─ Perform face detection
│  ├─ Apply image preprocessing operations
│  ├─ Detect faces in the frame using a face cascade classifier
│  ├─ For each detected face, apply background subtraction
│  ├─ Find contours in the resulting foreground mask
│  ├─ Find the largest contour that meets the size threshold
│  ├─ Draw a bounding box around the target
│  ├─ Add the target position to the trajectory list
│  └─ Reset the elapsed timer
├─ Perform eye detection
│  ├─ Apply image preprocessing operations
│  ├─ Detect eyes in the frame using an eye cascade classifier
│  ├─ For each detected eye, apply background subtraction
│  ├─ Find contours in the resulting foreground mask
│  ├─ Find the largest contour that meets the size threshold
│  ├─ Draw a bounding box around the target
│  ├─ Add the target position to the trajectory list
│  └─ Reset the elapsed timer
└─ Exit the application

End
