f = open('wasteland.txt', mode='at', encoding='utf-8')

# writelines - similar to readlines
f.writelines(
    ['You\'ll dive deeper into unit ',
     'testing and debugging, as well as learn some of the more advanced features of the Python language.\n ',
     'Our advanced Python track will show you how you can apply your newfound skill. ',
     'You\'ll learn full-stack web \n',
     'development, as well as some techniques that will help you implement advanced frameworks.']
)
f.close()