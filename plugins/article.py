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
    CURRENT_ISSUE = site.config.get('current_issue')    
    def find(name):
        c = article.context()
        if not name in c:
            logging.info("No attribute '%s' in article %s" % (name, article.path))
            return ''
        return c.get(name, '')
    
    #get list of current_issue
    logging.info('current issue is %s' % CURRENT_ISSUE) 
    for article in site.pages():
        # print re.findall('\/+[0-9]+\/', article.path)
        # get current issue list of article
        if len(re.findall('\/+[0-9]+\/', article.path)):
            if str(CURRENT_ISSUE) in article.path:
                
                currentArticleContext = {}
                currentArticleContext['title'] = find('title')
                currentArticleContext['sub_title'] = find('sub_title')
                currentArticleContext['by_line'] = find('by_line')
                currentArticleContext['publish_date'] = find('publish_date')
                currentArticleContext['headliner'] = find('headliner')
                currentArticleContext['issue_number'] = find('issue_number')
                currentArticleContext['article_thumb'] = find('article_thumb')
                currentArticleContext['order_by'] = find('order_by')

                ARTICLES_CURRENT.append(currentArticleContext)
            

def preBuildPage(site, page, context, data):
    """
    Add list of articles for every page context
    """
    context['articles'] = ARTICLES_CURRENT
    for article in ARTICLES_CURRENT:
        context.update(article)
    
    print context
    return context, data
