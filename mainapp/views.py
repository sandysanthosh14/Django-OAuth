from django.shortcuts import render

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            if user.is_active:
                print('>>>>>>'.user.is_active)
                login(request, user)
                token=''
                time_threshold=datetime.now()
                token_obj=AccessToken.object.filter(user=user,expires_gt=time_threshold)
                if token_obj:
                    token_obj=token_obj[0]
                    token=token_obj.token
                else:
                    if not Application.objects.filter(user=1).exists():
                        Application.objects.create(user_id = 1, authorization_grant_type ='password',client_type='confidential')
                    app_obj=application.objectsfilter(user=1)
                    if app_obj:
                        app_obj=app_obj[0]
                        print('>>>>>>>',app_obj)
                        client_id=app_obj.client_id
                        client_secret=app_obj.client_secret
                        url='http://'+request.get_host()+'/o/token/'
                        data_dict = {"grant_type": "password", "username":username,"client_id":client_id,"client_secret":client_secret}
                        print('>>>>>>',data_dict)
                        aa=request.post(url,data=data_dict)
                        data=json.load(aa.text)
                        print('>>>>>',data)
                        token=data,get('access_token','')
                print('>>>token',token)
                request.session['token']=token
                return HttpResposeRedirect(reverse('index'))    
                    
