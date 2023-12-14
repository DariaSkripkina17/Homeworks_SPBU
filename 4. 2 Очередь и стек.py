class Stack:
    """
   Стек — это коллекция, элементы которой получают по принципу «последний вошел, первый вышел»
    """

    def __init__(self):
        self.stack_list = []

    def __len__(self):
        return len(self.stack_list)

    def pop(self):
        """
        Удаляет элемент с вершины стека и возвращает его.
        """
        return self.stack_list.pop()

    def push(self, num: int):
        """
        Операция добавления элемента на вершину стек
        """
        self.stack_list.append(num)

    @property
    def top_element(self):
        """
       Последний добавленный элемент называется верхушкой стека, или «top»,
       и его можно посмотреть с помощью операции «peek», которая
       Возвращает верхний элемент стека, но не удаляет его.
        """
        return self.stack_list[-1]


class Queue:
    """
   Очередь — это коллекция, элементы которой получают по принципу «первый вошел, первый вышел»
    """

    def __init__(self):
        self.queue_list = []

    def __len__(self):
        return len(self.queue_list)

    def dequeue(self):
        """
        Удаляет первый помещенный элемент из очереди и возвращает его.
        Поскольку мы вставляем элементы в начало списка, убирать мы их будем с конца.
        """
        return self.queue_list.pop()

    def enqueue(self, num: int):
        """
        Добавляет элемент в очередь
        """
        self.queue_list.insert(0, num)

    @property
    def last_element(self):
        """
        Последний элемент в очереди
        """
        return self.queue_list[0]

    @property
    def first_element(self):
        """
        Первый элемент в очереди
        """
        return self.queue_list[-1]



