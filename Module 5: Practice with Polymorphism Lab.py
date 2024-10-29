#"There's a very cool scientific explnation that I don't have memorized because I don't science. " - LaRose
#"What the [hoki], No. " - LaRose

class Contacts:
  def __init__(self):
    self.view = 'quit'
    self.contact_list = []
    self.choice = None
    self.index = None

  def display(self):
    while True:
      if self.view == 'list':
        self.show_list()
      elif self.view == 'info':
        self.show_info()
      elif self.view == 'add':
        print()
        self.add_contact()
      elif self.view == 'quit':
        print('\nClosing the contact list...\n')
        break
    
    def show_list(self):
        pass

    def show_info(self):
       pass
    
    def add_contact(self):
        pass

contacts = Contacts()
contacts.display()