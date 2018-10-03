from django.shortcuts import render,get_object_or_404
from .models import Genre,Author,Audio,Image,Video
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import *
def index(request):#Glavnaya
    author_list=Author.objects.all()
    image_list = Image.objects.all()
    last_audio = Audio.objects.all()
    last_Video = Video.objects.last()
    video_list=Video.objects.all()
    audio_list = Audio.objects.all()
    return render(request, 'index.html', {'author_list':author_list,'video_list':video_list,'audio_list':audio_list,'image_list': image_list, 'last_audio': last_audio, 'object': last_Video})


def index1(request):#Audio


    image_list = Image.objects.all()
    last_audio = Audio.objects.all()
    last_Video = Video.objects.last()

    audio_list = Audio.objects.all()
    return render(request, 'index-1.html', {'audio_list':audio_list,'image_list': image_list, 'audio': last_audio, 'object': last_Video})


class Audio_detail(DetailView):
    model = Audio
    template_name = 'Audio_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Audio_detail, self).get_context_data(**kwargs)
        context['image_list'] = Image.objects.all()
        context['audio'] = Audio.objects.all()
        context['video'] = Video.objects.last()
        return context

class Audio_create(CreateView):
    model = Audio
    fields = '__all__'
    template_name = 'Audio_form.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Audio_create, self).get_context_data(**kwargs)
        context['image_list'] = Image.objects.all()
        context['audio'] = Audio.objects.all()
        context['object'] = Video.objects.last()
        return context


class Audio_update(UpdateView):
    model = Audio
    fields = '__all__'
    template_name = 'Audio_form.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Audio_update, self).get_context_data(**kwargs)
        context['image_list'] = Image.objects.all()
        context['audio'] = Audio.objects.all()
        context['object'] = Video.objects.last()
        return context
class Audio_delete(DeleteView):
    model = Audio
    success_url = reverse_lazy('index')
    template_name = 'Audio_delete.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Audio_delete, self).get_context_data(**kwargs)
        context['image_list'] = Image.objects.all()
        context['audio'] = Audio.objects.all()
        context['object'] = Video.objects.last()
        return context

class Video_create(CreateView):
        model = Video
        fields = '__all__'
        template_name = 'Video_form.html'

        def get_context_data(self, *, object_list=None, **kwargs):
            context = super(Video_create, self).get_context_data(**kwargs)
            context['image_list'] = Image.objects.all()
            context['audio'] = Audio.objects.all()
            context['object'] = Video.objects.last()
            return context


class Video_update(UpdateView):
    model = Video
    fields = '__all__'
    template_name = 'Audio_form.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Video_update, self).get_context_data(**kwargs)
        context['image_list'] = Image.objects.all()
        context['audio'] = Audio.objects.all()
        context['object'] = Video.objects.last()
        return context
class Video_delete(DeleteView):
    model = Video
    success_url = reverse_lazy('index')
    template_name = 'Video_delete.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Video_delete, self).get_context_data(**kwargs)
        context['image_list'] = Image.objects.all()
        context['audio'] = Audio.objects.all()
        context['object'] = Video.objects.last()
        return context




def index2(request):#Video

    image_list = Image.objects.all()
    last_audio = Audio.objects.all()
    last_Video = Video.objects.last()
    video_list = Video.objects.all()
    return render(request, 'index-2.html', {'video_list':video_list,'image_list': image_list, 'audio': last_audio, 'object': last_Video})
class Video_detail(DetailView):
    model = Video
    template_name = 'Video_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Video_detail, self).get_context_data(**kwargs)
        context['image_list'] = Image.objects.all()
        context['audio'] = Audio.objects.all()
        context['object'] = Video.objects.last()
        return context


def index3(request):#Gallery
    last_audio=Audio.objects.all()
    last_Video=Video.objects.last()
    search_query = request.GET.get('search')
    if search_query:
        image_list = Image.objects.filter(name__icontains=search_query)
    else:
        image_list = Image.objects.all()
    return  render(request,'index-3.html',{'image_list':image_list,'audio':last_audio,'object':last_Video})

class Author_list(ListView):#authors

    model = Author
    template_name = 'index-4.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Author_list, self).get_context_data(**kwargs)
        context['image_list']=Image.objects.all()
        context['audio']= Audio.objects.all()
        context['object'] = Video.objects.last()
        return context

class Author_detail(DetailView):
    model = Author
    template_name = 'Author_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Author_detail, self).get_context_data(**kwargs)


        context['image_list'] = Image.objects.all()
        context['audio'] = Audio.objects.all()
        context['object'] = Video.objects.last()
        context['audio_list']=Audio.objects.all().filter(author_id__exact=1)
        return context

class Genre_detail(DetailView):
    model = Genre
    template_name = 'Genre_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Genre_detail, self).get_context_data(**kwargs)
        context['image_list'] = Image.objects.all()
        context['audio'] = Audio.objects.all()
        context['object'] = Video.objects.last()
        return context


def index5(request):
    image_list=Image.objects.all()
    last_audio = Audio.objects.all()
    last_Video = Video.objects.last()


    return render(request,'index-5.html', {'image_list': image_list, 'audio': last_audio, 'object': last_Video})