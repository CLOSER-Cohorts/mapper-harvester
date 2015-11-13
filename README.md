# mapper-harvester
A small python program to harvest the mapping config files from Mapper.

## How to use

Run default app
```
./app.py
```


Run interactively
``` python
> from harvester import MapperHarvester as MH
> mh = MH()
> mh.config.URL_params = "?study=CLS"
> mh.run()
```

## Config options
| Option | Default | Purpose |
| ------ | ------- | ------- |
| URL | http://mapper.closer.ac.uk/instruments/ | URL of where Mapper is located, including instruments arguements with a trailing slash |
| URL_params | <empty string> | URL variables to limit the instruments selected |
| mapping_file_name | /mapping.txt | Name of Q-V file on Mapper |
| dv_file_name | /dv.txt | Name of V-DV file on Mapper |
| question_topics_file_name | /topic-q.txt | Name of Topic-Q file on Mapper |
| variable_topics_file_name | /topic-v.txt | Name of Topic-V file on Mapper |
| out_path | output/ | Output folder for harvested files |
| mapping_file_out | qvlinking/ | Subfolder for harvested Q-V files. To skip this file set to False. |
| dv_file_out | dvlinking/ | Subfolder for harvested V-DV files. To skip this file set to False. |
| tq_file_out | tqlinking/ | Subfolder for harvested Topic-Q files. To skip this file set to False. |
| tv_file_out | tvlinking/ | Subfolder for harvested Topic-V files. To skip this file set to False. |
