from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Final


class FinalListView(View):
    template_name = 'final/final_list.html'
    queryset = Final.objects.all()
    
    def get_queryset(self):
        return self.queryset
    
    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset()}    
        return render(request, self.template_name, context)
    

class FinalView(View):
    template_name = 'final/final_detail.html'
    def get(self, request, id=None, *args, **kwargs):
        context = {}
        
        if id is not None:
            obj = get_object_or_404(Final, id=id)
            context['object'] = obj
        return render(request, self.template_name, context)
    

class MyListView(FinalListView):
    queryset = Final.objects.filter(id=1)
    


def my_fbv(request, *args, **kwargs):
    return render(request, 'about.html', {})