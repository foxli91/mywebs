from django.shortcuts import render, redirect, HttpResponse
# Create your views here.
# 这里是视图的，放html或者直接返回json数据
def user_info(request):
    print(request, type(request))
    # 这里直接返回页面了
    '''
    这里是页面的和SpringBoot的ModelAndView那种模式一样实际开发中很少用
    '''
    return render(request, 'user.html')
def user_list(request):
    '''
    这里是返回文本数据的实际开发中可以返回json数据
    '''
    us_list = [{'name': '赵云', 'level': 14, 'score': 3500000}, {'name': '张飞', 'level': 24, 'score': 13500000}]
    return HttpResponse(us_list)
def home(request):
    return render(request, 'home.html')
def no_auth_redirect(request):
    print('没有权限跳转')
    '''
    这里是进行重定向的
    '''
    redirect('https://www.baidu.com')
    return redirect(to='/home')
