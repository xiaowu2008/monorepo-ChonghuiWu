**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 4

<hr>

**Use Case**: Save Canvas

**Primary Actor**: User

**Goal in Context**: Save the current state of the canvas as an image file.

**Preconditions**: The application is running, and the canvas contains some drawings.

**Trigger**: User selects the 'Save' option from a menu.
  
**Scenario**: 
1. User initiates the save command either by selecting the 'Save' option from a menu.
2. The system prompts the user to select a location and provide a filename.
3. User chooses the location and provides a filename.
4. The system saves the current state of the canvas as an image file to the specified location with the given filename.
 
**Exceptions**: 
User initiates the save command, but the system fails to save the image.

Corrective Action:
The system displays an error message to the user indicating the issue.
The system prompts the user to try saving again or choose a different location.

**Priority**: High

**When available**: First release

**Channel to actor**: Graphical User Interface

**Secondary Actor**: File System

**Channels to Secondary Actors**: Operating System API

**Open Issues**: 
Consider adding a "Save As" feature for users to save in different formats or locations without overwriting the original file.

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
