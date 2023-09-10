#mdpi scrapper
#purpose = scrape academic articles and journals from mdpi
#co-authors = Darlingson Makuwila and Mphatso Chiomba
#how it works : linkextractor recieves keyword
# produces a url for mdpi
# the link is for search result  with articles
#link extractor then scrapes the page for links of articles on the page
#returning a list of links to articles

#the script then iterates through the list of link
#the script passes each link to page_scrapper

#page scrapper returns a list of info about the article found on the link

#file_writer then writes the list to a file


######################################current issues#########################################################
# the derive url method of class linkExtractor is intended to take keyword(s) and produce the link..it currently does not do anything
# the set_page method of page scrapper is meant to set the page to be scrapped, currently it retrieves a local page on the desktop

# affiliations and abstract have commas...figure out how to write them to csv
# some articles have more than one date, figure out how to extract the publication date
# find the volume and number
import json
import re
from itertools import chain

from bs4 import BeautifulSoup
import requests

class linkExtractor:
    __url_link =''
    __header = headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
    __keyword = ''
    def __init__(self):
        pass
    def get_links(self,keyword):
        self.__keyword =  keyword
        self.__url_link = self.derive_url(keyword)
        result = requests.get(self.__url_link)
        result_doc = BeautifulSoup(result.text,'html.parser')
        number_of_links = self.number_of_results(result_doc)
        links = []
        if number_of_links > 10:
            links_list = self.get_all_links(number_of_links)
            for index in links_list:
                links.append(self.extract_links(index))
        else:
            links = self.extract_links(result_doc)
        links = list(chain.from_iterable(links))
        return links

    def get_all_links(self,number_of_links):
        number_of_pages = 0
        remainder = number_of_links%10
        if not remainder==0:
            number_of_links = number_of_links + (10 - remainder)
            print(number_of_links)
            number_of_pages = number_of_links//10
            print(number_of_pages)
        else:
            number_of_pages = number_of_links//10
        all_links_list = []
        for index in range(1,number_of_pages+1):
            page_num = index
            the_link = self.__url_link+"&page_no="+str(page_num)
            req = requests.get(the_link)
            soup = BeautifulSoup(req.text,'html.parser')
            all_links_list.append(soup)
        return (all_links_list)



    def derive_url(self,keywords):
        # first_part = "https://www.mdpi.com/search?sort=pubdate&page_count=10&year_from=2010&year_to=2022&q="
        first_part = "https://www.mdpi.com/search?sort=pubdate&page_count=10&year_from=2010&year_to=2022&featured=&subjects=&journals=&article_types=&countries=MALAWI&q="
        keywords = keywords.replace(" ", '+')
        full_link = first_part+ keywords
        self.__url_link = full_link
        print(full_link)
        return full_link
    def number_of_results(self,soup):
        pd = soup.find_all('h1')
        a_string = pd[0].text
        number_of_results_list = re.findall(r'\d+', a_string)
        number_of_results = int(number_of_results_list[0])
        return number_of_results
    def extract_links(self,result_doc):
        #first find all articles
        #find_all and select methods return a list
        #iterate through the list and pass to get list method
        articles = result_doc.select(".title-link")
        link_list = []
        for index in range(len(articles)):
            link_list.append(self.get_link(articles[index]))
        return link_list

    def get_link(self,article_block):
        #article block is a beautiful soup tag
        #extract the link directly by passing accessing the href element
        link = article_block['href']
        return link

class page_scrapper:
    __page_url =''
    __header = headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
    __local_page = ''

    def set_page_url(self,page_link):
        self.__page_url = 'https://www.mdpi.com' + page_link

    def getPage(self):
        print(self.__page_url)
        page = requests.get(self.__page_url,headers = self.__header)
        beautiful_soup_page = BeautifulSoup(page.text,'html.parser')
        return beautiful_soup_page

    def scrape_page(self,beautiful_soup_page):
        title = self.get_title(beautiful_soup_page)
        authors = self.get_authors(beautiful_soup_page)
        journal_of_publication = self.get_journal_publication(beautiful_soup_page)
        doi = self.get_doi(beautiful_soup_page)
        publication_date = self.get_publication_date(beautiful_soup_page)
        link_to_article = self.get_link_to_article(beautiful_soup_page)
        special_issue = self.get_special_journal_of_publication(beautiful_soup_page)
        abstract = self.get_abstract(beautiful_soup_page)
        keywords = self.get_keywords(beautiful_soup_page)
        affiliations = self.get_affiliations(beautiful_soup_page)
        volume_number = self.get_volume_number(beautiful_soup_page)
        article_info_list = [title,authors,journal_of_publication,doi,publication_date,link_to_article,special_issue,abstract,keywords,affiliations,volume_number]
        return article_info_list

    def get_title(self, beautiful_soup_page):
        title =beautiful_soup_page.find("h1",class_= "title").text
        title = title.replace('\n',"")
        string_unicode = title
        string_encode = string_unicode.encode("ascii", "ignore")
        string_decode = string_encode.decode()
        return string_decode

    def get_authors(self, beautiful_soup_page):
        authors_tag_list = beautiful_soup_page.find_all('span', class_ ="sciprofiles-link__name")
        authors_list = []
        for index in range(len(authors_tag_list)):
            string_unicode = authors_tag_list[index].text
            string_encode = string_unicode.encode("ascii", "ignore")
            string_decode = string_encode.decode()
            authors_list.append(string_decode)
        authors_list = self.convertlistToString(authors_list)
        return(authors_list)

    def get_doi(self, beautiful_soup_page):
        doi_container =beautiful_soup_page.find("div",class_= "bib-identity")
        doi_anchor =doi_container.find("a")
        doi_link = doi_anchor['href']
        return doi_link

    def get_publication_date(self, beautiful_soup_page):
        publication_history = beautiful_soup_page.find('div',class_ ="pubhistory")
        publication_history = publication_history.find_all("span")
        publication_history_List = []
        for index in range(len(publication_history)):
            publication_history_List.append(publication_history[index].text)
        publication_history_List = self.convertlistToString(publication_history_List)
        return(publication_history_List)

    def get_link_to_article(self, beautiful_soup_page):
        abstract_div = beautiful_soup_page.find("div",class_="art-abstract")
        abstract_link_anchor_tag = abstract_div.find('a')
        if not abstract_link_anchor_tag:
            return None
        else:
            link_to_article = abstract_link_anchor_tag['href']
            link_to_article = 'https://www.mdpi.com' + link_to_article
            return(link_to_article)

    def get_abstract(self, beautiful_soup_page):
        abstract_tag = beautiful_soup_page.find('div', class_='art-abstract')
        abstract_text = abstract_tag.text
        abstract_text = abstract_text.replace('\n',"")
        string_unicode = abstract_text
        string_encode = string_unicode.encode("ascii", "ignore")
        string_decode = string_encode.decode()
        return string_decode

    def get_keywords(self, beautiful_soup_page):
        keywords_div = beautiful_soup_page.find('div',class_='art-keywords')
        if not keywords_div:
            return None
        else:
            keywords_first_span = keywords_div.find('span')
            keywords = keywords_first_span.text
            keywords = keywords.replace('\n',"")
            return keywords

    def get_affiliations(self, beautiful_soup_page):
        affiliations_tags_list = beautiful_soup_page.find_all('div',class_='affiliation-name')
        affiliations_list = []
        for affiliation in affiliations_tags_list:
            affiliations_list.append(affiliation.text)
        affiliations = self.convertlistToString_with_semicolon(affiliations_list)
        affiliations = affiliations.replace('\n',"")
        string_unicode = affiliations
        string_encode = string_unicode.encode("ascii", "ignore")
        string_decode = string_encode.decode()
        affiliations = string_decode
        return affiliations

    def convertlistToString(self,list):
        list_string = ' , '.join([str(item) for item in list])
        return list_string

    def convertlistToString_with_semicolon(self,list):
        list_string = ' ; '.join([str(item) for item in list])
        return list_string

    def get_special_journal_of_publication(self, beautiful_soup_page):
        journal_of_publication_div = beautiful_soup_page.find("div",class_="belongsTo")
        if not journal_of_publication_div:
            return None
        else:
            journal_of_publication = journal_of_publication_div.find('a')
            journal_of_publication = journal_of_publication.text
            return(journal_of_publication)
    def get_journal_publication(self,beautiful_soup_page):
        publisher_div = beautiful_soup_page.find('div',class_='bib-identity')
        if not publisher_div:
            return None
        else:
            publication_tag = publisher_div.find('em')
            publication_name = publication_tag.text
            print(publication_name)
            return publication_name
    def get_volume_number(self,beautiful_soup_page):
        breadcrumb_tags = beautiful_soup_page.find_all('div',class_='breadcrumb__element')
        volume_number_tag = breadcrumb_tags[2]
        volume_number = volume_number_tag.text
        volume_number = volume_number.replace('\n',"")
        print(volume_number)
        return volume_number


class file_writer:
    def __init__(self):
        pass
    def write_to_file(self,article_dictionary):
        #convert the list to a dictionary so that it will be easy to write to the JSON file
        # for index in article_info_list:
        #     # dictionary ={
        #     #     "name" : "sathiyajith",
        #     #     "rollno" : 56,
        #     #     "cgpa" : 8.6,
        #     #     "phonenumber" : "9976770500"
        #     # }
        #     dictionary = {
        #         "title" : article_info_list[0],
        #         "authors" : article_info_list[1],
        #         "publisher" : article_info_list[2],
        #         "doi" : article_info_list[3],
        #         "publication info": article_info_list[4],
        #         "link" : article_info_list[5],
        #     }
        json_object = json.dumps(article_dictionary, indent = 4)
        # Writing to sample.json
        with open("fullsample.json", "a") as outfile:
            outfile.write(json_object)


if __name__ == '__main__':
    def get_publication_year(publication_info):
        publication_info_list = publication_info.split(' , ')
        published_year_info = publication_info_list[-1]
        published_year_info_list = published_year_info.split(':')
        published_date_info = published_year_info_list[-1]
        published_date_info_list  = published_date_info.split(" ")
        published_year = published_date_info_list[-1]
        return published_year
    def create_json_object(article):
        publication_year = get_publication_year(article[4])
        article_info = {
            "title" : article[0],
            "authors" : article[1],
            "journal_of_publication" : article[2],
            "doi" : article[3],
            "publication info": article[4],
            "publication year":publication_year,
            "link" : article[5],
            "special issue" : article[6],
            "abstract" : article[7],
            "keywords" : article[8],
            "affiliations" : article[9],
            "volume number" : article[10]
        }
        return article_info

    keywords_list = ['health','Education', 'Energy', 'Water','Agriculture','climate']
    articles_dictionary = []
    for index in keywords_list:

        linkExtract = linkExtractor()
        links = linkExtract.get_links(index)

        for index in range(len(links)):
            print(links[index])
            page_scrapper_obj= page_scrapper()
            page_scrapper_obj.set_page_url(links[index])
            page = page_scrapper_obj.getPage()
            article_info = page_scrapper_obj.scrape_page(page)
            article_info_json_object = create_json_object(article_info)
            articles_dictionary.append(article_info_json_object)

    filewrite = file_writer()
    filewrite.write_to_file(articles_dictionary)
    # print(article_info)
    # print(articles_dictionary)


#what needs to be done
#write the dataset to a file
#create a list of keywords
#retrieve articles from the keywords
#



#force result page to only load 10 articles, so try to access the other articles from the other pages
#take a look at JSON files, JSON files will ignore the comma
#remove the break line from the title
