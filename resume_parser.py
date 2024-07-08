import os
import json
from docx import Document

def read_resume(file_path):
    """
    Reads a resume from a .docx file and returns the text content.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    
    doc = Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

def parse_resume(text):
    """
    Parses the text content of a resume and converts it into JSON format.
    """
    lines = text.split('\n')
    resume_data = {
        "name": "",
        "contact_information": "",
        "summary": "",
        "experience": [],
        "education": [],
        "skills": [],
        "certifications": [],
        "projects": []
    }
    
    current_section = None
    for line in lines:
        line = line.strip()
        if line.lower() == "experience":
            current_section = "experience"
            continue
        elif line.lower() == "education":
            current_section = "education"
            continue
        elif line.lower() == "skills":
            current_section = "skills"
            continue
        elif line.lower() == "certifications":
            current_section = "certifications"
            continue
        elif line.lower() == "projects":
            current_section = "projects"
            continue
        elif not resume_data["name"]:
            resume_data["name"] = line
            continue
        elif not resume_data["contact_information"]:
            resume_data["contact_information"] = line
            continue
        elif not resume_data["summary"]:
            resume_data["summary"] = line
            continue
        
        if current_section and line:
            resume_data[current_section].append(line)
    
    return resume_data

def main():
    file_path = input("Enter the path to your resume file (.docx): ").strip('"')
    try:
        resume_text = read_resume(file_path)
        resume_json = parse_resume(resume_text)
        print(json.dumps(resume_json, indent=4))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
