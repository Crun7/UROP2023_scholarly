import re

# def is_apa_citation(citation):
#     author =  r'[A-Z][a-z]+\,(\s[A-Z]\.)+(\,\s[A-Z][a-z]+\,\s([A-Z]\.)+)*\,\s\&(\s[A-Z][a-z]+\,\s[A-Z]\.)?'
#     year   = r'\s\(\d{4}\)\.'
#     main_title  = r'(\s(\w+(\s\w+)+)\:)?'
#     sub_title = r'\s(\w+(\s\w+)+)\.'
#     publisher = r'\s(\w+(\s\w+)+)\,'
#     extra = r'\s+\d+\(\d+\)\,\s+\d+(-|–)\d+'
#     doi = r""


#     apa_pattern_without_doi = author + year + main_title + sub_title + publisher + extra
#     if re.match(apa_pattern_without_doi, citation):
#         return True
#     else:
#         return False




# # Test the function
# citation = "Doe, J., & Smith, J. (2023). An analysis of AI advancements. Journal of Technology Studies, 20(4), 350-375. https://doi.org/10.1234/jts2023.104"
# print(is_apa_citation(citation))  # Should print: True

# citation = "Doe, J., & Smith, J. (2023). An analysis of AI advancements. Journal of Technology Studies, 20(4), 350-375."
# print(is_apa_citation(citation))  # Should print: True

# citation = "Not an APA citation"
# print(is_apa_citation(citation))  # Should print: False

# citation = "Grady, J. S., Her, M., Moreno, G., Perez, C., & Yelinek, J. (2019). Emotions in storybooks: A comparison of storybooks that represent ethnic and racial groups in the United States. Psychology of Popular Media Culture, 8(3), 207–217. https://doi.org/10.1037/ppm0000185"
# print(is_apa_citation(citation))  # Should print: True





# author =  r'[A-Z][a-z]+\,(\s[A-Z]\.)+(\,\s[A-Z][a-z]+\,\s([A-Z]\.)+)*\,\s\&(\s[A-Z][a-z]+\,\s[A-Z]\.)?'
# year   = r'\s\(\d{4}\)\.'
# main_title  = r'(\s([A-Za-z]+(\s[A-Za-z]+)+)\:)?'
# sub_title = r'\s([A-Za-z]+(\s[A-Za-z]+)+)\.'
# publisher = r'\s([A-Za-z]+(\s[A-Za-z]+)+)\,'
# extra = r'\s+\d+\(\d+\)\,\s+\d+(-|–)\d+'
# pp = r"pp." 
# doi = r""
# cit = "Doe, J., & Smith, J. (2023). An analysis of AI advancements. Journal of Technology Studies, 20(4), 350375."
# print(re.match(author + year + main_title + sub_title + publisher + extra, cit))



# vol_page = r'\s+\d+\(\d+\)\,\spp\.\s+\d+(-|–)\d+'
# print(re.match(vol_page, " 5(2), pp. 121–139."))


# import re

# def extract_title(citation):
#     # First, find the year of publication by searching for four digits within parentheses.
#     year_match = re.search(r'\((\d{4})\)', citation)
    
#     # If the year is found, check if it's followed by the title (Harvard or APA style).
#     if year_match:
#         year_index = year_match.end()
#         # Extract the title by finding the text between the year and the next period.
#         title_match = re.search(r'\.\s(.*?)\.\s', citation[year_index:])
        
#         # If the title is found, return it.
#         if title_match:
#             return title_match.group(1)
    
#     # If the year is not found or the title is not found after the year, assume MLA style.
#     # Extract the title by finding the text between the first two periods.
#     title_match = re.search(r'\.\s(.*?)\.\s', citation)
    
#     # If the title is found, return it.
#     if title_match:
#         return title_match.group(1)
    
#     # If no title is found, return an error message.
#     return "Title not found"

# # Test the function with an example citation.
# citation = "Smith, Thomas, and Barbara Michelle Williams. The Citation Manual for Students: A Quick Guide. Wiley, 2020."
# print(extract_title(citation))


import re

def extract_citations(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    citations = []
    collect_citations = False

    for line in lines:
        if 'Reference' in line or 'Bibliography' in line:
            collect_citations = True
            continue
        if collect_citations:
            if line.strip():  # not an empty line
                citation = re.sub('^\d+\.\s*', '', line.strip())
                citations.append(citation)
    return citations

filename = 'test_file.txt'
citations = extract_citations(filename)

for citation in citations:
    print(citation)






