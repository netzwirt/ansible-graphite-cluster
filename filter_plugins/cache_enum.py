
def cache_enum(input):

    char = 97 + int(input)
    return chr(char)


class FilterModule(object):
    def filters(self):
        return {
            'cache_enum': cache_enum,
		}