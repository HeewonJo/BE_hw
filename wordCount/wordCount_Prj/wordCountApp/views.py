from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def wordCount(request):
    return render(request, "wordCount.html")

def result(request):
    entered_text = request.GET['fulltext']
    word_list = entered_text.split()

    word_dictionary = {}
    
    # word_num = 1
    # for text in entered_text:
    #     if text == ' ':
    #        word_num += 1

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    word_num = entered_text.count(' ') + 1
    space_include = len(entered_text)
    space_except = space_include - entered_text.count(' ')

    return render(request, "result.html", {'alltext': entered_text, 'dictionary': word_dictionary.items(), 'word_num': word_num, 'space_include': space_include, 'space_except': space_except})

def hello(request):
    entered_name = request.GET["myname"]

    return render(request, "hello.html", {"myname": entered_name})