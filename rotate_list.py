class RotateList:

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

    def rotate_list(self, lists):
        """
        Rotate a list of n elements to the right by given steps.
        :param lists:
        :return:
        """
        steps = int(input("Enter the steps: "))
        final_list = (lists[-steps:] + lists[:-steps])
        return final_list


if __name__ == '__main__':
    rotate_list = RotateList()
    listFromUser = rotate_list.list_from_user()
    print("final rotated list ", rotate_list.rotate_list(listFromUser))
