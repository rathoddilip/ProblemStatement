from functools import reduce


class ProductElement:

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

    def product_element(self, lists):
        """
        product of all the elements of numbers except numbers .
        :param lists:
        :return:
        """
        final_list = []
        for index, element in enumerate(lists):
            final_list.append(reduce(lambda number1, number2: number1 * number2, lists[index + 1:] + lists[:index]))
            index_elements = lists[index + 1:] + lists[:index]
            print(f"product element in list{index_elements} at index {index}")
            print(f"except element is {element}  and new list {final_list} ")
        return final_list


if __name__ == '__main__':
    product = ProductElement()
    listFromUser = product.list_from_user()
    print("final list is ", product.product_element(listFromUser))
