

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .ai_caption import generate_caption
from .models import HouseImage

@api_view(['POST'])
def generate_description(request):
    image = request.FILES['image']
    house_image = HouseImage.objects.create(image=image)
    caption = generate_caption(house_image.image.path)
    house_image.description = caption
    house_image.save()
    return Response({"description": caption, "image_url": house_image.image.url})
