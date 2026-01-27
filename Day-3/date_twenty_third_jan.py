### list comprehension where we are storing element from one to another in the form of title

# names=["Aniket","Bhanu","Murthy","Sadgyan"]
# name=input()
# names2=names[:2]
# print(names2)
# for name in names:
#     if len(name)==7:
#         names2.append(name.title())
# print(names2)

#OR

# names2=[name.title() for name in names if len(name)==7]
# print(names2)

#----------------------------------------------------------------------------------------------------------------------------#
### dictionary comprehension

# types={'name':str,'age':int,'address':str}
# new_entry={}
# for i in types:
#     new_entry[i]=i.title()
# print(new_entry)

#OR

# new_entry={i:i.title() for i in types}
# print(new_entry)

#----------------------------------------------------------------------------------------------------------------------------#
### Lambda functions(its a enormous function which is used to call only single variable  to avoid call it rigorously its also has space complex)

# def adder(x,y):
#     return x+y
# adder2=lambda x,y:x+y
# result=(adder(42,10)==adder2(42,10))
# print(result)
#---------------------------------------------------------------------------------------------------------------------------------

### create lambda functionw hoch return cube of number

# def cube(x):
#     return x**3
# cube2=lambda x:(x**3)
# result=cube2(3)==cube(3)
# print(cube(3))
# print(result)
#--------------------------------------------------------------------------------------------------------------------------------------

### Lambda in sorting

#name=["Aniket","bhanu","murthy","sadgyan"]
# print(sorted(name))

### OR

#print(sorted(name,key=lambda name:len(name)))
#----------------------------------------------------------------------------------------------------------------------------#

### Classes (we cand efine every entity as an obejct)

# class duck:
#     sound='Quack quack'
#     movement='have flat foor and slow in walk'

#     def quack(self):
#         print(self.sound)

#     def move(self):
#         print(self.movement)

# def main():
#     donald=duck()
#     donald.quack()
#     donald.move()

# if __name__ =='__main__':main()
        
### Methods

# class animal:
#   def __init__(self,**kwargs):
#     self._type=kwargs['type'] if 'type' in kwargs else 'kitten'
#     self._name=kwargs['name'] if 'name' in kwargs else 'fluffy'
#     self._sound=kwargs['sound'] if 'sound' in kwargs else 'meow'
#   def type(self,t=None):
#     if t:
#       self._type=t
#       return self._type
#   def name(self,t=None):
#     if t:
#       self._name=t
#       return self._name
#   def sound(self,t=None):
#     if t:
#       self._sound=t
#       return self._sound
#   def __str__(self):
#     return f'The {self._type} is named {self._name} and says {self._sound}'
# def main():
#   a1=animal(type='kitten',name='fluffy',sound='meow')
#   a2=animal(type='duck',name='donald',sound='quack')
#   print(a1)
#   print(a2)
# if __name__=='__main__':
#   main()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

### Inheritance

# class Animal:
#     def _init_(self, **kwargs):
#         if 'type' in kwargs: self._type = kwargs['type']
#         if 'name' in kwargs: self._name = kwargs['name']
#         if 'sound' in kwargs: self._sound = kwargs['sound']

#     def type(self, t = None):
#         if t: self.__type = t
#         try: return self._type
#         except AttributeError: return None

#     def name(self, n = None):
#         if n: self.__name = n
#         try: return self._name
#         except AttributeError: return None
    
#     def sound(self, s = None):
#         if s: self.__sound = s
#         try: return self._sound
#         except AttributeError: return None

# class Duck(Animal):
#     def _init_(self, **kwargs):
#         self._type = 'Kitten'
#         if 'type' in kwargs: del kwargs['type']
#         super()._init_(**kwargs)

#     def type(self, t = None):
#         if t: self._type = t
#         return self._type

#     def sound(self, s = None):
#         if s: self._sound = s
#         return self._sound

#     def quack(self):
#         print(self._sound)

#     def move(self):
#         print(self._sound)

#     def _str_(self):
#         return f'The {self._type} named {self._name} says {self._sound}'
    
# def main():
#     a1 = Duck(type = 'Kitten', name = 'Fluffy', sound = 'rwar')
#     a2 = Duck(type = 'Duck', name = 'donald', sound = 'quack')
#     print(a1)
#     print(a2)

# if __name__ == "_main_":
#     main()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------