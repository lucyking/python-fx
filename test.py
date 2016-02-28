# -*- coding: utf-8 -*-
import sys
import re

NBSP = u'\xA0'

class alpha:
    _space_splitter = re.compile(' {2,}')
    def kkk(self, num):
        self.beta(num)
        return 'show' in 'show '

    def beta(self, num):
        if num < len(sys.path[0]):
            print sys.path[0]
            print type(sys.path[0])
            print type(num)
    def strup(self,char):
        return str.upper(char)


    def string(self,string):
        # print string
        # print [self.strup(i) for i in string.split()]
        return ''.join(string.split('\t'))

    def _process_row(self, row):
        print "NBSP Process"
        if NBSP in row:
            row = row.replace(NBSP, ' ')
        return row.rstrip()

    @classmethod
    def split_row(cls, row):
        return row.split('\t')

    def _process_cell(self, cell):
        if len(cell) > 1 and cell[0] == cell[-1] == '"':
            cell = cell[1:-1].replace('""', '"')
            print "Double"
            # cell = cell[1:-1].replace('"', '')
        return cell.replace('"','')



if __name__ == '__main__':
    k = alpha()


    # print  k.string("a b\t\t\tc")
    # str = u'alphak "'
    # print str[0:len(str)]
    # print str[0:4]
    # if str[0:3] == 'alph':
    #     print str[-1]
    # print (u'a' in str)
    # if '"' in str:
    #     str = str.replace('"','')
    # print str

    cells = [u'', u'applib.click_element', u'accessibility_id="show "']
    row = u"\"    applib.click_element \"\"\"   accessibility_id=\"show \"\n"
    print row
    row = k._process_row(row)
    print row
    cells = [k._process_cell(cell) for cell in k.split_row(row)]
    # for cell in k.split_row(row):
    #     print cell
    #     print k._process_cell(cell)
    print "kkk"
    print cells
    print k._space_splitter.split("     aaa bbb c ")  # delete ' ' N -> {2+} line:25

