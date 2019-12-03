from django.shortcuts import render
from django.http import HttpResponse
import json,sys,os
import pickle
from backend.models import Users
# Create your views here.

from backend.fuck_poe.network_model import poetry_network
from backend.fuck_poe.fuck_generate import gen_poetry

cur_file = os.path.abspath(sys.argv[0])
cur_path = os.path.dirname(cur_file)

def index(request):
    return HttpResponse("Hello")

def gen_f_poetry(request):
    keywords = request.GET.get('title')

    # 加载数据
    int_text, vocab_to_int,int_to_vocab = \
        pickle.load(open(cur_path+"\\backend\\fuck_poe\\preprocess.p",mode='rb'))

    # 加载模型
    gen_network = poetry_network(vocab_size=len(int_to_vocab),batch_size=1)
    gen_network.model.build()

    poem = gen_poetry(
        restore_net=gen_network,vocab_to_int=vocab_to_int,
        int_to_vocab=int_to_vocab,top_n=10,
        rule=7,sentence_lines=4,hidden_head=keywords
    )
    return HttpResponse(poem)

def logon(request):
    username = request.POST['username']
    passwod = request.POST['passwod']
    print('--->',username,type(username))
    print('--->',passwod,type(passwod))

    user = Users.objects.filter(username=username)
    if user:
        print("用户名唯一")
        new_user = Users()
        Users.objects.create(username=username,passward=passwod)
        return HttpResponse("注册成功")
    else:
        return HttpResponse("注册失败")