import os
import json
import re

def parse_file_content(content, file_type, file_year):
    # Regular expression patterns for extracting data
    area_pattern = r"Área:\s*(.+)\s*$"
    author_pattern = r"Autor:\s*(.+)\s*$"
    title_pattern = r"Tese:\s*(.+)\s*$"
    program_pattern = r"Programa de Pós-Graduação:\s*(.+)\s*$"
    ies_pattern = r"IES:\s*(.+)\s*$"
    advisor_pattern = r"Orientador:\s*(.+)\s*$"
    coadvisor_pattern = r"Coorientador:\s*(.+)\s*$"
    research_pattern = r"Pesquisa:\s*(.+)"

    # Split the content by double newlines to separate each record
    records = [record for record in content.split('\n\n') if record.strip()]

    structured_data = []

    for record in records:
        lines = record.split('\n')
        area_of_interest = not lines[0].startswith("NÃO")
        structured_record = {
            "areaOfInterest": area_of_interest, 
            "type": file_type, 
            "year": file_year,
            "research": "Item não pesquisado"  # Default value for research
        }

        for line in lines:
            if re.match(area_pattern, line):
                areas = re.findall(area_pattern, line)
                structured_record["area"] = areas[0].split(' / ')
            elif re.match(author_pattern, line):
                author = re.search(author_pattern, line).group(1)
                structured_record["author"] = author
            elif re.match(title_pattern, line):
                title = re.search(title_pattern, line).group(1)
                structured_record["thesisTitle"] = title
            elif re.match(program_pattern, line):
                program = re.search(program_pattern, line).group(1)
                structured_record["program"] = program
            elif re.match(ies_pattern, line):
                ies = re.search(ies_pattern, line).group(1)
                structured_record["ies"] = ies
            elif re.match(advisor_pattern, line):
                advisor = re.search(advisor_pattern, line).group(1)
                structured_record["advisor"] = advisor
            elif re.match(coadvisor_pattern, line):
                coadvisor = re.search(coadvisor_pattern, line).group(1)
                structured_record["coAdvisor"] = coadvisor
            elif re.match(research_pattern, line):
                research = re.search(research_pattern, line).group(1)
                structured_record["research"] = research

        structured_data.append(structured_record)

    return structured_data

def main():
    input_folder = 'unformatted-files'
    output_file = 'result.json'
    all_data = []

    # Read unformatted files from the folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.json'):
            with open(os.path.join(input_folder, filename), 'r', encoding='utf-8') as file:
                content = file.read()
                # Determine the file type (MH or TP) and year from the filename
                file_type = 'MH' if filename.upper().startswith('MH') else 'TP'
                file_year = filename[-9:-5]  # Assumes year is last 4 characters before '.json'
                structured_data = parse_file_content(content, file_type, file_year)
                all_data.extend(structured_data)

    # Write the unified data to a file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(all_data, outfile, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()
