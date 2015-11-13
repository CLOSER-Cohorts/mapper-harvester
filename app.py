#!/usr/bin/python

from __future__ import division

import json
import sys
import urllib2


class MapperConfig(object):
    URL = 'http://mapper.closer.ac.uk/instruments/'
    mapping_file_name = '/mapping.txt'
    dv_file_name = '/dv.txt'
    question_topics_file_name = '/topic-q.txt'
    variable_topics_file_name = '/topic-v.txt'
    out_path = 'output/'
    mapping_file_out = 'qvlinking/'
    dv_file_out = 'dvlinking/'
    tq_file_out = 'tqlinking/'
    tv_file_out = 'tvlinking/'


class MapperHarvester(object):
    def run(self):
        instruments = json.loads(urllib2.urlopen(MapperConfig.URL[:-1] + '.json').read())

        counter = 0
        print '{prefix:30s}'.format(prefix='Prefix'),
        if MapperConfig.mapping_file_out:
            print '{mapping:10s}'.format(mapping='Mapping'),
        if MapperConfig.dv_file_out:
            print '{dv:10s}'.format(dv='DV'),
        if MapperConfig.tq_file_out:
            print '{tq:10s}'.format(tq='Topic-Q'),
        if MapperConfig.tv_file_out:
            print '{tv:10s}'.format(tv='Topic-V'),
        print ""
        for i in instruments:
            print '{prefix:30s}'.format(prefix=i['prefix']),

            if MapperConfig.mapping_file_out:
                self.fetch(i['id'], MapperConfig.mapping_file_name)
                print'{mapping:10s}'.format(mapping=('[x]' if len(self.buf) > 0 else '[ ]')),
                self.write(i['prefix'], MapperConfig.mapping_file_out)

            if MapperConfig.dv_file_out:
                self.fetch(i['id'], MapperConfig.dv_file_name)
                print'{dv:10s}'.format(dv=('[x]' if len(self.buf) > 0 else '[ ]')),
                self.write(i['prefix'], MapperConfig.dv_file_out)

            if MapperConfig.tq_file_out:
                self.fetch(i['id'], MapperConfig.question_topics_file_name)
                print'{tq:10s}'.format(tq=('[x]' if len(self.buf) > 0 else '[ ]')),
                self.write(i['prefix'], MapperConfig.tq_file_out)

            if MapperConfig.tv_file_out:
                self.fetch(i['id'], MapperConfig.variable_topics_file_name)
                print'{tv:10s}'.format(tv=('[x]' if len(self.buf) > 0 else '[ ]')),
                self.write(i['prefix'], MapperConfig.tv_file_out)

            self.clear_buf()

            print ""
            sys.stdout.write("Progress: %d%% \r" % (counter * 100 / len(instruments)))
            sys.stdout.flush()

            counter += 1

    def fetch(self, id, file_name):
        if file_name[:1] != '/':
            file_name = '/' + file_name

        try:
            self.buf = urllib2.urlopen(MapperConfig.URL + str(id) + file_name).read()
        except urllib2.HTTPError:
            self.clear_buf()

    def write(self, prefix, relative_out):
        if len(self.buf) > 0:
            with open(MapperConfig.out_path + relative_out + prefix + ".txt", 'w') as f:
                f.write(self.buf)

    def clear_buf(self):
        buf = ""

    def dump_buf(self):
        print self.buf


if __name__ == '__main__':
    mh = MapperHarvester()
    mh.run()
