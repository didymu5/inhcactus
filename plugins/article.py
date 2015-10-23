import os
import datetime
import logging
import re

ARTICLE_PATH = 'issues/'
ARTICLES_ISSUE = []
ARTICLES_CURRENT = []
CURRENT_ISSUE = None;

def preBuild(site):
    """
    Add the list of ARTICLES to every page context so we can
    access them from wherever on the site.
    """
    global ARTICLES_ISSUE
    global ARTICLES_CURRENT
    #\/+[0-9]+\/

    def find(name):
        c = article.context()
        if not name in c:
            logging.info("No attribute '%s' in article %s" % (name, article.path))
            return ''
        return c.get(name, '')
    
    #get list of current_issue

    for article in site.pages():
        # print re.findall('\/+[0-9]+\/', article.path)
        # get current issue list of article
        if len(re.findall('\/+[0-9]+\/', article.path)):

            allArticleContext = {}
            allArticleContext['title'] = find('title')
            allArticleContext['sub_title'] = find('sub_title')
            allArticleContext['by_line'] = find('by_line')
            allArticleContext['publish_date'] = find('publish_date')
            allArticleContext['headliner'] = find('headliner')
            allArticleContext['issue_number'] = int(re.findall('[0-9][0-9]', article.path)[0])
            allArticleContext['article_thumb'] = find('article_thumb')
            allArticleContext['order_by'] = find('order_by')
            ARTICLES_CURRENT.append(allArticleContext)


    sorted(ARTICLES_CURRENT, key=lambda allArticleContext: allArticleContext['order_by'])

    def filterCurrentIssueArticle():

        for article in ARTICLES_CURRENT:
            # print article['title'], article['order_by']
            print 'boo!'

    filterCurrentIssueArticle()

def preBuildPage(site, page, context, data):
    """
    Add list of articles for every page context
    """
    CURRENT_ISSUE = site.config.get('current_issue')
    print CURRENT_ISSUE
    context['current_issue'] = CURRENT_ISSUE
    context['articles'] = ARTICLES_CURRENT
    for article in ARTICLES_CURRENT:
        context.update(article)

    return context, data
