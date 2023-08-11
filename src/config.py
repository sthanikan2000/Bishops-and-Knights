class Configurations:
    row = 3
    col = 3
    sq_size = 100
    width = row * sq_size
    height = col * sq_size
    # def __init__(self):
    #     self.row = 3
    #     self.col = 3
    #     self.sq_size = 100
    #     self.width = self.row * self.sq_size
    #     self.height = self.col * self.sq_size
    
    def change_dimensions(self,type): # type is whether increase or decrease
        if type == 'increase':
            print('Increasing')
            Configurations.row += 1
            Configurations.col += 1
            Configurations.width = Configurations.row * Configurations.sq_size
            Configurations.height = Configurations.col * Configurations.sq_size
        elif type == 'decrease':
            if Configurations.row > 3:
                Configurations.row -= 1
                Configurations.col -= 1
                Configurations.width = Configurations.row * Configurations.sq_size
                Configurations.height = Configurations.col * Configurations.sq_size
            else:
                print('Cannot decrease further')