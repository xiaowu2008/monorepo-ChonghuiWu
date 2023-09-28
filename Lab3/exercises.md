# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!


## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
	MObject is a concrete class as it can be instantiated.
1. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
	The commented-out __del__ method is a destructor which would be called when an object is deleted. 
1. What class does Texture inherit from?
	The Texture class inherits from the Image class.
1. What methods and attributes does the Texture class inherit from 'Image'? 
	The Texture class inherits all methods (getWidth, getHeight, getPixelColorR, getPixels, setPixelsToRandomValue) and attributes (m_width, m_height, m_colorChannels, m_Pixels) from the Image class.
1. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
	I think it is a 'has-a' relationship as A texture is not inherently an image. And as required, I refactored the code.

1. I did not declare a constructor for Texture. Does Python automatically create constructors for us? 
	Yes, Python automatically provides a default constructor if you do not provide one.

## Task 2 - Singleton

1. Refactor the singleton.py file such that:
  - The first time the logger is constructed, it will print out:
  	-  `Logger created exactly once`
  - If the logger is already initialized, it will print:
  	-  `logger already created`
Note: You do not 'have' a constructor, but you construct the object in the *instance* member function where you will create an object.  
Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

1. Are singleton's in Python thread safe? Why or why not?

Singletons in Python are not inherently thread-safe. Without proper locks and synchronization, two threads might create two separate instances of the Singleton class if they check the instance existence at the same time.
  
