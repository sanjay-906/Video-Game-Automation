### Automating a Video Game<br>

Informally speaking, It's an aimbot, used to automatically detect enemies and lock the crosshair onto them 

#### STEP 1: Creating a custom dataset<br>
Screenshots from the game are taken and objects are labelled<br>
This is done using "MakeSense AI" which is a free, open source tool for labelling images<br>
<br>

![labelling](https://raw.githubusercontent.com/sanjay-906/Video-Game-Automation/main/Output/makesense%20ai.png)

The dataset contains images and their respective text files which has the coordinates of the bounding boxes of each label present in the image


#### STEP 2: Training Yolo v7 with the dataset<br>

![testing](https://raw.githubusercontent.com/sanjay-906/Video-Game-Automation/main/Output/test.png)

After training for 240 epochs, The best weights were taken for testing, and above is the result

#### STEP 3: Real time object detection from video game<br>

![output1](https://raw.githubusercontent.com/sanjay-906/Video-Game-Automation/main/Output/output1.png)

Live object detection from the game; the left part is game window and the right part is the output 


#### STEP 4: Moving the crosshair and shooting<br>


#### FINAL RESULT:<br>
