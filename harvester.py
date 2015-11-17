from __future__ import division

import json
import sys
import urllib2

from config import MapperConfig


class MapperHarvester(object):
    def __init__(self, config=None):
        self.buf = ""
        self.config = config
        if self.config is None:
            self.config = MapperConfig()

    def run(self):
        instruments = json.loads(urllib2.urlopen(self.config.URL[:-1] + '.json' + self.config.URL_params).read())

        counter = 0
        print '{prefix:30s}'.format(prefix='Prefix'),
        if self.config.mapping_file_out:
            print '{mapping:10s}'.format(mapping='Mapping'),
        if self.config.dv_file_out:
            print '{dv:10s}'.format(dv='DV'),
        if self.config.tq_file_out:
            print '{tq:10s}'.format(tq='Topic-Q'),
        if self.config.tv_file_out:
            print '{tv:10s}'.format(tv='Topic-V'),
        print ""
        for i in instruments:
            print '{prefix:30s}'.format(prefix=i['prefix']),

            if self.config.mapping_file_out:
                self.download(i, self.config.mapping_file_name, self.config.mapping_file_out)

            if self.config.dv_file_out:
                self.download(i, self.config.dv_file_name, self.config.dv_file_out)
                # self.fetch(i['id'], self.config.dv_file_name)
                # print'{dv:10s}'.format(dv=('[x]' if len(self.buf) > 0 else '[ ]')),
                # self.write(i['prefix'], self.config.dv_file_out)

            if self.config.tq_file_out:
                self.download(i, self.config.question_topics_file_name, self.config.tq_file_out)
                # self.fetch(i['id'], self.config.question_topics_file_name)
                # print'{tq:10s}'.format(tq=('[x]' if len(self.buf) > 0 else '[ ]')),
                #self.write(i['prefix'], self.config.tq_file_out)

            if self.config.tv_file_out:
                self.download(i, self.config.variable_topics_file_name, self.config.tv_file_out)
                # self.fetch(i['id'], self.config.variable_topics_file_name)
                # print'{tv:10s}'.format(tv=('[x]' if len(self.buf) > 0 else '[ ]')),
                #self.write(i['prefix'], self.config.tv_file_out)

            self.clear_buf()

            print ""
            sys.stdout.write("Progress: %d%% \r" % (counter * 100 / len(instruments)))
            sys.stdout.flush()

            counter += 1

    def download(self, instrument, file_name, file_out):
        try:
            self.fetch(instrument['id'], file_name)
            zeros = 0
            lines = 0
            for line in self.buf.splitlines():
                lines += 1
                if line.split("\t")[0] == "0":
                    zeros += 1
            print'{result:10s}'.format(
                result=("{0:.0f}".format((1 - (zeros / lines)) * 100 if len(self.buf) > 0 else 0.0) + "%")),
            self.write(instrument['prefix'], file_out)
        except urllib2.URLError:
            print'{result:10s}'.format(result='X'),

    def fetch(self, iid, file_name):
        if file_name[:1] != '/':
            file_name = '/' + file_name

        try:
            self.buf = urllib2.urlopen(self.config.URL + str(iid) + file_name).read()
        except urllib2.HTTPError:
            self.clear_buf()

    def write(self, prefix, relative_out):
        if len(self.buf) > 0:
            with open(self.config.out_path + relative_out + prefix + ".txt", 'w') as f:
                f.write(self.buf)

    def clear_buf(self):
        self.buf = ""

    def dump_buf(self):
        print self.buf
