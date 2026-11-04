Task related to the learning resource
ACTIVITY 2: This activity will help you test your understanding of duck-typing: polymorphism
without inheritance.
—-------------
Allotted Time: 15 minutes
Grading: Non-graded, but submission is required.
Submission: Upload your file to the Khub submission bin.
File Name: Follow the file name format provided by your teacher.

Instruction: Do what is asked in each item below:
1. Answer the following questions:
a. What is duck typing, as explained in the video?
- It basically is a type of polymorphism that assumes that if the object acts like duck then it is a duck.
b. What did the Car class need to have so it could work inside the same loop as Dog and
Cat, even if it does not inherit from the Animal class?
- It can make a sound.
2. Create the Python code that:
a. Creates three classes: Car, Boat, and Drone with a method move().
move() in the Car class prints "The car drives on the road."
move() in the Boat class prints "The boat sails on water."
move() in the Drone class prints "The drone flies in the sky."
b. Has a function named start_trip(vehicle), with a parameter vehicle, that simply calls the
move() method: vehicle.move().
c. Creates one object of each class.
d. Calls the start_trip() method for each object. -- Complete
3. How does the code in 2.2 demonstrate polymorphism?
- A single function can output different results.