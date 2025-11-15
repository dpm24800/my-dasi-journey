---
layout: post
title: Object Oriented Programming Basics – Python
description: 
thumbnail: ../../../../assets/images/python/oop.jpg
author: Dipak Pulami Magar
date:   2025-11-15 16:12:45 +0545
categories: python
status: draft
---

# 1. Introduction to OOP
- Object-Oriented Programming (OOP) is a programming paradigm that organizes code into **objects**—containers that bundle **data** (attributes) and **behavior** (methods).
- It is a method of structuring programs so that data and functions that operate on that data are bundled together into logical units called objects.
- It helps in building large, modular, maintainable, and reusable software systems.
- It is based on the idea that everything in a program can be represented as an object. 
  - An object represents a real-world entity such as a student, a car, a bank account, or even a concept like a transaction.

## 1.2. Why Python uses OOP?
Python supports multiple paradigms, including procedural, functional, and object-oriented programming. OOP becomes useful in Python when building:
* Data models
* Frameworks
* APIs
* Large scripts or applications
* Machine learning pipelines
* GUIs

## 1.3. Features of OOP:
* **Modularity:** Breaks large programs into small, logical parts.
* **Reusability:** Inheritance allows writing once and reusing multiple times.
* **Maintainability:** Easy to update or fix.
* **Scalability:** Useful for large systems (ML pipelines, apps, games, etc.).

### 1.4. OOP vs. Procedural Programming

| Procedural                      | OOP                              |
| ------------------------------- | -------------------------------- |
| Step-by-step instructions       | Based on objects & interactions  |
| Functions + data separate       | Data + behavior bundled together |
| Harder to scale                 | Easier to scale                  |
| More suitable for small scripts | Better for large applications    |

<!-- | dfdsfsdfs | dfdfsdf |
| dfdsfsdfs | dfdfsdf |
| dfdsfsdfs | dfdfsdf | -->

- In procedural programming, functions and data are separate. 
- In OOP, both are combined inside classes, making the code more organized. 
- Procedural style is suitable for small scripts, but OOP is better for larger systems where structure matters.

---

# 2. Classes & Objects
- A **class** is a blueprint; an **object** is an instance of that blueprint.
- A class is a blueprint or template. An object is an instance created from that blueprint.

## Defining a Class
```python
class Person:
    pass
```

## Creating an Object
```python
p = Person()
```

## Constructor: `__init__`
### The `__init__` Constructor
This method runs automatically when object is created.
The constructor initializes object attributes during creation.
```python
class Person:
    def __init__(self, name, age):
        self.name = name      # Instance attribute
        self.age = age        # Instance attribute
```

## Understanding `self`: The role of `self`
- The `self` parameter refers to the specific object being created or used. 
- It is used to access attributes and methods belonging to that object.
* Refers to **current object**.
* Needed to access attributes/methods inside the class.

Example:

```python
class Person:
    def greet(self):
        print("Hello, I’m", self.name)
```

---

# 3. Attributes & Methods
Objects contain data (attributes) and behavior (methods).
- Attributes are variables inside a class.
- Methods are functions inside a class.

## 3.1 Instance Attributes
- Each object has its own values.  
- Instance attributes belong to each object separately.

```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand      # instance attribute
        self.model = model
        self.year = year
```

Different instances have different values:

```python
c1 = Car("Toyota", "Corolla", 2020)
c2 = Car("Tesla", "Model S", 2024)
```

## 3.2 Class Attributes
- Class attributes are *shared by all objects* of the class.

```python
class Car:
    wheels = 4   # class attribute, shared for all cars
    
    def __init__(self, brand):
        self.brand = brand

car1 = Car("BMW")
car2 = Car("Audi")

print(car1.wheels)  # 4
print(car2.wheels)  # 4
```

## 3.3 Types of Methods: Instance, Class & Static Methods
### Instance Methods
For operating on object (instance) data.
These operate on individual object data. They require `self`.

```python
class Test:
    def show(self):
        print("This is instance method.")
```

```python
class Test:
    def instance_method(self):
        print("Instance method called")
```

### Class Method — `@classmethod`
- These operate on class-level data. 
- Works with **class**, not object.
- They use the `@classmethod` decorator and receive the class as the first parameter (`cls`).

```python
class Student:
    school = "Himalayan School"

    @classmethod
    def get_school(cls):
        return cls.school
```

### Static Methods— `@staticmethod`
- General utility method—not tied to class or object.
- These do not access object or class data. They behave like normal functions but belong inside a class for logical grouping.
- 
```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b
```

---
`__str__` and `__repr__`
## **3.4 String Representation Methods**

### **`__str__` → User-friendly output**
Returns a human-readable string. Used by `print()`.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person: {self.name}"

print(Person("Dipak")) 
```

### **`__repr__` → Developer representation**
Returns a machine-readable string used for debugging or logging.

```python
def __repr__(self):
    return f"Person(name='{self.name}')"
```

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person: {self.name}"

    def __repr__(self):
        return f"Person(name='{self.name}')"
```

## 1.1. Major Principles of OOP:
1. [Encapsulation](#4-encapsulation)
2. [Inheritance](#6-inheritance)
3. [Abstraction](#5-abstraction)
4. [Polymorphism](#7-polymorphism)

These principles allow the program to be cleaner, scalable, and easier to debug.

---

# **4. Encapsulation**
- Encapsulation means restricting access to certain attributes so users cannot change them accidentally. 
- In Python, encapsulation is done through naming conventions.

> Encapsulation = protecting data from direct modification.

Python doesn't enforce strict private variables, but uses:
* `_var` → protected (convention)
* `__var` → private (name mangling)

---

## Public Attributes
Accessible from anywhere.

```python
self.name
```

### Protected Attribute
Indicated with a single underscore. Developers agree not to access them directly.

```python
class A:
    _value = 10
    self._salary
```

---

## Private Attributes
### **Private Attribute & Name Mangling**
Indicated with double underscore. Python performs name mangling.

```python
class Bank:
    def __init__(self, balance):
        self.__balance = balance   # private

    def get_balance(self):
        return self.__balance

b = Bank(5000)
print(b.get_balance())       # ✔ works
print(b.__balance)           # ❌ Error
```

Internally Python changes name:
`_Bank__balance`

```python
self.__balance
```

Accessing private attributes directly will cause an error.

---

### Getters & Setters Using `@property`
Python's preferred way to enforce encapsulation is the `@property` decorator.

```python
class Student:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) < 3:
            raise ValueError("Name too short")
        self.__name = value
```
This avoids directly exposing internal variables.

---

# 5. Abstraction
Abstraction = hiding complex details, showing only necessary parts.
Python supports abstraction using **abstract classes**.

Abstraction hides complexities and exposes only essential parts. Python supports abstraction using abstract classes and abstract methods.

Abstract classes cannot be instantiated. They act as blueprints for subclasses.

### Abstract Class Example
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"
```
Subclasses must implement the abstract method.

```python
class Dog(Animal):
    def sound(self):
        return "Bark"
```

Abstraction helps ensure a standard interface across subclasses.

---

# 6. Inheritance
- Inheritance allows a class (child/subclass) to derive features from another class (parent/superclass).
- This enables code reuse and logical hierarchy.
- A class can inherit properties/methods from another.

## 6.1 Single Inheritance
```python
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    pass
```

## 6.2 Multilevel Inheritance

```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass
```

## **6.3 Multiple Inheritance**

```python
class A: 
    pass
class B: 
    pass

class C(A, B):
    pass
```
When methods conflict, Python resolves them using the Method Resolution Order (MRO).
Python resolves conflicts using **MRO** (Method Resolution Order).

## **6.4 Using `super()`**

```python
class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def show(self):
        super().show()
        print("Child")
```

### **6.5 Method Overriding**
- A child class can redefine a method of the parent.
- Child modifies parent method.

```python
class Animal:
    def sound(self):
        print("Some sound")

class Cat(Animal):
    def sound(self):
        print("Meow")
```

## 6.5 Using `super()`
`super()` is used to call parent methods inside child methods.

```python
class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def show(self):
        super().show()
        print("Child")
```

---

# 7. Polymorphism
Means “many forms”.
One interface → multiple implementations.
Polymorphism means "many forms." Python supports polymorphism in multiple ways.

## 7.1 Polymorphism with Methods Overriding

```python
class Bird:
    def fly(self):
        print("Flying")

class Penguin(Bird):
    def fly(self):
        print("Cannot fly")
```

## 7.2 Duck Typing
- Python cares about behavior, not type.
- Python uses behavior rather than type. If two objects have the same method name, they are interchangeable.

```python
class Duck:
    def sound(self):
        print("Quack")

class Dog:
    def sound(self):
        print("Bark")

for obj in (Duck(), Dog()):
    obj.sound()
```

## **7.3 Operator Overloading**
Special methods allow custom behavior for operators.

Example: Overloading `+`

Custom behavior for `+`, `-`, etc.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
```

---

# 8. Special (Dunder) Methods
Dunder methods begin and end with double underscores. They allow objects to integrate with Python syntax.

Dunder = “Double underscore”
These give objects special behavior.

### **Common Dunder Methods**
Common methods include:
| Method                   | Purpose              |
| ------------------------ | -------------------- |
| `__init__`               | Constructor          |
| `__str__`                | User readable        |
| `__repr__`               | Developer readable   |
| `__len__`                | len(obj)             |
| `__getitem__`            | Indexing             |
| `__setitem__`            | Assigning index      |
| `__call__`               | Make object callable |
| `__eq__`, `__lt__`, etc. | Comparisons          |
| `__add__`, `__sub__`     | Operator overloading |

---

* `__init__` (constructor)
* `__str__` (readable output)
* `__repr__` (debug representation)
* `__len__` (length)
* `__getitem__` and `__setitem__` (indexing)
* `__call__` (make object callable)
* Comparison methods: `__eq__`, `__lt__`, `__gt__`
* Arithmetic methods: `__add__`, `__sub__`, `__mul__`

Example: making an object callable

```python
class A:
    def __call__(self):
        print("Object called like a function")

obj = A()
obj()  # behaves like a function
```

---

# 9. Advanced OOP Concepts
These are not required for beginners but very useful as projects get bigger.

## 9.1 Composition
A class is composed of other classes.
Has-a relationship.

```python
class Engine:
    pass

class Car:
    def __init__(self):
        self.engine = Engine()   # Composition
```
This represents a "has-a" relationship.

## 9.2 Aggregation
Similar to composition, but the contained object can exist independently.

Whole-part relationship but part can exist independently.

```python
class Department:
    pass

class College:
    def __init__(self, dept):
        self.dept = dept
```

## 9.3 Mixins
A mixin is a class that provides methods to another class but is not intended to be used independently.

Class used only to add functionality.

```python
class JsonMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class User(JsonMixin):
    def __init__(self, name):
        self.name = name
```

## 9.4 `__dict__` and Namespaces
Shows object attributes.

```python
obj.__dict__     # shows instance attributes
Class.__dict__   # shows class attributes, methods
```

## 9.5 `__slots__`
Used to limit attributes and reduce memory usage.

Restrict attributes and save memory.

```python
class Person:
    __slots__ = ['name', 'age']
```
# Conclusion
This detailed note covers:
- Core OOP principles
- All class/method types
- Encapsulation, abstraction, inheritance, polymorphism
- All essential dunder methods
- Advanced concepts like mixins, composition, slots