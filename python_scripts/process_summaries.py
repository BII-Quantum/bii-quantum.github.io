import json
import os

def clean_text(text):
    return text.replace('&', '\\&').replace('%', '\\%').replace('#', '\\#').replace('\_', '\\_').replace('^', '\\textasciicircum{}')#.replace('{', '\\{').replace('}', '\\}').replace('~', '\\textasciitilde{}')

# def gen_summary(input_dir):
#     sections = []
    
#     for filename in os.listdir(input_dir):
#         if filename.endswith(".json"):
#             with open(os.path.join(input_dir, filename), 'r', encoding='utf-8') as file:
#                 data = json.load(file)
#                 # project_number = clean_text(data.get("project_number", "Unknown Project"))
#                 project_name = clean_text(data.get("project_name", "Unknown Project"))
#                 summary = clean_text(data.get("summary", "No summary available."))
#                 video_url = data.get("video_url", "")
                
#                 if video_url:
#                     section_title = f"\\subsection*{{\\href{{{video_url}}}{{{project_name}}}}}"
#                 else:
#                     section_title = f"\\subsection*{{{project_name}}}"
                
#                 section = f"{section_title}\n\n{summary}\n"
#                 sections.append(section)
    
#     print(" ".join(sections))


def gen_summary(input_dir):
    sections = []
    entries = []

    for filename in os.listdir(input_dir):
        if filename.endswith(".json"):
            with open(os.path.join(input_dir, filename), 'r', encoding='utf-8') as file:
                data = json.load(file)
                project_number = clean_text(str(data.get("project_number", "Unknown Project")))
                project_name = clean_text(data.get("project_name", "Unknown Project"))
                summary = clean_text(data.get("summary", "No summary available."))
                video_url = data.get("video_url", "")
                
                entries.append((project_number, project_name, summary, video_url))

    try:
        entries.sort(key=lambda x: int(x[0]))
    except ValueError:
        entries.sort(key=lambda x: x[0])

    for project_number, project_name, summary, video_url in entries:
        title = f"Project {project_number}: {project_name}"
        if video_url:
            section_title = f"\\subsection*{{\\href{{{video_url}}}{{{title}}}}}"
        else:
            section_title = f"\\subsection*{{{title}}}"
        
        section = f"{section_title}\n\n{summary}\n"
        sections.append(section)

    print(" ".join(sections))

    
    
local_json_dir = "_projects/json_summaries"
gen_summary(local_json_dir)
