import json
import copy

__author__ = 'centimo'


class TagsTree:
    def __init__(self):
        self._data = dict()


    def __eq__(self, other):
        """
        :type other: treeNode_Data
        """
        if not isinstance(other, TagsTree):
            return NotImplemented
        return self._data == other._data


    def __repr__(self):
        return "TagsTree()({0._data! r})".format(self)


    def loads(self, str_in):
        self._data = json.loads(str_in)


    def dumps(self):
        """
        :return: Сериализованную _data в виде строки
        """
        return json.dumps(self._data)


    def clear(self):
        self._data.clear()


    def get(self, keys_list):
        """
        :return: 
        :type keys_list: list
        """

        if not isinstance(keys_list, list):
            return NotImplemented
        temp = self._data
        i = 0
        for key in keys_list:
            temp2 = temp.get(key)
            if temp2 is None:
                break
            else:
                temp = temp2
                i += 1
        return list(temp.get(str('0')).keys()), i


    def add_snippet(self, snippet_id, tags_list):
        if not (isinstance(tags_list, list) & isinstance(snippet_id, str)):
            return NotImplemented
        temp = self._data
        for tag in tags_list:
            temp2 = temp.get(tag)
            if temp2 is None:
                temp.update({tag: {str('0'): {snippet_id: 1}}})
                temp = temp.get(tag)
            else:
                temp2.get(str('0')).update({snippet_id: 1})
            temp = temp2
        return None


    def delete_snippet(self, snippet_id, tags_list):
        if not (isinstance(tags_list, list) & isinstance(snippet_id, str)):
            return NotImplemented
        temp = self._data
        for tag in tags_list:
            temp = temp.get(tag)
            if temp is None:
                return None
            temp.get(str('0')).pop(snippet_id)
        return None
