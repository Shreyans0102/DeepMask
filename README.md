# DeepMask

Description as a Tweet:
Using Facial Recognition AI combined with a mask detector to tell if users are wearing their masks. If not, they are in for a surprise. Their photo will be posted to a (temporary) hall of shame, with a personal shaming from our beloved Chancellor.

Inspiration:
A passion for over-engineering. Doing dumb things in the most high tech ways possible. Also the Pandemic that has shaped the last 2 years of our lives.

What it does:
DeepMask is a system to detect people not wearing face masks, and swiftly deliver their punishment. This punishment includes, but is not limited to, Inclusion in the "Hall of Shame" and A thorough rebuke by our beloved Chancellor.

How we built it:
DeepMask is a system that uses multiple technologies across a wide range of technical fields. The Face Mask detection side is using a Machine Learning model to detect a person not wearing their face mask. This model communicates with a flask web server and an arduino. The flask web server hosts a temporary hall of shame to show people that are not wearing their masks. The arduino delivers a different kind of punishment: Slander by Swammy. Our Beloved Chancellor takes time out of his busy day to rebuke people not wearing their masks. Optionally, he also offers the offenders a new mask to wear, to avoid further punishment.

Technologies we used:
HTML/CSS
Python
Flask
Arduino
Raspberry Pi
Microcontrollers
AI/Machine Learning
Robotics
Other Hardware
Challenges we ran into:
Raspberry Pi -> We could not connect the RBP to eduroam so we could ssh into it and do things. After numerous hours of troubleshooting, we decided to use an arduino and do of the computer vision from the laptop's webcam.

AI Facial detection Model -> at first, we attempted to train our own CNN model with pytorch from the ground up from around 70,000 images of people wearing and not wearing their masks. We quickly realized this would not be possible as we do not have enough compute power to train an accurate model from scratch. Instead, we tried to use Transfer learning, a method of training a pretrained model on some new data to make the training less intensive. This seemed to work, but there were some issues integrating the two datasets together. At the end, we loaded a pretrained model that can detect face masks and used that instead.

In order to get our lithoplane to have the Chancellor's face visible, we needed a powerful enough light. This was very difficult to do. Once we got a power supply that was 24V, and an old high power LED, we connected it to a relay. This relay seemed to be working, but the LED light stopped turning on. After working with the HackUMass team, we eventually figured out how to get it to work (mostly out of luck) and soldered it into place.

Accomplishments we're proud of:
We are most proud of the face mask recognition system and its integration with the rest of the system. The data communication was challenging but rewarding in the end. We built all of these pieces of the system separately with no guarantee that they would all work together, but after some troubleshooting we were able to get all pieces to be compatible.

What we've learned:
We learned a lot about how to integrate software and hardware to build a full project. We had to go broad and deep to get this project to work, extending from AI/ML all the way to soldering power supplies to get an LED to work. All members learned how to work together as a team when time was limited.

What's next:
The next step of this project is to get the transfer learning model to work. This will allow us to detect a third category: mask worn incorrectly. If we could do this, we could program a third state for the system to provide intermediate punishment for wearing a mask but doing so incorrectly.

Built with:
Software:

The Facial detection system was written in python using PyTorch and openCV. The communication system to the arduino was also written in python. We built a flask server to host the hall of shame.

The hardware we used was an arduino, multiple servo motors, 3D printed lithoplane and figures.
