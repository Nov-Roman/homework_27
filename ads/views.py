import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Ad, Category


def index(request):
    response = {'status': 'ok'}
    return JsonResponse(response, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdView(View):

    def get(self, request):
        ads = Ad.objects.all()

        response = [
            {
                'id': ad.id,
                'author': ad.author,
                'name': ad.name,
                'price': ad.price,
                'description': ad.description,
                'address': ad.address,
                'is_published': ad.is_published
            }
            for ad in ads
        ]

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})

    def post(self, request):
        ad_data = json.loads(request.body)
        ad = Ad.objects.create(**ad_data)

        response = {
                'id': ad.id,
                'author': ad.author,
                'name': ad.name,
                'price': ad.price,
                'description': ad.description,
                'address': ad.address,
                'is_published': ad.is_published
        }

        return JsonResponse(response, json_dumps_params={"ensure_ascii": False})


class AdDetailView(DetailView):
    model = Ad

    def get(self, *args, **kwargs):
        ad = self.get_object()

        response = {
                'id': ad.id,
                'author': ad.author,
                'name': ad.name,
                'price': ad.price,
                'description': ad.description,
                'address': ad.address,
                'is_published': ad.is_published
        }

        return JsonResponse(response, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name='dispatch')
class CategoryView(View):

    def get(self, request):
        """Display all categories"""
        categories = Category.objects.all()

        response = [
            {
                'id': category.id,
                'name': category.name
            }
            for category in categories
        ]

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})

    def post(self, request):
        """Add category to database"""
        category_data = json.loads(request.body)
        category = Category.objects.create(**category_data)

        response = {
                'id': category.id,
                'name': category.name
        }

        return JsonResponse(response, json_dumps_params={"ensure_ascii": False})


class CategoryDetailView(DetailView):
    model = Category

    def get(self, *args, **kwargs):
        category = self.get_object()

        response = {
                'id': category.id,
                'name': category.name
        }

        return JsonResponse(response, json_dumps_params={"ensure_ascii": False})
