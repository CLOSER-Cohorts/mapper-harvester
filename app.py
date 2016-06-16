#!/usr/bin/python

from harvester import MapperHarvester
from config import  MapperConfig as MC

if __name__ == '__main__':
    mh = MapperHarvester()
    #mh.config.URL_params = "?study=ALSPAC"
    #mh.run()

    #mh.config.URL_params = "?study=CLS"
    #mh.clear_buf()
    #mh.run()

    #mh.config.URL_params = "?study=SOTON"
    #mh.clear_buf()
    #mh.run()

    mh.config.URL_params = "?study=NSHD"
    mh.config.mapping_file_out = mh.config.dv_file_out = mh.config.tq_file_out = mh.config.tv_file_out = False
    mh.config.questions_file_out = MC.questions_file_out
    mh.config.variables_file_out = MC.variables_file_out
    #mh.clear_buf()
    #mh.run()

    #mh.config.URL_params = "?study=US"
    #mh.clear_buf()
    mh.run()
