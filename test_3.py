from datetime import datetime

# Применить написанный логгер к приложению из любого предыдущего д/з.

class FlatIterator:

    def init(self, list_of_list):
        self.list_of_list = list_of_list
        self.flatten_list = self.flatten(self.list_of_list)
        self.index = 0

    def iter(self):
        return self

    def next(self):
        if self.index < len(self.flatten_list):
            item = self.flatten_list[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

    def flatten(self, lst):
        result = []
        for item in lst:
            if isinstance(item, list):
                result.extend(self.flatten(item))
            else:
                result.append(item)
        return result


def logger(path):
    def decorator(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            with open(path, 'a') as log_file:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_file.write(f"{timestamp} - {old_function.name} called with args: {args}, kwargs: {kwargs}, returned: {result}\n")
            return result
        return new_function
    return decorator


@logger('main.log')
def test_flat_iterator(list_of_lists):
    flatten_iterator = FlatIterator(list_of_lists)
    result = list(flatten_iterator)
    return result


if __name__ == "main":
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    test_flat_iterator(list_of_lists_1)
    test_flat_iterator(list_of_lists_2)