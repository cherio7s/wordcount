from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request , 'home.html')

def count(request):
    data=request.GET['fulltextarea']
    data_list=data.split()
    length=len(data_list)
    print(length)
    word_dict={}

    for word in data_list:
        if word in data_list:
            word_dict[word]=+1
        else:
            word_dict[word]=1


    return render(request , 'count.html',{"fulltext":data,"words":length , "word_dict":word_dict})
