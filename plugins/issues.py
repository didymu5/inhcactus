
ISSUES_PATH = '/issues'
ISSUES = []

def preBuild(site):
	print site
	return site

def preBuildPage(site, page, context, data):
    """
    Add the list of posts to every page context so we can
    access them from wherever on the site.
    """
    context['issues'] = ISSUES

    print context['issues'] 
    # print context

    # for issue in ISSUES:
    #     if issue['path'] == page.path:
    #         context.update(post)

    return context, data
