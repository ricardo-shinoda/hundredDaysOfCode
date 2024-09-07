class itemLista:
    def _init_(self, data=0, nextItem=None):
        self.data = data
        self.next = nextItem

    def _repr_(self):
        return '%s => %s' % (self.data, self.next)


class ListaEncadeada:
    def _init_(self):
        self.head = None

    def _repr_(self):
        return ""
