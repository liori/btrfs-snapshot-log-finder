from parse import parse


def parse_list_output(output):
    for line in output.split('\n'):
        id_, gen, _top_level, path = parse(
            'ID {:d} gen {:d} top level {:d} path {}', line)
        
        yield (id_, gen, path)
