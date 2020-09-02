from django.utils import timezone
from django.views.generic.list import ListView

from .models import Person
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q

class PersonListView(ListView):
    
    model = Person
    paginate_by = 100
    template_name = 'person_list.html'
    queryset = Person.objects.all()
    search_param = None
    row_total = paginate_by
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['search'] = self.search_param
        return context

    def get_queryset(self, *args, **kwargs):
            queryset = super(PersonListView, self).get_queryset(*args, **kwargs)
            
            search_query = self.request.GET.get('search')
            if search_query:
                self.search_param = search_query
                queryset = queryset.filter(
                        Q(name__icontains=search_query)|
                        Q(surname__icontains=search_query)|
                        Q(job__icontains=search_query)|
                        Q(address__icontains=search_query)|
                        Q(email__icontains=search_query)|
                        Q(description__icontains=search_query)
                        ).distinct()
            return queryset
            


    # def get_queryset(self):
    #     qs = super().get_queryset() 
    #     return qs.filter(name__iexact=self.kwargs['name'])
        
    

# def search(request):
#     if request.method == 'POST':      
#         srch = request.POST.get("title")  
        
#         if srch:
#             match = Person.objects.filter(Q(name__contains=srch) |
#                                           Q(surname__contains=srch) |
#                                           Q(job__contains=srch) |
#                                           Q(address__contains=srch) |
#                                           Q(email__contains=srch) |
#                                           Q(description__contains=srch))
#             if match:
#                 return render(request,"search.html",{"sr":match})
#             else:
#                 messages.error(request, 'arama sonucu bulunamadi')
#         else:
#             return HttpResponseRedirect('/search/')

#     return render(request,"search.html")