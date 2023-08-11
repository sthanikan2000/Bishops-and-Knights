class Dragger:
    
    def __init__(self):
        self.dragging = False
        self.row = None
        self.col = None

    def update_dragger(self, row, col):
        self.row = row
        self.col = col
