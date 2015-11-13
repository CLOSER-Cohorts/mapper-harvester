#!/usr/bin/python

from harvester import MapperHarvester

if __name__ == '__main__':
    mh = MapperHarvester()
    mh.config.URL_params = "?study=ALSPAC"
    mh.run()

    mh.config.URL_params = "?study=CLS"
    mh.clear_buf()
    mh.run()

    mh.config.URL_params = "?study=SOTON"
    mh.clear_buf()
    mh.run()

    mh.config.URL_params = "?study=NSHD"
    mh.clear_buf()
    mh.run()

    mh.config.URL_params = "?study=US"
    mh.clear_buf()
    mh.run()
