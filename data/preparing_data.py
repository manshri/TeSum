### =================================================== ###
###          Importing necessary libraries              ###
### =================================================== ###
from bs4 import BeautifulSoup
import requests
import os
import urllib
import urllib.request
import codecs
import re
import sys





def crawling_from_surya():

    # ### =================================================== ###
    # ###                 Define Page Urls                    ###
    # ### =================================================== ###
    # source = {
    # "telangana":"https://www.telugu.suryaa.com/telangana-latest.php?pagination=",
    # "andhra":"https://www.telugu.suryaa.com/andhrapradesh-latest.php?pagination=",
    # "national":"https://telugu.suryaa.com/national-news-in-telugu.php?pagination=",
    # "world":"https://telugu.suryaa.com/international-news-in-telugu.php?pagination=",
    # "cinema":"https://cinema.suryaa.com/latest-cinema-telugu-news.html?pagination="
    # }
    # total_pages = {"telangana":797,"andhra":868,"national":172,"world":29,"cinema":400}
    # ### =================================================== ###


    # ### =================================================== ###
    # ### Creating sub folders for each category
    # ### =================================================== ###
    # for category in source:
    #     if not os.path.exists(category+"/"):
    #         os.mkdir(category+"/")
    #         os.mkdir(category+"/articles/")
    #     elif not os.mkdir.exists(category+"/articles/"):
    #         os.mkdir(category+"/articles/")
    # ### =================================================== ###


    # ### =================================================== ###
    # ###                 Generating Page Urls                ###
    # ### =================================================== ###
    # page_links = {}
    # for category in source:
    #     page_links[category] = []
    #     for i in range(total_pages[category]):
    #         url = source[category] + str(i+1)
    #         page_links[category].append(url)

    #     text_file = category+".txt"
    #     with open(text_file, "w", encoding="utf-8") as fp:
    #         fp.write("\n".join(page_links[category]))
    # ### =================================================== ###


    # ### =================================================== ###
    # ###                 Generating Article Urls             ###
    # ### =================================================== ###
    # article_links = {}
    # for category, page_urls in page_links.items():
    #     article_links[category] = []
    #     index = 0
    #     for link in page_urls:
    #         response = requests.get(link)
    #         soup = BeautifulSoup(response.text,"html.parser")
    #         anchors = soup.findAll('a',attrs = {"class":"media-left"})

    #         for anchor in anchors:
    #             href = anchor.get('href')
    #             article_links[category].append(href)
    #             print("Index = {}\nLink = {}".format(index,href))
    #             index += 1

    #     ###Writing article links into the file
    #     with open(category + ".txt", "w", encoding="utf-8") as fp:
    #         fp.write("\n".join(article_links[category]))
    # ### =================================================== ###


    ### =================================================== ###
    ###              Extracting article content             ###
    ### =================================================== ###
    ### Extracting article contents from article links
    for category in article_links:
        file_name = 1
        for url in article_links[category]:
            soup = BeautifulSoup(urllib.request.urlopen(url).read(), 'html.parser')
            print("Count: {}\tURL: {}".format(file_name,url))

            try:
                title = soup.find('h1',attrs = {"class":"ramabhadra_font_title"})
                with open(category + "articles/"+str(file_name)+".title.txt","w",encoding="utf-8") as fp:
                    title = title.text
                    title = title.strip()
                    fp.write(title)
            except Exception as e:
                print(e)

            try:
                article = soup.find('span',attrs = {"class":"ramabhadra_font_titext"})
                article = article.find('p')
                with open(category + "/articles/"+str(file_name)+".article.txt","w",encoding="utf-8") as fp:
                    article = article.text
                    article = article.strip()
                    fp.write(article)
            except Exception as e:
                print(e)
            file_name += 1
    ### =================================================== ###



def crawling_from_prabha():
    # ### =================================================== ###
    # ###             Generating page links                   ###
    # ### =================================================== ###
    # base_url = "https://www.prabhanews.com/category/latest-news/page/"
    # pages_count = 20085

    # ### Generating the page links
    # page_links = []
    # index = 1
    # while(index<=pages_count):
    #     page_links.append(base_url + str(index))
    #     index += 1
    # ### =================================================== ###


    # ### =================================================== ###
    # ###       Extracting article links from each page       ###
    # ### =================================================== ###
    # ### ======================== ###
    # ### Adjust the page links here
    # page_starting = 0
    # pages_limit = len(page_links)
    # ### ======================== ###

    # article_links = []
    # index = 0
    # for page_link in page_links[page_starting:pages_limit]:
    #     res = requests.get(page_link,allow_redirects=False)
    #     soup = BeautifulSoup(res.text, 'lxml')
    #     anchors = soup.find_all('a',  attrs= {'class':'mh-excerpt-more'})
    #     if anchors is not None:
    #         for anchor in anchors:
    #             link = anchor.get('href')
    #             if link is not None:
    #                 article_links.append(link)
    #                 index += 1
    #                 print(index)
    #                 print(link)
    #     else:
    #         print("{} Not found!".format(page_link))


    # ### Writing all the links to text file
    # with codecs.open("Article_urls.txt","w",encoding="utf-8") as fp:
    #     for link in article_links:
    #         fp.write(link+"\n")
    # ### =================================================== ###


    ### =================================================== ###
    ### Extracting article contents from each article link  ###
    ### =================================================== ###

    ### *************************************************** ###
    ### Define the parameters here
    count = 1
    ending = len(article_links)
    ### *************************************************** ###

    base_folder = "articles/"
    base_title_folder = "titles/"
    if not os.path.exists(base_folder):
        os.mkdir(base_folder)

    if not os.path.exists(base_title_folder):
        os.mkdir(base_title_folder)

    file_no = 1 + (count-1)
    for article_link in article_links[(count-1):ending]:
        res = requests.get(article_link,allow_redirects=False)
        soup = BeautifulSoup(res.text, 'lxml')
        div_content = soup.find('div',  attrs= {'class':'entry-content clearfix'})
        if div_content is not None:
            article_data = div_content.find('p').text
            ### Saving article contents into text file ###
            try:
                with codecs.open(base_folder+"/article."+str(file_no)+".txt","w",encoding="utf-8") as fp:
                    fp.write(article_data)
                div_content = soup.find('header',  attrs= {'class':'entry-header clearfix'})
                try:
                    header = div_content.find('h1')
                    title = ""
                    if header is not None:
                        title = header.text
                        with codecs.open(base_title_folder+"/article."+str(file_no)+".title.txt","w",encoding="utf-8") as fp:
                            fp.write(title)
                except:
                    print("Title for {} not found".format(article_link))
                print("Count = {}\nLink = {}".format(file_no,article_link))
                file_no += 1
            except Exception as e:
                print(e)
        else:
            print("{} Not found!".format(article_link))
    ### =================================================== ###




def crawling_from_vaartha():


    # ### ===================================================== ###
    # ###                     Helper Functions                  ###
    # ### ===================================================== ###
    # ### Method to retrieve the article links using page links ###
    # def get_previous_link(url):
    #     '''
    #     This function is responsible to extract the previous page
    #     link given the next page (extract the page links from end
    #     to begining)
    #     Input:
    #         @url : end page url of this website
    #     Output:
    #         url of the previous page given next page.
    #     '''
    #     res = requests.get(url)
    #     try:
    #         soup = BeautifulSoup(res.text, 'lxml')
    #         res = soup.find('div',  attrs= {'id':'content'})
    #         if res is not None:
    #             next_link = res.findAll('li', attrs={'class':'previous'})
    #             try:
    #                 for link in next_link:
    #                     try:
    #                         ref = link.find('a')
    #                         return ref.get('href')
    #                     except Exception as e:
    #                         print(e)
    #                         return ""
    #             except Exception as e:
    #                 print(e)
    #                 return "exit"
    #         else:
    #             return "exit"
    #     except Exception as e:
    #         print(e)


    # ### Method to retrieve the article links using page links ###
    # def get_article_urls(page_url):
    #     '''
    #     This function is responsible to extract the article urls
    #     present in the given page url.
    #     Input:
    #         @page_url : page url
    #     Output:
    #         [article_link_1, article_link_2, ..., article_link_n]
    #     '''
    #     res = requests.get(page_url)
    #     articles = []
    #     try:
    #         soup = BeautifulSoup(res.text, 'lxml')
    #         res = soup.find('div',  attrs= {'id':'content'})
    #         if res is not None:
    #             next_link = res.findAll('div', attrs={'class':'entry-content clearfix'})
    #             try:
    #                 for link in next_link:
    #                     try:
    #                         ref = link.find('a')
    #                         try:
    #                             articles.append(ref.get('href'))
    #                         except Exception as e:
    #                             print(e)
    #                     except Exception as e:
    #                         print(e)
    #                 return articles
    #             except Exception as e:
    #                 print(e)
    #                 return articles
    #         else:
    #             return articles
    #     except Exception as e:
    #         print(e)
    #         return articles


    ### Method to retrieve the article links using page links ###
    def get_article_contents(article_url):
        '''
        This function is responsible to extract the article content
        present in the given article url.
        Input:
            @article_url : article url
        Output:
            string: article text in string format
        '''
        res = requests.get(article_url)
        article = ""
        title = ""
        try:
            soup = BeautifulSoup(res.text, 'lxml')
            res = soup.find('div',  attrs= {'id':'content'})
            if res is not None:
                next_link = res.findAll('div', attrs={'class':'entry-content clearfix'})
                
                
                ### =========================================== ###
                ### Extracting the article paragraph content ###
                try:
                    for link in next_link:
                        try:
                            paragraphs = link.findAll('p')
                            if paragraphs is not None:
                                for para in paragraphs:
                                    try:
                                        if para.find('a') is None:
                                            article += para.text
                                    except Exception as e:
                                        print(e)
                                return article
                        except Exception as e:
                            print(e)
                    return article
                except Exception as e:
                    print(e)
                    return article
        except Exception as e:
            print(e)
            return articles        

    ### ===================================================== ###
    ###                 Extracting Page URLs                  ###
    ### ===================================================== ###
    base_url = "https://www.vaartha.com/telangana/page/1/"
    page_links = []
    page_links.append(base_url)

    count = 1
    url = base_url
    print("Count = {}\nLink = {}".format(count,url))
    while(url!="exit"):
        url = get_previous_link(url)
        if(url!=""):
            count += 1
            print("Count = {}\nLink = {}".format(count,url))
            page_links.append(url)

    try:
        with codecs.open("vaartha_page_links.txt","w",encoding="utf-8") as fp:
            for link in page_links:
                fp.write(link+"\n")
    except Exception as e:
        print(e)
    ### ===================================================== ###


    ### ===================================================== ###
    ###                 Article Links Extraction              ###
    ### ===================================================== ###
    ### Crawling article links using page links ###
    article_urls = []
    count = 1
    for page_url in page_links:
        article_links = get_article_urls(page_url)
        if article_links is not None:
            for link in article_links:
                article_urls.append(link)
                print("Count = {}\nLink = {}".format(count,link))
                count += 1

    ### Saving article links into text file ###
    try:
        with codecs.open("vaartha_article_links.txt","w",encoding="utf-8") as fp:
            for link in article_urls:
                fp.write(link+"\n")
    except Exception as e:
        print(e)
    ### ===================================================== ###


    ### ===================================================== ###
    ###                 Article Content Saving                ###
    ### ===================================================== ###

    ### ***************************************************** ###
    ### Define the parameters here
    count = 1
    ending = len(article_urls)
    ### ***************************************************** ###

    base_folder = "articles/"
    if not os.path.exists(base_folder):
        os.mkdir(base_folder)

    file_no = 1 + (count-1)
    try:
        for article in article_urls[(count-1):ending]:
            file_no +=1
            article_data = get_article_contents(article)
            if article_data is not None:
                ### Saving article contents into text file ###
                try:
                    with codecs.open(base_folder + "article."+str(file_no)+".txt","w",encoding="utf-8") as fp:
                        fp.write(article_data)
                except Exception as e:
                    print(e)
                print("Count = {}\nLink = {}".format(count,link))
                count += 1
    except Exception as e:
        print(e)
    ### ===================================================== ###


if __name__ == "__main__":
    if(len(sys.argv)==2):
        if(websitename==1):
            crawling_from_prajasakti()
        elif(websitename==2):
            crawling_from_surya()
        elif(websitename==3):
            crawling_from_prabha()
        elif(websitename==4):
            crawling_from_vaartha()
        else:
            print("\nInvalid website index.")
            print("Hint:\n1 for prajasakti\n2 for surya\n3 for prabha\n4 for vaartha\n")
    else:
        print("Hint:")
        print(">>>python3 crawling_script.py <website_index>")