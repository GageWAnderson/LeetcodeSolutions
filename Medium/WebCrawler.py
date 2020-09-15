# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

#This is a BFS problem, doing this to make sure I'm ready for the multi-threaded version
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        # Get our starting hostname (q states always http) which we'll need to validate future sites.
        host = 'http://' + startUrl.split('/')[2]
		# Use a queue for a bfs traversal, a set to track the sites we visit.
        q = collections.deque([])
        q.append(startUrl)
        visited = set()
        visited.add(startUrl)
        while q:
            site = q.popleft()
			# For neighboring sites.
            for i in htmlParser.getUrls(site):
			    # if they have the same hostname and haven't been visited, go there.
                if i[:len(host)] == host and i not in visited:
                    visited.add(i)
                    q.append(i)
         # Return the sites we visited.
        return visited