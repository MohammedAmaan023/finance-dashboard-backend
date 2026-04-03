from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Record
from .serializers import RecordSerializer
from .permissions import IsAdmin, IsAnalyst


from .models import User
from .serializers import UserSerializer

# CREATE
@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdmin])
def create_record(request):
    serializer = RecordSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors)

# READ + FILTER
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAnalyst])
def get_records(request):
    records = Record.objects.filter(user=request.user)

    if request.GET.get('type'):
        records = records.filter(type=request.GET['type'])

    if request.GET.get('category'):
        records = records.filter(category=request.GET['category'])

    if request.GET.get('start'):
        records = records.filter(date__gte=request.GET['start'])

    if request.GET.get('end'):
        records = records.filter(date__lte=request.GET['end'])

    return Response(RecordSerializer(records, many=True).data)

# UPDATE
@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsAdmin])
def update_record(request, pk):
    record = Record.objects.get(id=pk)
    serializer = RecordSerializer(record, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

# DELETE
@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdmin])
def delete_record(request, pk):
    Record.objects.get(id=pk).delete()
    return Response({"msg": "Deleted"})




@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAnalyst])
def dashboard(request):
    records = Record.objects.filter(user=request.user)

    income = sum(r.amount for r in records if r.type == 'income')
    expense = sum(r.amount for r in records if r.type == 'expense')

    category_totals = {}
    for r in records:
        category_totals[r.category] = category_totals.get(r.category, 0) + r.amount

    return Response({
        "total_income": income,
        "total_expense": expense,
        "net_balance": income - expense,
        "category_totals": category_totals,
        "recent": RecordSerializer(records.order_by('-date')[:5], many=True).data
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdmin])
def get_users(request):
    users = User.objects.all()
    return Response(UserSerializer(users, many=True).data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsAdmin])
def update_user(request, pk):
    user = User.objects.get(id=pk)
    user.role = request.data.get('role', user.role)
    user.is_active = request.data.get('is_active', user.is_active)
    user.save()
    return Response(UserSerializer(user).data)

