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
        if self.config.questions_file_out:
            print '{q:10s}'.format(q='Questions'),
        if self.config.variables_file_out:
            print '{v:10s}'.format(v='Variables'),
        print ""
        for i in instruments:
            print '{prefix:30s}'.format(prefix=i['prefix']),

            if self.config.mapping_file_out:
                self.download(i, self.config.mapping_file_name, self.config.mapping_file_out, suffix='qvmapping')

            if self.config.dv_file_out:
                self.download(i, self.config.dv_file_name, self.config.dv_file_out, suffix='dv')

            if self.config.tq_file_out:
                self.download(i, self.config.question_topics_file_name, self.config.tq_file_out, 1, 'tqlinking')

            if self.config.tv_file_out:
                self.download(i, self.config.variable_topics_file_name, self.config.tv_file_out, 1, 'tvlinking')

            if self.config.questions_file_out:
                self.download(i, self.config.questions_file_name, self.config.questions_file_out, suffix='questions')

            if self.config.variables_file_out:
                self.download(i, self.config.variables_file_name, self.config.variables_file_out, suffix='variables')

            self.clear_buf()

            print ""
            sys.stdout.write("Progress: %d%% \r" % (counter * 100 / len(instruments)))
            sys.stdout.flush()

            counter += 1

    def download(self, instrument, file_name, file_out, column=0, suffix=''):
        try:
            self.fetch(instrument['id'], file_name)
            zeros = 0
            lines = 0
            for line in self.buf.splitlines():
                lines += 1
                if line.split("\t")[column] == "0":
                    zeros += 1
            print'{result:10s}'.format(
                result=("{0:.0f}".format((1 - (zeros / lines)) * 100 if len(self.buf) > 0 else 0.0) + "%")),
            self.write(instrument['prefix'], file_out, suffix)
        except urllib2.URLError:
            print'{result:10s}'.format(result='X'),
        sys.stdout.flush()

    def fetch(self, iid, file_name):
        if file_name[:1] != '/':
            file_name = '/' + file_name

        try:
            self.buf = urllib2.urlopen(self.config.URL + str(iid) + file_name).read()
        except urllib2.HTTPError:
            self.clear_buf()

    def write(self, prefix, relative_out, suffix=''):
        if len(self.buf) > 0:
            with open(self.config.out_path + relative_out + prefix + ('.' + suffix if len(suffix) > 0 else '') + ".txt",
                      'w') as f:
                f.write(self.buf)

    def clear_buf(self):
        self.buf = ""

    def dump_buf(self):
        print self.buf
