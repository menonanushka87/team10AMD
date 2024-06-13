import os
import json
from django.conf import settings
from django.http import JsonResponse
from .models import UploadedFile
from sarif import loader

def process_files_standalone(csv_filename, sarif_filename):
    sarif_file_path = os.path.join(settings.MEDIA_ROOT, "uploads", sarif_filename)
    file1 = loader.load_sarif_file(os.path.join(os.getcwd(), "database-b8b8ebcf851d-2017-04-11.sarif"))
    file1 = file1.get_records()
    file2 = loader.load_sarif_file(sarif_file_path)
    file2 = file2.get_records()

    def extract_issue_key(issue):
        return (
            issue['Location'],
            issue['Line'],
            issue['Severity'],
            issue['Code'],
            issue['Description']
        )

    issues_file1 = set(map(extract_issue_key, file1))
    issues_file2 = set(map(extract_issue_key, file2))

    
    issues_only_in_file2 = issues_file2 - issues_file1

    results = {
        'issues_only_in_file2': list(issues_only_in_file2),
        'total_issues_in_file2': len(issues_file2)
    }

    return json.dumps(results)

def upload_file(request):
    if request.method == 'POST' and request.FILES.get('csvFile') and request.FILES.get('sarifFile'):
        csv_file = request.FILES['csvFile']
        sarif_file = request.FILES['sarifFile']

        
        media_path = os.path.join(settings.MEDIA_ROOT, "uploads")
        if not os.path.exists(media_path):
            os.makedirs(media_path)

        
        csv_file_path = os.path.join(media_path, csv_file.name)
        sarif_file_path = os.path.join(media_path, sarif_file.name)

        with open(csv_file_path, 'wb+') as destination:
            for chunk in csv_file.chunks():
                destination.write(chunk)

        with open(sarif_file_path, 'wb+') as destination:
            for chunk in sarif_file.chunks():
                destination.write(chunk)

        # Process files
        analysis_results_json = process_files_standalone(csv_file.name, sarif_file.name)
        analysis_results = json.loads(analysis_results_json) 

        return JsonResponse(analysis_results)
    else:
        return JsonResponse({'error': 'Both CSV and SARIF files are required'}, status=400)

        
        
        

    

