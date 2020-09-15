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

#This seems a lot like a graph-traversal problem
#Maybe BFS, different searches occur at the same time on different threads, share a seen() set
#Also, I have no idea how to do this Multi-Threaded stuff in Python, I guess this is time to learn!


from threading import Thread
from threading import Lock
#I have the right idea, now I need to know how to implement it in Python
class SolutionReference:
    def __init__(self):
        self.lock = Lock()
        self.queue = collections.deque()
        self.visited = set()
    
    def extractHostName(self, url):
        return '.'.join(url.split('/')[2].split('.')[1:])    
    
    def downloadUrl(self, curr_url, htmlParser):
        next_urls = htmlParser.getUrls(curr_url)
        
		# Use Lock to protect shared states.
        with self.lock:
            for url in next_urls:
                if url not in self.visited and self.curr_hostname == self.extractHostName(url):
                    self.queue.append(url)
                    self.visited.add(url)  
    
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        """
        :type startUrl: str
        :type htmlParser: HtmlParser
        :rtype: List[str]
        """
        self.queue.append(startUrl)
        self.curr_hostname = self.extractHostName(startUrl)
        self.visited = {startUrl}
        
        while self.queue:
            curr_url = self.queue.popleft()

            threads = list()
			# Add at least first URL from the queue
            threads.append(Thread(target=self.downloadUrl, args=(curr_url, htmlParser)))
			# If there are still URLs in the queue, add to the thread list 
            while self.queue:
                curr_url = self.queue.popleft()
                threads.append(Thread(target=self.downloadUrl, args=(curr_url, htmlParser)))
                
			# Execute this batch of threads
            for thread in threads:
                thread.start()
                
			# Main thread waiting for the above threads to finish
            for thread in threads:
                thread.join()
                
        return list(self.visited)  