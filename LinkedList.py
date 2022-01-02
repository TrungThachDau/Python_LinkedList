from types import NoneType, prepare_class


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class List:
    def __init__(self):
        self.head = None
        self.tail = None
    def printList(self):
        stt = 0
        p = self.head
        kq = "DS["
        while p!= None:
            stt += 1
            if stt ==1:
                kq += " " + str(p.data)
            else:
                kq +=" -> " + str(p.data)
            p=p.next
        kq +=" ]"
        print(kq)

    def addNode(self,data):
        node=Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next=node
            self.tail=node
    def insertNode(self,index,data):
        node=Node(data)
        q = None            #q la nut truoc p
        p = self.head       #p la nut hien tai
        i = 0
        while i < index and p != None:
            i += 1
            q = p
            p = p.next
        if q == None:
            #Them vao dau DS
            node.next=self.head
            self.head = node
            if self.tail == None:
                self.tail = node
        else:
            if p == None:
                #Them vao cuoi DS
                self.tail.next = node
                self.tail = node
            else:
                #Them vao giua DS
                q.next = node
                node.next  = p

    def findNode(self,data):
        p=self.head
        index = 0
        while p!= None and p.data!= data:
            p = p.next
            index += 1
        if p ==None:
            return None
        else:
            return index


    def deleteNode(self,data):
        p = self.head
        q = None
        while p != None and p.data != data:
            q = p
            p = p.next
        if p != None:
            if p == self.head and p == self.tail:
                # Xoa phan tu duy nhat
                self.head = self.tail = None
            elif p == self.head:
                #Xoa pt dau tien
                self.head = self.head.next
            elif p ==self.tail:
                #Xoa pt cuoi
                q.next = None
                self.tail = q
            else:
                #xoa o giua
                q.next = p.next

            del p
    def update(self,index,data):
        p = self.head
        i = 0
        while i < index and p != None:
            i += 1
            p = p.next
        if p != None:
            p.data = data
    def deleteList(self):
        p = self.head
        self.head = self.tail = None
        while p != None:
            tmp = p
            p = p.next
            del tmp


if __name__ == '__main__':
    print("Hello world")
    ds = List()
    print("\n-----------Them tu mang-----------")
    a=[2,3,4,54,53,63,39,13,24,31,0]
    for x in a:
        ds.addNode(x)
    ds.printList()
    print("\n---------- Them 1 phan tu----------")
    print("Nhap phan tu can them: ")
    num = int(input())
    ds.addNode(num)
    print("Nhap phan tu can them: ")
    num = int(input())
    ds.addNode(num)
    ds.printList()
    print("\n-----------Chen them nut-----")
    print("Nhap so can chen: ")
    num = int(input())
    print("Nhap vi tri can chen: ")
    index = int(input())
    ds.insertNode(index,num)
    ds.printList()
    print("\n----------------Tim-------")
    print("\nNhap so can tim: ")
    num = int(input())
    vt = ds.findNode(num)
    print(f"So {num} nam o vi tri {vt}")
    print("------------Xoa---------------")
    print("Nhap so can xoa: ")
    num = int(input())
    ds.deleteNode(num)
    ds.printList()
    print("------------Cap nhat-----------")
    ds.printList()
    print("Nhap vi tri muon cap nhat: ")
    vt = int(input())
    print("Nhap gia tri muon cap nhat: ")
    num = int(input())
    ds.update(vt,num)
    ds.printList()
    print("-------------Xoa DSLK-----------")
    ds.deleteList()
    print("Da xoa xong")
    ds.printList()


