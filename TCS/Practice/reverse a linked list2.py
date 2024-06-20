class Node:
    def __init__(self, data):
        self.data = data  # Initialize the data of the node
        self.next = None  # Initialize the next pointer of the node to None

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list to None

    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if not self.head:  # If the linked list is empty
            self.head = new_node  # Set the new node as the head
            return
        last_node = self.head  # Start from the head of the linked list
        while last_node.next:  # Traverse to the end of the linked list
            last_node = last_node.next
        last_node.next = new_node  # Append the new node at the end

    def reverse(self):
        prev = None  # Initialize previous pointer to None
        current = self.head  # Start from the head of the linked list
        while current:  # Traverse through the linked list
            next_node = current.next  # Temporarily store the next node
            current.next = prev  # Reverse the current node's pointer
            prev = current  # Move the previous pointer to the current node
            current = next_node  # Move to the next node in the original list
        self.head = prev  # Set the head to the new first element (previously last element)

    def display(self):
        current = self.head  # Start from the head of the linked list
        while current:  # Traverse through the linked list
            print(current.data, end=" -> ")  # Print the data of each node
            current = current.next  # Move to the next node
        print("None")  # Indicate the end of the linked list

if __name__ == "__main__":
    llist = LinkedList()  # Create a new linked list object
    
    # Taking input from the user in the format "1 2 3 4"
    elements = input("Enter the elements of the linked list separated by spaces: ").split()
    for elem in elements:  # Loop through each element in the input
        llist.append(int(elem.strip()))  # Convert to integer and append to the linked list

    print("Original Linked List:")
    llist.display()  # Display the original linked list

    llist.reverse()  # Reverse the linked list

    print("Reversed Linked List:")
    llist.display()  # Display the reversed linked list
