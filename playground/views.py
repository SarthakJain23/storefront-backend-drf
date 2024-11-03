import logging

import requests
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView

logger = logging.getLogger(__name__)


class HelloView(APIView):

    @method_decorator(cache_page(5))
    def get(self, request):
        try:
            logger.info("Calling httpbin")
            response = requests.request("GET", "https://httpbin.org/delay/2")
            logger.info("Response received")
            data = response.json()
        except requests.ConnectionError:
            logger.error("Failed to connect to httpbin")
        return render(request, "hello.html", {"name": data})
