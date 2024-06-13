import json

# Step 1: Upload the SARIF file (read from the local file system)
file_path = 'db/database-a632c89dd778-2024-06-07.sarif'
baseline_file_path = 'db/database-b8b8ebcf851d-2017-04-11.sarif'

def extract_baseline():
    '''
    Extract baseline
    :return: list contaning dictionaries for issues
    '''
    with open(baseline_file_path, 'r', encoding='utf-8') as f:
        baseline_data = json.load(f)
    issues = []
    issues_full_list = baseline_data['runs'][0]['tool']['driver']['rules']
    for issue in issues_full_list:
        # print(issue)
        prop = issue['properties']
        if 'security' in prop['tags']: #gets all VULNERABILITIES
            curr_issue = {}
            curr_issue['id'] = issue['id']
            curr_issue['name'] = issue['name']
            curr_issue['shortDescription'] = issue['shortDescription']
            curr_issue['fullDescription'] = issue['fullDescription']
            curr_issue['security-severity'] = float(issue['properties']['security-severity'])
            issues.append(curr_issue)
    return issues

def extract_new(new_file_path: str):
    """
    Extract user's file

    :param new_file_path: user's file uploaded
    :return:
    """
    with open(new_file_path, 'r', encoding='utf-8') as f:
        baseline_data = json.load(f)
    issues = []
    issues_full_list = baseline_data['runs'][0]['tool']['driver']['rules']
    for issue in issues_full_list:
        # print(issue)
        prop = issue['properties']
        if 'security' in prop['tags']:  # gets all VULNERABILITIES
            curr_issue = {}
            curr_issue['id'] = issue['id']
            curr_issue['name'] = issue['name']
            curr_issue['shortDescription'] = issue['shortDescription']
            curr_issue['fullDescription'] = issue['fullDescription']
            curr_issue['security-severity'] = float(issue['properties']['security-severity'])
            issues.append(curr_issue)
    return issues


def compare(baseline, new):
    """

    :param baseline: baseline data
    :param new: user uploaded data
    :return: list of all NEW issues
    """
    new_issues = []
    ids=[]

    for b in baseline:
        ids.append(b['id'])

    for n in new:
        id = n['id']
        if id not in ids:  # NEW ID FOUND --> NEW ISSUE, NOT IN BASELINE
            new_issues.append(n)
    return new_issues




baseline = extract_baseline()
new = extract_new(file_path)

compare(baseline, new)
