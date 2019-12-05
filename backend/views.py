from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import redirect
import json,sys,os
import pickle
from backend.models import Users,UserGen
import json
import re
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
    if request.method == "POST":
        print('fuck you login')

        postBody = request.body
        json_result = json.loads(postBody)
        username = json_result['username']
        password = json_result['passward']
        print("=>", username, password)

        user = Users.objects.get(username=username)
        if user.username == username and user.passward == password:
            print("FUCK YOUS")

            session_id = request.session.get(username)
            request.session[username] = username
            print("==>", session_id)
            request.session['username'] = username
            request.session['passwd'] = password
            res_dict = dict(
                status =1,
                session_id = session_id
            )
            return redirect('/api/user/')
            #return HttpResponse("登录成功")
        else:
            res_dict = dict(
                status = 0
            )
            return JsonResponse(res_dict)

def user(request):
    username = request.session['username']
    res_dict = dict(
        status = 1,
        username = username
    )
    return JsonResponse(res_dict)

def save(request):
    # 首先检查是否登录
    #username = request.session['username']
    title = request.GET.get('title')
    content = request.GET.get('content')
    user = request.GET.get('user')
    print("--->",user)
    print("--->",title)
    print("===>",content)
    new_content = UserGen()
    new_content.username = user
    new_content.title = title
    new_content.content = content
    new_content.save()
    res_dict = dict(
        status = 1
    )
    return JsonResponse(res_dict)


def quit(request):
    user = request.GET.get('username')
    print("quit=>",user)
    try:
        request.session.clear()
        status = 2
    except Exception as e:
        status = 3
    res_dict = dict(
        status= status
    )
    return JsonResponse(res_dict)
def queryAll(request):
    status = 0
    user = request.GET.get('username')
    name = request.session['刘正']
    print("session->",name)
    print('查询的用户',user)

    try:
        poem_result = UserGen.objects.all().values_list().filter(username=user)
        #print(poem_result,type(poem_result))
        poem_list = []
        title_list = []
        complete_poen = []
        id_list = []
        for poem in poem_result:
            id,_,content,title = poem
            content = content.replace(' ', '')
            #print(title,content)
            poem = content.replace('，','\n')
            poem = poem.replace('。','\n')
            #poem = re.split('，|。',content)
            #print(content.replace(' ','').split('， 。'))
            #print(title,poem,type(title),type(poem))
            #print(poem)
            #poem.insert(0,title)
            #print(poem)
            # print(id,type(id))
            title_list.append(title)
            poem_list.append(poem)
            complete_poen.append([title,poem])
            id_list.append(id)

        status = 4
    except Exception as e:
        print(e)
        status = 5


    res_dict = dict(
        status = status,
        poem = poem_list,
        title = title_list,
        c_poem = complete_poen,
        id_list = id_list
    )


    #res_dict['poem'] = poem_list
    return JsonResponse(res_dict)

def isave(request):
    if request.method == "POST":
        print("fuck you this is isave")
        postBody = request.body
        json_result = json.loads(postBody)
        p_content = json_result['p_content']
        p_index = json_result['p_index']

        try:
            result = UserGen.objects.get(id=p_index)
            # print(result.title)
            # print(result.content)
            # print('--------------->')
            # print(p_content)

            result.content = p_content
            result.save()
            status = 6

            print(result)
        except Exception as e:
            status = 7
    res_dict = dict(
        status = status
    )
    return JsonResponse(res_dict)

def delrecord(request):
    id = request.GET.get('id')

    print('古诗id->',id)
    try:
        UserGen.objects.get(id=id).delete()
        status = 8
    except Exception as e:
        status = 9
    res_dict = dict(
        status = status
    )
    return JsonResponse(res_dict)
