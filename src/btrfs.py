from parse import parse


def parse_list_output(output):
    id_, gen, _top_level, path = parse(
        'ID {:d} gen {:d} top level {:d} path {}', output)
    
    return [(id_, gen, path)]
