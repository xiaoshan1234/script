import configparser

conf = configparser.ConfigParser()
try:
    conf.read("./ddns.conf")
    sections = conf.sections()
    print(sections)
    ddnsConf = conf.items('ddns')
    print(ddnsConf)
    print(conf["ddn"]["target_host"])
except KeyError as error:
    print("error: connot find ",error)
except configparser.NoSectionError as error:
    print(error)
except Exception as error:
    print(error)