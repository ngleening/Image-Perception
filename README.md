# Try to beat this sophisticated approach which analyzes your Rock-Paper-Scissors patterns!

#### A project by Lee Ning, Grace, Osbert & Qian Yu

## Team Quote: "When you think you're playing randomly, you're actually not"
This code helps you to play the classic game of Rock-Paper-Scissors, with a twist.


### Code Requirements
1. You will need either Anaconda or Python3.
2. pip install requirements.txt
3. Allow webcam access to your preferred code execution application


### Description
Rock–paper–scissors (also known as scissors-paper-rock or other variants) is a hand game usually played between two people, in which each player simultaneously forms one of three shapes with an outstretched hand. These shapes are "rock" (a closed fist), "paper" (a flat hand), and "scissors" (a fist with the index finger and middle finger extended, forming a V). "Scissors" is identical to the two-fingered V sign (aka "victory" or "peace sign") except that it is pointed horizontally instead of being held upright in the air. A simultaneous, zero-sum game, it has only two possible outcomes: a draw, or a win for one player and a loss for the other.


### Rules
Scissors cuts Paper --> Paper covers Rock --> Rock crushes Scissors 


### Gameplay (For class presentation)
The class will split into teams where each group will play against one another.

Instructions:
1. First play will be for each group to win chips. You will need to play 10 rounds of RPS. The number of points you win will translate into chips for you to bet in subsequent rounds. In this round, 1 point = 5 chips.
2. After you have won chips, each group will take turns to go through 3 plays of 30 rounds each. 
3. In order to enter each play, you have to bet a certain number of chips. If you win the computer in RPS after each play, then you will win back double the chips you bet. If you lose to the computer, then you will lose the chips you bet. 
4. After 3 plays, the group that has the most number of chips will win a special prize! 

Rules before playing:
1. Please follow sample examples of the ideal hand gestures. (e.g. Cannot have your arm shown in the image)
2. If the screen does not detect your chosen hand gesture, move your hand slightly until it detects the correct one.


### Implementation - Hand detection
Network Used: Convolutional Neural Network<br/>
Layers:

**Basic CNN:**
As there is no need for a complex neural network model for training of these 3 images, we adapted a small part of VGG16's model out to create a basic CNN model. Using a complex model may result in expensive computational power to be required and high cost in time and it may even yield the same result as the basic CNN model shown here.
	
	1. Conv2D-32

	2. MaxPool2D

	3. Conv2D-64

	4. MaxPool2D
**Classification Layer:**

	1. Flatten

	2. FC-1024 
		- A Dense layer with 1024 nodes and ReLu activation
	
	3. Dropout
		- It is likely that we have overfitted the model hence, we chose a higher dropout ratio of 0.6. This helps to thin the network during training.

	4. Softmax

**Compile Model:**
	
	1. Adam Optimizer (learning rate was auto-tuned)


### Implementation - For CPU to defeat User
The common idea of RPS is that it is a game of chances, a game of randomness but we seek to differ from this opinion.

A group of researchers from Chinese universities have written a paper about the role of psychology in winning (or losing) at rock-paper-scissors. After studying how players change or keep their strategies during multiple-round sessions, they figured out a basic rule that people tend to play by that could potentially be exploited.

This gave us the intuition to create an RPS algorithm built on this rule. We believe that by harnessing the power of computing, we can devise a strategy to beat human in this game, beyond chances by figuring out patterns played.

Our Algorithm works in this way:
1. For the 1st round, the CPU will randomly select Rock, Paper or Scissors since there is no prior knowledge of what our opponent will play

2. In subsequents round (up to the 10th round), the CPU will start to analyse if the human is playing in a certain manner such as:
	a. Using only a single gesture
	b. Playing in pairs (i.e: RP-RP-RP)
	c. Copying the moves made by the CPU
On detection that a consistent pattern is played by the human, the CPU will make counter moves accordingly.

3. From the 10th round and onwards, we modified the Markov Decision Policy and introduced a Rewards-and-Penalty system. Based on the probability of each subsequent move played by the human, the system will give a 1.5 reward for a winning move by CPU, a 0.5 reward for a draw and a -1.2 reward for a lose.

This computer will the compute the probability of making a move and choose the action that gives the maximises the reward. This allows the model to learn the pattern of how the human plays over time and makes calculated decisions instead of playing it randomly.


### Procedure
Go through the presentation slide 'RPS_Presentation.pptx'.
Afterwards, just run 'RPS_App.py' for playing Rock-Paper-Scissors via webcam. Have fun!


### Directories
1. RPS_generatedata - This folder contains <b>CreateGest.py</b> which helps to create our training images and <b>CreateCSV.py</b> which is used to tranform it into a CSV file.
2. RPS_gestures - This folder contains our training images.
3. RPS_training - This folder contains <b>RPS_Model.py</b> which we used to form the architecture for our hand detection model.
4. RPS_emo - This folder contains the emojis used to depict the user or CPU's actions.
5. <b>RPS_MEDIUM.py</b> - This file is our algorithm for the CPU to beat user.
6. <b>RPS_App.py</b> - This file is our game stimulation python file.
7. RPS_logs & RPS_dir_logs - This two folders contains our log files.
8. <b>RPS_Presentation.pptx</b> - This file contains our final presentation slides.



