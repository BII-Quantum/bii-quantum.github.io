import csv

def clean_url(url):
    return url.strip() if isinstance(url, str) else ''

def get_social_icon(url):
    if 'linkedin.com' in url:
        return '\\faLinkedin'
    elif 'twitter.com' in url or 'x.com' in url:
        return '\\faTwitter'
    elif 'youtube.com' in url:
        return '\\faVideo'
    else:
        return '\\faGithub'

# Load the CSV file
table_content = ''  
unique_projects = set()  

with open('AC-bo-hackathon-2024.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    # Iterate over each row in the CSV
    for row in reader:
        project_name = row['Project Name']
        if project_name in unique_projects:
            continue  # Skip this row if the project name repeats

        unique_projects.add(project_name)  
        project_num = row['Project num']
        project_name_escaped = project_name.replace('&', '\\&')  
        github_repo = clean_url(row['Github Repo'])
        social_media = clean_url(row['Link to Social Media Post'])
        video_link = clean_url(row['Link to Video (if recorded)'])

        links = []
        if github_repo:
            links.append(f"\\href{{{github_repo}}}{{\\faGithub}}")
        if social_media:
            links.append(f"\\href{{{social_media}}}{{{get_social_icon(social_media)}}}")
        if video_link:
            links.append(f"\\href{{{video_link}}}{{\\faVideo}}")

        links_str = ' \\, '.join(links)  # Separate links with a small space

        table_content += f"{project_num} & {project_name_escaped} & {links_str} \\\\\n"

print(table_content)
