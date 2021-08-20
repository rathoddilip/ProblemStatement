import fileinput


class ValueCount:

    def get_char_count(self, paragraph):
        """
        will return count of char in paragraph
        :param paragraph:
        :return:
        """
        all_char_freq_dict = {}
        in_lowercase_para = paragraph.lower()
        remove_white_space_paragraph = in_lowercase_para.replace(" ", "")
        print("after removing white space paragraph:", remove_white_space_paragraph)
        for char in remove_white_space_paragraph:
            if char in all_char_freq_dict:
                all_char_freq_dict[char] += 1
            else:
                all_char_freq_dict[char] = 1
        return all_char_freq_dict

    def get_a_an_word_count(self, paragraph):
        """
        will get indefinite word dictionary and definite word dictionary
        :param paragraph:
        :return:
        """

        definite_dict = {}
        indefinite_dict = {}
        all_freq_dict = {}

        counts = all_freq_dict
        counts_indefinite = indefinite_dict
        counts_definite = definite_dict
        in_lowercase_words = paragraph.lower()
        words = in_lowercase_words.split()

        for word in words:
            if word == 'a':
                if word in counts_indefinite:
                    counts_indefinite[word] += 1
                else:
                    counts_indefinite[word] = 1
            elif word == 'an':
                if word in counts_indefinite:
                    counts_indefinite[word] += 1
                else:
                    counts_indefinite[word] = 1
            elif word == 'the':
                if word in counts_definite:
                    counts_definite[word] += 1
                else:
                    counts_definite[word] = 1
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1

        print("frequency of indefinite word dictionary: ", indefinite_dict)
        print("frequency of definite word dictionary: ", definite_dict)
        print("frequency of each word dictionary : ", all_freq_dict)


if __name__ == "__main__":
    value_count = ValueCount()
    paragraph = "a school in our neighbourhood was closed. Once I saw such an example and there was one s" \
                "chool in the area when I checked, but the authir introduced the indefinite article instead " \
                "of the. On the other hand I see autiomatically the introduction of the definite article" \
                " the school in our area was closed or a Starbucks on Downing stree t was closed Let’s eat" \
                " lunch in an hour"

    print("all character count in paragraph: ", value_count.get_char_count(paragraph))
    print("-------------------------------------------------------------------------------------------------------")
    value_count.get_a_an_word_count(paragraph)
