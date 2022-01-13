#data structures - containers storing data in a specific memory layout
# based on the problem we have to pick the right data structure

#Big O notation
#use to measure how running time or space requirement
#for your program grow as input size grows

# as size of array grows time taken also grows

#array

#linkedlist
class Node:                    #represents individual elements in the LL
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head = None     

    def insert_at_begining(self, data):
        node=Node(data, self.head)      # takes data value and inserts at the beginning of LL
        self.head = node

    def print(self):
        if self.head is None:
            print("linked List is empty")
            return

        itr = self.head
        listr = ''
        
        while itr:
            listr += str(itr.data) + '-->'
            itr = itr.next

        print(listr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 8
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    # def insert_after_values(self, data_after, data_to_insert):
        #search for first occurance of data_after value in linked list
        #now insert data_to_insert after data_after node

    # def remove_by_value(self, data):
    #     #remove first node that containes data

if __name__=='__main__':
    ll = LinkedList()
    # ll.insert_at_begining(5)
    # ll.insert_at_begining(89)
    # ll.insert_at_end(79)
    # ll.print()
    # ll.insert_at_end(5)
    # ll.insert_at_end(89)
    # ll.insert_at_end(79)
    # ll.print()
    # ll.insert_values(["banana","mango","grapes","orange"])
    # ll.print()
    # print("length:",ll.get_length())
    # ll.insert_values(["banana","mango","grapes","orange"])
    # ll.print()
    # ll.remove_at(2)
    # ll.remove_at(-1)
    # ll.print()
    # ll.insert_values(["banana","mango","grapes","orange"])
    # ll.print()
    # ll.insert_at(0,"figs")
    # ll.print()
    # ll.insert_at(2, "jackfruit")
    # ll.print()
    ll.insert_values([45,7,12,567,99])
    ll.insert_at_end(67)
    ll.print()
    ll.remove_at(2)
    ll.print()




