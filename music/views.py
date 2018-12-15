#from django.http import Http404
#from django.shortcuts import render , get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Album

# Create your views here.
'''def index(request):
    #return HttpResponse("<h1>Music App </h1>")
    all_albums=Album.objects.all()
    template =loader.get_template('music/index.html')
    context = {
        'all_albums' : all_albums,
    }
    #html=''    
    #for album in all_albums:
     #   url ='/music/'+str(album.id)+'/'
      #  html +='<a href="'+url+'">'+str(album.artist_title)+'</a><br>'
    
   # return HttpResponse(html)
    return HttpResponse(template.render(context,request))


def index(request):   
    all_albums=Album.objects.all()    
    context = {
        'all_albums' : all_albums,
    }    
    return render(request,'music/index.html',context)
    

def  detail(request,album_id):
        album=get_object_or_404(Album , pk=album_id)        
        return render(request,'music/details.html',{'album' : album })


def  favorite(request,album_id):
        album=get_object_or_404(Album , pk=album_id)
        try:
            selected_song=album.song_set.get(pk=request.POST['song'])        
        except (KeyError,Song.DoesNotExist):
            return render(request,'music/details.html',{
                'album' : album ,
                'error_msg':'You did not select a valid song',
                })
        else:
            if selected_song.is_favorite==True :
                selected_song.is_favorite=False
                selected_song.save()
                return render(request,'music/details.html',{
                    'album' : album                  
                    })
            else:
                selected_song.is_favorite=True
                selected_song.save()
                return render(request,'music/details.html',{
                    'album' : album                  
                    })


def  favorite(request,album_id):
        album=get_object_or_404(Album , pk=album_id)
        return render(request,'music/details.html',{
                    'album' : album                  
                    })'''


class IndexView(generic.ListView):
    template_name='music/index.html'
    context_object_name='all_albums'    
    
    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model=Album
    template_name='music/details.html'
    
class AlbumCreate(CreateView):
    model=Album
    fields=['artist','artist_title','gener','album_logo']
    