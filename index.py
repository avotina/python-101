# msg='My name is Kate'
# new_msg=msg[11:]+msg[7:10]+' '+msg[0:2]+msg[2:7]
# print(new_msg.upper())

# msg="""Hello, this is my
# first multiline string,
# yes it is!"""
# print(msg)

# msg='Welcome to Python 101: Strings'
# print(msg.replace('Python', 'Java'))
# print('Python' in msg)

# name='MARTA'
# color = 'RED'
# msg = '[' + name + '] loves the color ' + color.lower() + '!'
# msg1 = f'[{name.capitalize()}] loves the color {color.lower()}!'
# print(msg)
# print(msg1)

# name= input('What is your name?:')
# age= input('What is your age?:')
# print('Hello '+name+ ' you are '+age+' years old'+'!')

# num1= input('Number 1 is:')
# num2= input('Number 2 is:')
# answer=float(num1)*float(num2)
# print(answer)

name = input('Enter your name: ')
distance_km = input('Enter distance in km: ')
distance_mi = float(distance_km)/1.609
print(f'Hi {name.title()}! {distance_km}km is equivalent to {distance_mi} miles.')