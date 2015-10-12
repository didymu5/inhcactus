import os
import datetime
import logging
import re

ISSUES_PATH = 'issues/'
ISSUES = []

Global = {"config": {}, "issues":[]}

def preBuild(site):
    """
    Add the list of posts to every page context so we can
    access them from wherever on the site.
    """
    global ISSUES

    def find(name):
        c = page.context()
        if not name in c:
            logging.info("Missing info '%s' for post %s" % (name, page.path))
            return ''
        return c.get(name, '')
    #^[0-9]*$
    
    for page in site.pages():
        if page.path.startswith(ISSUES_PATH):
            print page.context().get('issue_number')
            if not page.path.endswith('.html'):
                continue
            # print page.path
            issueContext = {}
            issueContext['title'] = find('title')
            issueContext['issue_number'] = find('issue_number')
            issueContext['path'] = page.path
            try:
                issueContext['publishDate'] = datetime.datetime.strptime(find('publish_date'), '%m-%d-%y')
            except Exception, e:
                logging.warning("Date format not correct for page %s, should be m-d-yy\n%s" % (page.path, e))
                continue
            
            ISSUES.append(issueContext)

    # print ISSUES[1]
            

def preBuildPage(site, page, context, data):
    """
    Add list of issues for every page context
    """
    context['issues'] = ISSUES
    
    for issue in ISSUES:
        if  issue["path"] == page.path:
                context.update(issue)

    return context, data
