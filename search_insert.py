class SearchInsert:

    def list_from_user(self):
        """
        take input from user
        :return:
        """
        lists = []
        size_of_lists = int(input("Enter size of list: "))
        for index in range(0, size_of_lists):
            elements = int(input(f"Enter element at index {index} :"))
            # adding the element
            lists.append(elements)
        return lists

    def search_insert_element(self, lists, target):
        """
        return the target element index number
        :param lists:
        :param target:
        :return:
        """
        if target in lists:
            return lists.index(target)
        else:
            lists.append(target)
            lists.sort()
            return lists.index(target)


if __name__ == '__main__':
    search_element = SearchInsert()
    listFromUser = search_element.list_from_user()
    targetElement = int(input("Enter target element"))
    print("Target element index is: ", search_element.search_insert_element(listFromUser, targetElement))
