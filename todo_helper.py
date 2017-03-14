import argparse
import os
import datetime
import re

class Item:
    def __init__(self, text, completed):
        self._text = text
        self._completed = completed

class Section:
    def __init__(self, name, items):
        self._name = name
        self._items = items
        
def do_copy(yest, today):
    if not os.path.exists(yest):
        open(today, 'w').close()
    else:
        with open(yest, 'r') as f:
            contents = list(f)
        if contents != None:
            finalContents = [line for line in contents if not line.startswith('x ')]
        with open(today, 'w') as f:
            f.write('\n'.join([n.rstrip() for n in finalContents]))

def parse_file(fileToParse):
    sections = []
    if os.path.exists(fileToParse):
        with open(fileToParse) as f:
            contents = list(f)
    items = []
    section = ''
    for content in contents:
        if content.startswith('##'):
            if (section != ''):
                sections.append(Section(section, items))
            items = []
            matches = re.compile('^##(.*)##$').match(content)
            section = matches.group(1)
        elif content.isspace():
            continue
        else:
            items.append(Item(content[2:] if content.startswith('x ') else content, content.startswith('x ')))
    if section != '':
        sections.append(Section(section, items))
    return sections

def do_cleanup(fileToParse):
    sections = parse_file(fileToParse)
    with open(fileToParse, 'w') as f:
        for section in sections:
            print('##{}##'.format(section._name).rstrip(), file=f)
            for unfinished in [item._text.rstrip() for item in section._items if not item._completed]:
                print(unfinished, file=f)
            for finished in [item._text.rstrip() for item in section._items if item._completed]:
                print('x {}'.format(finished), file=f)
            print('', file=f)


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Utility for managing todo lists')

  rootGroup = parser.add_mutually_exclusive_group()

  copyGroup = rootGroup.add_argument_group('copy')
  copyGroup.add_argument('--yest', help='Filename for yesterday\'s todo')
  copyGroup.add_argument('--today', help='Filename for today\'s todo')
  copyGroup.add_argument('--copy', action='store_true')

  cleanGroup = rootGroup.add_argument_group('clean')
  cleanGroup.add_argument('--clean', action='store_true')
  cleanGroup.add_argument('--file', help='Filename')

  args = parser.parse_args()

  if args.copy:
      do_copy(args.yest, args.today)
  elif args.clean:
      do_cleanup(args.file)

