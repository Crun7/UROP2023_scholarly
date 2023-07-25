from scholarly import scholarly
import re
# From Scriber
# Harvard style: 
#   Books: Author surname, initial. (Year) Book title. City: Publisher.
#   journal: Author surname, initial. (Year) ‘Article title’, Journal Name, Volume(Issue), pp. page range.

# APA style: 
#   Books: Author’s Last Name, Initial(s). (Year of publication). Title of book. Publisher.
#   journal: Author’s Last Name, Initial(s). (Year of publication). Title of article. Title of Journal, Volume(Issue), Pages.

# MLA style: 
#   Books:  Author’s Last Name, First Name. Title of Book. Publisher, Year of publication.
#   journal: Author’s Last Name, First Name. “Title of Article.” Title of Journal, vol. Volume, no. Issue, Month Year of publication, pp. Pages.

def check_paper_exists(citation) -> str:
    # Search for publications with the given title
    title = extract_title(citation)
    search_query = scholarly.search_pubs(title)

    try:
        # Get the first publication from the search results
        pub = next(search_query)
        return pub['bib']['title'].lower()
      
    except StopIteration:
        # If no search results were found, the paper does not exist
        return "NA"

def apa_citation(citation):
    author =  r'[A-Z][a-z]+\,(\s[A-Z]\.)+(\,\s[A-Z][a-z]+\,\s([A-Z]\.)+)*\,\s\&(\s[A-Z][a-z]+\,\s[A-Z]\.)?'
    year   = r'\s\(\d{4}\)\.'
    main_title  = r'(\s(\w+(\s\w+)+)\:)?'
    sub_title = r'\s(\w+(\s\w+)+)\.'
    publisher = r'\s(\w+(\s\w+)+)\,'
    vol_page = r'\s+\d+\(\d+\)\,\s+\d+(-|–)\d+'
    doi = r""


    apa_pattern_without_doi = author + year + main_title + sub_title + publisher + vol_page
    if re.match(apa_pattern_without_doi, citation):
        return True
    else:
        return False
    
def harvard_citation(citation):
    # only single author supported right now 
    author =  r'[A-Z][a-z]+\,(\s[A-Z]\.)+'
    year   = r'\s\(\d{4}\)'
    title = r'\s(\w+(\s\w+)+)\.'
    publisher = r'\s(\w+(\s\w+)+)\,'
    vol_page = r'\s+\d+\(\d+\)\,\spp\.\s+\d+(-|–)\d+'
    
def extract_title(citation):
    if 'pp.' in citation or 'vol.' in citation:
        return extract_journal_title(citation)
    else:
        return extract_book_title(citation)
    

def extract_book_title(citation):
    # find the year of publication
    year_match = re.search(r'\((\d{4})\)', citation)
    
    # check if it's followed by the title (Harvard or APA style).
    if year_match:
        year_index = year_match.end()
        # Extract the title
        title_match = re.search(r'\.\s(.*?)\.\s', citation[year_index:])
        
        if title_match:
            return title_match.group(1)
    
    # If the year is not found then MLA style.
    title_match = re.search(r'\.\s(.*?)\.\s', citation)
    
    if title_match:
        return title_match.group(1)
    
    # error message if title is not found.
    return "Title not found"

def extract_journal_title(citation):
    # find the year of publication
    year_match = re.search(r'\((\d{4})\)', citation)

    # check if it's followed by the title (Harvard or APA style).
    if year_match:
        year_index = year_match.end()
        # Extract the title
        title_match = re.search(r'\.\s(.*?)\,\s', citation[year_index:])
        
        if title_match:
            return title_match.group(1)
    
    # If the year is not found assume MLA style.
    title_match = re.search(r'(\"|“)(.*?)(\"|”)', citation)
    
    # If the title is found, return it.
    if title_match:
        return title_match.group(2)
    
    # error message if title is not found.
    return "Title not found"


# Assume references and citation all starts "Reference" and "Bibliography"
def extract_citations():
    file = input("enter the file name: ")
    with open(file, 'r') as f:
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

# filename = 'test_file.txt'
# citations = extract_citations(filename)

# for citation in citations:
#     print(citation)

# # Test the function with an example citation.
# citation = "Andreff, Wladimir, and Paul D. Staudohar. “The Evolving European Model of Professional Sports Finance.” Journal of Sports Economics, vol. 1, no. 3, Sept. 2000, pp. 257–76, https://doi.org/10.1177/152700250000100304."
# print(extract_journal_title(citation))


# # Test the function with an example citation.
# citation = "Smith, Thomas, and Barbara Michelle Williams. The Citation Manual for Students: A Quick Guide. Wiley, 2020."
# print(extract_book_title(citation))

# print(check_paper_exists(citation))




