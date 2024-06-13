from django.shortcuts import render
from django.http import JsonResponse

def upload_file(request):
    if request.method == 'POST' and request.FILES.get('csvFile') and request.FILES.get('sarifFile'):
        csv_file = request.FILES['csvFile']
        sarif_file = request.FILES['sarifFile']
        
        # Process the uploaded files here (e.g., save to database, analyze data)
        # Example: Save files to the media folder
        with open('media/' + csv_file.name, 'wb+') as destination:
            for chunk in csv_file.chunks():
                destination.write(chunk)

        with open('media/' + sarif_file.name, 'wb+') as destination:
            for chunk in sarif_file.chunks():
                destination.write(chunk)

        # Example: Perform some processing on the uploaded files
        # For demonstration, just echoing the filenames in response
        response_data = {
            'message': 'Files uploaded successfully',
            'csvFileName': csv_file.name,
            'sarifFileName': sarif_file.name,
        }
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Both CSV and SARIF files are required'}, status=400)
