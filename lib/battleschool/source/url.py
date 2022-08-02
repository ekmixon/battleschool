__author__ = 'spencergibb'


from . import Source


class Url(Source):
    """url source handler.
    """

    def type(self):
        return 'url'

    def module_name(self):
        return 'get_url'

    def dest_dir(self, source):
        return self.options.cache_dir

    def module_args(self, source):
        force = "yes" if self.options.update_sources else "no"
        module_args = f'url={source["url"]} dest={self.dest_dir(source)}/{source["name"]} force={force} validate_certs=no '


        if "playbooks" not in source:
            source["playbooks"] = []

        source["playbooks"].append(source["name"])
        return module_args
