from rest_framework.decorators import api_view
from rest_framework.response import Response
'''
@api_view(['GET'])
def get_book(request):
    book_objs=Book.objects.all()
    serializer=BookSerializer(book_objs,many=True)
    print('hello')
    return Response({'status':200,'payload':serializer.data})
'''

@api_view(['GET','POST'])
def test(request):
    print("A request from nodeMcu")
    return Response({"data":"Hurray!!"})