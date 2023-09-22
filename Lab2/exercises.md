# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping) 
and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL. 
Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.

I think that for "clear", "get", "items" ...they are chosen to be descriptive verbs that convey the primary action they perform. only pop() have two actions.

2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

A list is an ordered collection of elements (O(1) average time complexity for append operations and O(n) time complexity for inserting or deleting elements from or within the list. ), while a dictionary is an unordered collection of key-value pairs.( O(1) for lookups, insertions, and deletions)

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

Yes, a list allows for random access. You can directly access any element of the list using its index in constant time O(1).

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.). 
What do you think are the pros/cons of a library that can work with any data type?

Pro: 1, it provides flexibility as we can use the same container data structure for multiple data types without needing specialized versions for each type. 
2, Developers don't need to define the data type of the elements when declaring or initializing a container, making coding faster and more intuitive.
Cons: 1, Containers that can hold any data type have to store additional information about the type of each element, which can introduce memory overhead.
2, Without static typing, type-related errors can occur at runtime, which might be harder to debug compared to compile-time type checking.

## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

All the functions are well named in the Requests module.

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

No because most of these extra arguments are optional, only use them when it is needed.

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?  

`**kwargs`  is a way of passing a variable number of keyword arguments to a function.

Pros: 1, It provides flexibility in that you can extend the function's functionality in the future without changing its signature.
2, You can pass this dictionary of keyword arguments to another function, which makes it easier to reuse and delegate functionality.

Cons: 1, It's easier to make mistakes by passing incorrect argument names.
2, When reading code, it's not immediately clear what the expected arguments are, making the code harder to understand.
3, Automatic documentation generation tools might not capture all the possible keyword arguments, making it harder for users to know what's supported.

4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text. 
Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?


1, None is served as default value. Making them optional. For parameters without default values, they are considered mandatory, and the caller must provide values for them when invoking the method.
2, Yes, default argument values can be any valid Python value.
3,  By setting default values, the number of overloaded methods or function signatures can be reduced thus make a function or method easier to use. Also, it can prevent some missing argument errors.
