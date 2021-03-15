import json
from django.shortcuts import render
from django.http.response import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
#from rest_framework.decorators import permission_classes

from django.core.serializers import serialize 
from measurement.measures import Volume, Area, Mass, Time, Weight 
from . import models
from . import seralizers

@api_view(['GET', 'POST'])
#@permission_classes([IsAuthenticated])
def productsList(request):
    if request.method == 'GET':
        products = models.Product.objects.all()
        products_serializer = seralizers.ProductSerializer(products, many=True)
        return JsonResponse(products_serializer.data, safe=False)

    elif request.method == 'POST':
        product_data = JSONParser().parse(request) 
        product_serializer = seralizers.ProductSerializer(data=product_data)
        if product_serializer.is_valid(): 
            product_serializer.save()
            return JsonResponse(product_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
#@permission_classes([IsAuthenticated])
def productById(request, id):
    try: 
        product = models.Product.objects.get(pk=id) 
    except models.Product.DoesNotExist: 
        return JsonResponse({
            'message': 'The product does not exist'
            }, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        product_serializer = seralizers.ProductSerializer(product) 
        return JsonResponse(product_serializer.data) 
    
    elif request.method == 'PUT': 
        product_data = JSONParser().parse(request) 
        product_serializer = seralizers.ProductSerializer(product, data=product_data) 
        if product_serializer.is_valid(): 
            product_serializer.save() 
            return JsonResponse(product_serializer.data) 
        return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        product.delete() 
        return JsonResponse({'message': 'Product was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
#@permission_classes([IsAuthenticated])
def productsRatingById(request, uid, pid):
    try: 
        product = models.Product.objects.get(pk=pid) 
    except models.Product.DoesNotExist: 
        return JsonResponse({
            'message': 'The product does not exist'
            }, status=status.HTTP_404_NOT_FOUND)  
 
    if request.method == 'GET':
        try: 
            productRating = models.ProductRating.objects.get(product=pid, user=uid) 
        except ObjectDoesNotExist: 
            return JsonResponse({
            'message': 'The product has not been rated'
            }, status=status.HTTP_404_NOT_FOUND)  
         
        productRating_serializer = seralizers.ProductRatingSerializer(productRating) 
        return JsonResponse(productRating_serializer.data, safe=False) 
    
    elif request.method == 'POST':
        productRating_data = JSONParser().parse(request) 
        productRating_serializer = seralizers.ProductRatingSerializer(data=productRating_data)
        if productRating_serializer.is_valid(): 
            productRating_serializer.save()
            return JsonResponse(productRating_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(productRating_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT': 
        try: 
            productRating = models.ProductRating.objects.get(product=pid,user=uid) 
        except ObjectDoesNotExist: 
            return JsonResponse({
            'message': 'The product has not been rated'
            }, status=status.HTTP_404_NOT_FOUND)  

        productRating_data = JSONParser().parse(request) 
        productRating_serializer = seralizers.ProductRatingSerializer(productRating, data=productRating_data) 
        if productRating_serializer.is_valid(): 
            productRating_serializer.save() 
            return JsonResponse(productRating_serializer.data) 
        return JsonResponse(productRating_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    elif request.method == 'DELETE':
        try: 
            productRating = models.ProductRating.objects.get(product=pid,user=uid) 
        except: 
            return JsonResponse({
            'message': 'The product has not been rated'
            }, status=status.HTTP_404_NOT_FOUND)  

        productRating.delete() 
        return JsonResponse({'message': 'Product Rating was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
#@permission_classes([IsAuthenticated])
def productsMeasurementById(request, pid):
    try: 
        product = models.Product.objects.get(pk=pid) 
    except models.Product.DoesNotExist: 
        return JsonResponse({
            'message': 'The product does not exist'
            }, status=status.HTTP_404_NOT_FOUND)  
 
    if request.method == 'GET':
        try: 
            productMeasurements = models.ProductMeasurements.objects.filter(product_measurements_id=pid)
        except ObjectDoesNotExist: 
            return JsonResponse({
            'message': 'The product has not been rated'
            }, status=status.HTTP_404_NOT_FOUND)  

        # productMeasurements_serializer = seralizers.ProductMeasurementsListSerializer(productMeasurements.values(), many=True)
        # return JsonResponse(productMeasurements_serializer.data, safe=False)

        # data = []
        # for pm_obj in productMeasurements:
        #      row = {}
        #      row['product_volume'] = seralizers.ProductMeasurementsSerializer(pm_obj, many=True)
        #      data.append(row)
        # return JsonResponse(data, safe=False)

        str_data = serialize('json', productMeasurements) 
        data = json.loads(str_data)
        return JsonResponse(data, safe=False)

        # data = []
        # for pm_obj in productMeasurements.values():
        #      row = {}
        #      row['id'] = pm_obj['product_measurements_id']
        #      #row['product_volume'] = Volume(cubic_meter = 1).cubic_meter
        #      #row['product_volume'] = pm_obj['product_volume'].cubic_meter
        #      row['product_volume'] = pm_obj['product_volume']
             
        #      data.append(row)
        # return JsonResponse(data, safe=False)
    
    elif request.method == 'POST':
        productMeasurements_data = JSONParser().parse(request) 
        productMeasurements_serializer = seralizers.ProductMeasurementsSerializer(data=productMeasurements_data)
        if productMeasurements_serializer.is_valid(): 
            productMeasurements_serializer.save()
            return JsonResponse(productMeasurements_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(productMeasurements_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT': 
        try: 
            productMeasurements = models.ProductMeasurements.objects.filter(product_measurements_id=pid).in_bulk()
        except ObjectDoesNotExist: 
            return JsonResponse({
            'message': 'The product has not been rated'
            }, status=status.HTTP_404_NOT_FOUND)  

        productMeasurements_data = JSONParser().parse(request) 
        productMeasurements_serializer = seralizers.ProductMeasurementsSerializer(productMeasurements, data=productMeasurements_data) 
        if productMeasurements_serializer.is_valid(): 
            productMeasurements_serializer.save() 
            return JsonResponse(productMeasurements_serializer.data) 
        return JsonResponse(productMeasurements_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    elif request.method == 'DELETE':
        try: 
            productMeasurements = models.ProductMeasurements.objects.filter(product_measurements_id=pid).in_bulk()
        except: 
            return JsonResponse({
            'message': 'The product has not been rated'
            }, status=status.HTTP_404_NOT_FOUND)  

        productMeasurements.delete() 
        return JsonResponse({'message': 'Product Rating was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# #@permission_classes([IsAuthenticated])
# def productsMeasurementById(request, pid):
#     try: 
#         product = models.Product.objects.get(pk=pid) 
#     except models.Product.DoesNotExist: 
#         return JsonResponse({
#             'message': 'The product does not exist'
#             }, status=status.HTTP_404_NOT_FOUND)  
 
#     if request.method == 'GET':
#         try: 
#             productMeasurements = models.ProductMeasurements.objects.filter(product_measurements_id=pid).in_bulk() 
#         except ObjectDoesNotExist: 
#             return JsonResponse({
#             'message': 'The product has not been rated'
#             }, status=status.HTTP_404_NOT_FOUND)  
         
#         productMeasurements_serializer = seralizers.ProductMeasurementsSerializer(productMeasurements) 
#         return JsonResponse(productMeasurements_serializer.data, safe=False) 
    
#     elif request.method == 'POST':
#         productMeasurements_data = JSONParser().parse(request) 
#         productMeasurements_serializer = seralizers.ProductMeasurementsSerializer(data=productMeasurements_data)
#         if productMeasurements_serializer.is_valid(): 
#             productMeasurements_serializer.save()
#             return JsonResponse(productMeasurements_serializer.data, status=status.HTTP_201_CREATED) 
#         return JsonResponse(productMeasurements_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'PUT': 
#         try: 
#             productMeasurements = models.ProductMeasurements.objects.filter(product_measurements_id=pid).in_bulk()
#         except ObjectDoesNotExist: 
#             return JsonResponse({
#             'message': 'The product has not been rated'
#             }, status=status.HTTP_404_NOT_FOUND)  

#         productMeasurements_data = JSONParser().parse(request) 
#         productMeasurements_serializer = seralizers.ProductMeasurementsSerializer(productMeasurements, data=productMeasurements_data) 
#         if productMeasurements_serializer.is_valid(): 
#             productMeasurements_serializer.save() 
#             return JsonResponse(productMeasurements_serializer.data) 
#         return JsonResponse(productMeasurements_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
#     elif request.method == 'DELETE':
#         try: 
#             productMeasurements = models.ProductMeasurements.objects.filter(product_measurements_id=pid).in_bulk()
#         except: 
#             return JsonResponse({
#             'message': 'The product has not been rated'
#             }, status=status.HTTP_404_NOT_FOUND)  

#         productMeasurements.delete() 
#         return JsonResponse({'message': 'Product Rating was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
