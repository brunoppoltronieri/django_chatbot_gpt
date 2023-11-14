from django.shortcuts import render,redirect, get_object_or_404
from django.http import JsonResponse
import openai
#from senha import API_KEY

from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat, Feedbacks, API_KEY

from django.utils import timezone


try:
    openai.api_key = API_KEY.objects.order_by("id")[0].api_key
except:
    openai.api_key = ""

def ask_openai(message):
    response = openai.ChatCompletion.create(
        #model = "gpt-3.5-turbo",
        model = "ft:gpt-3.5-turbo-0613:personal:3-5-turbo-finetune:8DRI7IAr",
        # prompt = message,
        # max_tokens=150,
        # n=1,
        # stop=None,
        # temperature=0.7,

        #Você é um especialista em linguagem de programação C e responde apenas sobre assuntos relacionados a linguagem de programação C.
        messages=[
            {"role": "system", "content": "You are an expert in the C programming language and answer only on topics related to the C programming language."},
            {"role": "user", "content": message},
        ]
    )
    answer = response.choices[0].message.content.strip()
    return answer

# Create your views here.

def chatbot(request):
    chats = Chat.objects.filter(user=request.user)


    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)

        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now)
        chat.save()
        
        chats = Chat.objects.filter(user=request.user)[0]
        print(chats.response)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html', {'chats': chats})


def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('chatbot')
        else:
            error_message = 'Usuário ou senha inválido'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        #email = request.POST['email']email, 
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            try:
                user = User.objects.create_user(username, '',password1)
                user.save()
                auth.login(request, user)
                return redirect('chatbot')
            except:
                error_message = 'Erro ao criar a conta'
            return render(request, 'register.html', {'error_message': error_message})
        else:
            error_message = "As senhas não correspondem" 
            return render(request, 'register.html', {'error_message': error_message})
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def delete_messages(request,score):
    #chat = get_object_or_404(Chat, pk=id)
    chats = Chat.objects.filter(user=request.user)
    #fed = Feedbacks.objects.all()
    #fed.delete()
    try:
        message_group = int(Feedbacks.objects.order_by("-message_group")[0].message_group)
    except:
        message_group = 0
    for chat in chats:
        feedback = Feedbacks(user_id=chat.user_id, chat_id=chat.id, message=chat.message, response=chat.response, created_at=chat.created_at, message_group=(message_group+1), approved=score)
        feedback.save()
    chats.delete()
    return redirect('chatbot')