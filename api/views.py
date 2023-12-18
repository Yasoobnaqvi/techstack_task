from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductSearchView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        search_query = self.request.query_params.get('search', '')
        return Product.objects.filter(name__icontains=search_query)

class ProductSelectView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.selected = True
        instance.save()
        return Response({'status': 'Product selected successfully'})

class DashboardView(View):
    template_name = 'dashboard.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('dashboard')  # Redirect to your dashboard or home page
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')