#Bad O(n^2) sort, should still know this
class BubbleSort:

    #Switches adjacent out of order elements
    #Does so len(arr) times to fully sort
    def bubbleSort(self,arr):
        for _ in range(len(arr)):
            for j in range(len(arr)-1):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
        return arr