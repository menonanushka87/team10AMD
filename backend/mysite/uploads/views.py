import os
from django.conf import settings
from django.http import JsonResponse
from .models import UploadedFile

def upload_file(request):
    if request.method == 'POST' and request.FILES.get('csvFile') and request.FILES.get('sarifFile'):
        csv_file = request.FILES['csvFile']
        sarif_file = request.FILES['sarifFile']

        # Ensure media directory exists
        media_path = os.path.join(settings.MEDIA_ROOT)
        if not os.path.exists(media_path):
            os.makedirs(media_path)

        # Save uploaded files to the database
        uploaded_csv = UploadedFile.objects.create(file=csv_file)
        uploaded_sarif = UploadedFile.objects.create(file=sarif_file)

        # Example response data with processed results
        response_data = {
            'message': 'Files uploaded successfully',
            'csvFileName': uploaded_csv.file.name,
            'sarifFileName': uploaded_sarif.file.name,
        }
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Both CSV and SARIF files are required'}, status=400)
