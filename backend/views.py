from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import redirect
import json,sys,os
import pickle
from backend.models import Users
import json
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

def token(request):
    token = get_token(request=request)
    return JsonResponse(token,safe=False)

def logon(request):
    if request.method == "POST":
        print('fuck you')

        postBody = request.body
        json_result = json.loads(postBody)
        username = json_result['username']
        password = json_result['passward']

        print("=>",username,password)
        print('=>',postBody)
        print('=>',request.POST)
        user = Users.objects.filter(username=username)
        if user:
            print("用户已存在")
            return HttpResponse("用户名已存在")
        else:
            # 创建用户
            new_user = Users()
            new_user.username = username
            new_user.passward = password
            new_user.save()
            return HttpResponse("注册成功")

def login(request):

    return HttpResponse("fuck you")