import os
import datetime
import logging
import re

ISSUES_PATH = 'issues/'
ISSUES = []

def preBuild(site):
    """
    Add the list of posts to every page context so we can
    access them from wherever on the site.
    """
    global ISSUES
    
    
    def find(name):
        c = issue.context()
        if not name in c:
            logging.info("No attribute '%s' in Issue %s" % (name, issue.path))
            return ''
        return c.get(name, '')

    for issue in site.pages():
        if issue.context().get('issue_title'):
            issueContext = {}
            issueContext['issue_title'] = find('issue_title')
            issueContext['issue_number'] = find('issue_number')
            issueContext['path'] = issue.path
            try:
                issueContext['publishDate'] = datetime.datetime.strptime(find('publish_date'), '%m-%d-%y')
            except Exception, e:
                logging.warning("Date format not correct for page %s, should be m-d-yy\n%s" % (page.path, e))
            issueContext['banner_image'] = find('banner_image')
            issueContext['issue_link'] = find('issue_link')
            issueContext['banner_image_small'] = find('banner_image_small')
            ISSUES.append(issueContext)
            logging.info("getting issue # %s '%s'" % (issueContext['issue_number'], issueContext['issue_title']))


def preBuildPage(site, page, context, data):
    """
    Add list of issues for every page context
    """
    context['manna'] = 'awesome stuff'
    context['issues'] = ISSUES
    # context.update(ISSUES)

    for issue in ISSUES:
        if  issue["path"] == page.path:
                context.update(issue)

    return context, data
