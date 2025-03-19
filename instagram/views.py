from django.db.models import Max, Min, Count, Avg
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from instagram.models import Post
from instagram.serializers import PostModelSerializer  # Faqat bitta import qoldi

# ✅ Post ro‘yxati va yaratish uchun APIView
class PostListOrCreate(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostModelSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PostModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ✅ Post tafsilotlari, yangilash va o‘chirish uchun APIView
class PostDetail(APIView):
    def get(self, request, pk, format=None):
        try:
            post = Post.objects.get(id=pk)
            serializer = PostModelSerializer(post)
            return Response(serializer.data)
        except Post.DoesNotExist:
            return Response({'error': 'Post does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        try:
            post = Post.objects.get(id=pk)
            post.delete()
            return Response({'message': 'Post successfully deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Post.DoesNotExist:
            return Response({'message': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostModelSerializer(post, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk=None):
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostModelSerializer(post, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

# ✅ ViewSet bilan ishlovchi API
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import UpdateTimeLimit

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer  # Faqat bitta serializer ishlatilmoqda
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.action in ['update', 'partial_update']:
            return [UpdateTimeLimit()]
        return super().get_permissions()



from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

# JWT LOGIN
@api_view(['POST'])
@permission_classes([AllowAny])  # Har kim login qila olishi uchun
def jwt_login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)

    return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)


# JWT LOGOUT (faqat frontend tokenni o‘chirishi kerak)
@api_view(['POST'])
def jwt_logout_view(request):
    return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
