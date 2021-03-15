import json

from django.core.exceptions import ObjectDoesNotExist
from django.core.serializers import serialize
from django.http.response import JsonResponse
from django.shortcuts import render
from measurement.measures import Area
from measurement.measures import Mass
from measurement.measures import Time
from measurement.measures import Volume
from measurement.measures import Weight
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated

from . import models
from . import seralizers

# from rest_framework.decorators import permission_classes


@api_view(["GET", "POST"])
# @permission_classes([IsAuthenticated])
def productsList(request):
    if request.method == "GET":
        products = models.Product.objects.all()
        products_serializer = seralizers.ProductSerializer(products, many=True)
        return JsonResponse(products_serializer.data, safe=False)

    elif request.method == "POST":
        product_data = JSONParser().parse(request)
        product_serializer = seralizers.ProductSerializer(data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse(product_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(product_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
# @permission_classes([IsAuthenticated])
def productById(request, id):
    try:
        product = models.Product.objects.get(pk=id)
    except models.Product.DoesNotExist:
        return JsonResponse({"message": "The product does not exist"},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        product_serializer = seralizers.ProductSerializer(product)
        return JsonResponse(product_serializer.data)

    elif request.method == "PUT":
        product_data = JSONParser().parse(request)
        product_serializer = seralizers.ProductSerializer(product,
                                                          data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse(product_serializer.data)
        return JsonResponse(product_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        product.delete()
        return JsonResponse(
            {"message": "Product was deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )


@api_view(["GET", "POST", "PUT", "DELETE"])
# @permission_classes([IsAuthenticated])
def productsRatingById(request, uid, pid):
    try:
        product = models.Product.objects.get(pk=pid)
    except models.Product.DoesNotExist:
        return JsonResponse({"message": "The product does not exist"},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        try:
            productRating = models.ProductRating.objects.get(product=pid,
                                                             user=uid)
        except ObjectDoesNotExist:
            return JsonResponse(
                {"message": "The product has not been rated"},
                status=status.HTTP_404_NOT_FOUND,
            )

        productRating_serializer = seralizers.ProductRatingSerializer(
            productRating)
        return JsonResponse(productRating_serializer.data, safe=False)

    elif request.method == "POST":
        productRating_data = JSONParser().parse(request)
        productRating_serializer = seralizers.ProductRatingSerializer(
            data=productRating_data)
        if productRating_serializer.is_valid():
            productRating_serializer.save()
            return JsonResponse(productRating_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(productRating_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        try:
            productRating = models.ProductRating.objects.get(product=pid,
                                                             user=uid)
        except ObjectDoesNotExist:
            return JsonResponse(
                {"message": "The product has not been rated"},
                status=status.HTTP_404_NOT_FOUND,
            )

        productRating_data = JSONParser().parse(request)
        productRating_serializer = seralizers.ProductRatingSerializer(
            productRating, data=productRating_data)
        if productRating_serializer.is_valid():
            productRating_serializer.save()
            return JsonResponse(productRating_serializer.data)
        return JsonResponse(productRating_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        try:
            productRating = models.ProductRating.objects.get(product=pid,
                                                             user=uid)
        except:
            return JsonResponse(
                {"message": "The product has not been rated"},
                status=status.HTTP_404_NOT_FOUND,
            )

        productRating.delete()
        return JsonResponse(
            {"message": "Product Rating was deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )


@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def productsAllRating(request, pid):
    try:
        product = models.Product.objects.get(pk=pid)
    except models.Product.DoesNotExist:
        return JsonResponse({"message": "The product does not exist"},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        try:
            productAllRating = models.ProductRating.objects.filter(
                product_id=pid)
        except ObjectDoesNotExist:
            return JsonResponse(
                {"message": "The product has not been rated"},
                status=status.HTTP_404_NOT_FOUND,
            )
        productAllRating_serializer = seralizers.ProductAllRatingSerializer(
            productAllRating, many=True)
        return JsonResponse(productAllRating_serializer.data, safe=False)


@api_view(["GET", "POST", "PUT", "DELETE"])
# @permission_classes([IsAuthenticated])
def productsMeasurementById(request, pid, mid="00000", units=""):
    try:
        product = models.Product.objects.get(pk=pid)
    except models.Product.DoesNotExist:
        return JsonResponse({"message": "The product does not exist"},
                            status=status.HTTP_404_NOT_FOUND)

    units = units.split("&")
    print(units, mid)

    if sum([int(i) for i in mid]) != len(units):
        return JsonResponse({"message": "Invalid Request"},
                            status=status.HTTP_400_BAD_REQUEST)

    if request.method == "GET":
        try:
            productMeasurements = models.ProductMeasurements.objects.filter(
                product_measurements_id=pid)
        except ObjectDoesNotExist:
            return JsonResponse(
                {"message": "The product has not been rated"},
                status=status.HTTP_404_NOT_FOUND,
            )

        str_data = serialize("json", productMeasurements)
        json_data = json.loads(str_data)

        data = []
        for record in json_data:
            row = {}
            row["product_measurements"] = record["fields"][
                "product_measurements"]
            row["product_volume"] = record["fields"]["product_volume"]
            row["product_area"] = record["fields"]["product_area"]
            row["product_mass"] = record["fields"]["product_mass"]
            row["product_weight"] = record["fields"]["product_weight"]
            row["product_time"] = record["fields"]["product_time"]

            for i in row.keys():
                if (row[i] is not None) and type(row[i]) != int:
                    row[i] = float(row[i].split(":")[0])

            counter = 0
            if (row["product_volume"] is not None) and int(mid[0]):
                try:
                    row["product_volume"] = eval(
                        "Volume(cubic_meter = row['product_volume']).{unit}".
                        format(unit=units[counter]))
                    counter += 1
                except AttributeError:
                    return JsonResponse(
                        {"message": "Invalid Units Given"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

            if (row["product_area"] is not None) and int(mid[1]):
                try:
                    row["product_area"] = eval(
                        "Area(sq_m = row['product_area']).{unit}".format(
                            unit=units[counter]))
                    counter += 1
                except AttributeError:
                    return JsonResponse(
                        {"message": "Invalid Units Given"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

            if (row["product_mass"] is not None) and int(mid[2]):
                try:
                    row["product_mass"] = eval(
                        "Mass(g = row['product_mass']).{unit}".format(
                            unit=units[counter]))
                    counter += 1
                except AttributeError:
                    return JsonResponse(
                        {"message": "Invalid Units Given"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

            if (row["product_weight"] is not None) and int(mid[3]):
                try:
                    row["product_weight"] = eval(
                        "Weight(g = row['product_weight']).{unit}".format(
                            unit=units[counter]))
                    counter += 1
                except AttributeError:
                    return JsonResponse(
                        {"message": "Invalid Units Given"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

            if (row["product_time"] is not None) and int(mid[4]):
                try:
                    row["product_time"] = eval(
                        "Time(s = row['product_time']).{unit}".format(
                            unit=units[counter]))
                    counter += 1
                except AttributeError:
                    return JsonResponse(
                        {"message": "Invalid Units Given"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

            data.append(row)
        return JsonResponse(data, safe=False)

    elif request.method == "POST":
        productMeasurements_data = JSONParser().parse(request)
        productMeasurements_serializer = seralizers.ProductMeasurementsSerializer(
            data=productMeasurements_data)

        if productMeasurements_serializer.is_valid():
            productMeasurements_serializer.save()
            return JsonResponse(productMeasurements_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(productMeasurements_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        try:
            productMeasurements = models.ProductMeasurements.objects.get(
                product_measurements_id=pid)
        except ObjectDoesNotExist:
            return JsonResponse(
                {"message": "The product has not been rated"},
                status=status.HTTP_404_NOT_FOUND,
            )

        productMeasurements_data = JSONParser().parse(request)
        productMeasurements_serializer = seralizers.ProductMeasurementsSerializer(
            productMeasurements, data=productMeasurements_data)
        if productMeasurements_serializer.is_valid():
            productMeasurements_serializer.save()
            return JsonResponse(productMeasurements_serializer.data)
        return JsonResponse(productMeasurements_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        try:
            productMeasurements = models.ProductMeasurements.objects.filter(
                product_measurements_id=pid)
        except:
            return JsonResponse(
                {"message": "The product has not been rated"},
                status=status.HTTP_404_NOT_FOUND,
            )

        productMeasurements.delete()
        return JsonResponse(
            {"message": "Product Rating was deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )
