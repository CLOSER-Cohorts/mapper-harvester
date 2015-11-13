class MapperConfig(object):
    URL = 'http://mapper.closer.ac.uk/instruments/'
    URL_params = ''
    mapping_file_name = '/mapping.txt'
    dv_file_name = '/dv.txt'
    question_topics_file_name = '/topic-q.txt'
    variable_topics_file_name = '/topic-v.txt'
    out_path = 'output/'
    mapping_file_out = 'qvlinking/'
    dv_file_out = 'dvlinking/'
    tq_file_out = 'tqlinking/'
    tv_file_out = 'tvlinking/'

    def __init__(self):
        self.URL = MapperConfig.URL
        self.URL_params = MapperConfig.URL_params
        self.mapping_file_name = MapperConfig.mapping_file_name
        self.dv_file_name = MapperConfig.dv_file_name
        self.question_topics_file_name = MapperConfig.question_topics_file_name
        self.variable_topics_file_name = MapperConfig.variable_topics_file_name
        self.out_path = MapperConfig.out_path
        self.mapping_file_out = MapperConfig.mapping_file_out
        self.dv_file_out = MapperConfig.dv_file_out
        self.tq_file_out = MapperConfig.tq_file_out
        self.tv_file_out = MapperConfig.tv_file_out
