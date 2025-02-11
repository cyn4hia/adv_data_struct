class AdvancedDataStructure:
    def __init__(self):
        self.data = []

    def add_element(self, element):
        self.data.append(element)

    def remove_element(self, element):
        if element in self.data:
            self.data.remove(element)

    def get_elements(self):
        return self.data

def main():
    # Create an instance of the AdvancedDataStructure class
    data_structure = AdvancedDataStructure()

    # Add elements to the data structure
    data_structure.add_element(1)
    data_structure.add_element(2)
    data_structure.add_element(3)

    # Remove an element from the data structure
    data_structure.remove_element(2)

    # Get all elements in the data structure
    elements = data_structure.get_elements()
    print(elements)

if __name__ == "__main__":
    main()
