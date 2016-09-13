from pyblish import api


class ExtractStarterModel(api.InstancePlugin):
    """Produce a stripped down Maya file from instance

    This plug-in takes into account only nodes relevant to models
    and discards anything else, especially deformers along with
    their intermediate nodes.

    """

    label = "Extract starter model"
    order = api.ExtractorOrder
    hosts = ["maya"]
    families = ["starter.model"]

    def process(self, instance):
        import os
        import datetime

        from maya import cmds
        from pyblish_maya import maintained_selection

        root = instance.context.data["workspaceDir"]
        time = datetime.datetime.now().strftime("%Y-%m-%dT%H-%M-%SZ")
        dirname = os.path.join(root, "private", time, str(instance))
        filename = "%s.ma" % instance

        try:
            os.makedirs(dirname)
        except OSError:
            pass

        path = os.path.join(dirname, filename)

        # Perform extraction
        self.log.info("Performing extraction..")
        with maintained_selection():
            cmds.select(instance, noExpand=True)
            cmds.file(path,
                      force=True,
                      typ="mayaAscii",
                      exportSelected=True,
                      preserveReferences=False,
                      constructionHistory=False)

        # Store reference for integration
        instance.data["privateDir"] = dirname

        self.log.info("Extracted {instance} to {path}".format(**locals()))