def empath_extraction(text):
    # You need to 'pip install empath' first
    from empath import Empath
    lexicon = Empath()
    # Get the Empath result
    '''Note : The output sequence of empath is random!!!'''
    result = lexicon.analyze(text, normalize=True)
    # Filter out those equal to zero
    output = dict()
    for (k, v) in result.items():
        if (v > 0):
            output[k] = v
    '''You can either print the result directly
        With format :  '#the class#':#the score#'''
    # Change the form of output as you need
    # for (k,v) in output.items():
    #     print(k + "-" + str(v))
    '''Or you can get the predefined classes in ./empathClass.txt
        and convert the #the class# into number,
        which may be more convenient and efficient for other programs to process.
        But this will definitely slow down this python code'''
    class_empath = dict()
    with open(r"./empathClass.txt") as file:
        for line in file:
            tmp = line.split(",")
        for index, item in enumerate(tmp):
            class_empath[item] = index
    output_convet = []
    for (k,v) in output.items():
        output_convet.append([str(class_empath[k]), str(v)])
    # Change the form of output as you need
    for item in output_convet:
        print("-".join(item))

# Test the result here.
empath_extraction("he hit the other person")