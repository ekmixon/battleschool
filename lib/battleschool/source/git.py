__author__ = 'spencergibb'


from . import Source


class Git(Source):
    """git source handler.
    """

    def type(self):
        return 'git'

    def dest_dir(self, source):
        return f"{self.options.cache_dir}/{source['name']}"

    def module_args(self, source):
        force = "no"
        update = "no"

        if self.options.update_sources:
            update = "yes"
            force = "yes"

        return f"repo={source['repo']} dest={self.dest_dir(source)} force={force} update={update} "
