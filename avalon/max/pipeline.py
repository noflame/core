import os
import sys
import errno
import importlib
import contextlib

print("befor import MaxPlus")
# from maya import cmds, OpenMaya
from MaxPlus import NotificationCodes, NotificationManager, PathManager
print("after import MaxPlus")

print "pyblish imported"
from pyblish import api as pyblish


from . import lib
from ..lib import logger
from .. import api, io, schema
from ..vendor import six
from ..vendor.Qt import QtCore, QtWidgets


def install(config):
    print(type(config))
    print(dir(config))
    print("module name: %s" %(config.__name__))
    print("module : %s" %(config.__file__))


def uninstall():
    print("uninstall start")
    print("uninstall end")


def load():
    print("")


def create(name, asset, family, options=None, data=None):
    """Create a new instance

    Associate nodes with a subset and family. These nodes are later
    validated, according to their `family`, and integrated into the
    shared environment, relative their `subset`.

    Data relative each family, along with default data, are imprinted
    into the resulting objectSet. This data is later used by extractors
    and finally asset browsers to help identify the origin of the asset.

    Arguments:
        name (str): Name of subset
        asset (str): Name of asset
        family (str): Name of family
        options (dict, optional): Additional options from GUI
        data (dict, optional): Additional data from GUI

    Raises:
        NameError on `subset` already exists
        KeyError on invalid dynamic property
        RuntimeError on host error

    Returns:
        Name of instance

    """

    print("create")


def update(container, version=-1):
    """Update `container` to `version`

    This function relies on a container being referenced. At the time of this
    writing, all assets - models, rigs, animations, shaders - are referenced
    and should pose no problem. But should there be an asset that isn't
    referenced then this function will need to see an update.

    Arguments:
        container (avalon-core:container-1.0): Container to update,
            from `host.ls()`.
        version (int, optional): Update the container to this version.
            If no version is passed, the latest is assumed.

    """
    print("update")


def remove(container):
    """Remove an existing `container` from Maya scene

    Arguments:
        container (avalon-core:container-1.0): Which container
            to remove from scene.

    """
    print("remove")
    print(container)
    print(dir(container))


def publish():
    """Shorthand to publish from within host"""
    import pyblish.util
    return pyblish.util.publish()


def ls():
    """List containers from active Max scene

    This is the host-equivalent of api.ls(), but instead of listing
    assets on disk, it lists assets already loaded in Max; once loaded
    they are called 'containers'
    """

def load(Loader,
         representation,
         name=None,
         namespace=None,
         data=None):
    """Load asset via database

    Arguments:
        Loader (api.Loader): The loader to process in host Maya.
        representation (dict, io.ObjectId or str): Address to representation
        name (str, optional): Use pre-defined name
        namespace (str, optional): Use pre-defined namespace
        data (dict, optional): Additional settings dictionary

    """
    print("load")

    assert representation is not None, "This is a bug"

    if isinstance(representation, (six.string_types, io.ObjectId)):
        representation = io.find_one({"_id": io.ObjectId(str(representation))})

    version, subset, asset, project = io.parenthood(representation)

    assert all([representation, version, subset, asset, project]), (
        "This is a bug"
    )

    context = {
        "project": project,
        "asset": asset,
        "subset": subset,
        "version": version,
        "representation": representation,
    }

    # Ensure data is a dictionary when no explicit data provided
    if data is None:
        data = dict()
    assert isinstance(data, dict), "Data must be a dictionary"

    name = name or subset["name"]
    namespace = namespace or lib.unique_namespace(
        asset["name"] + "_",
        prefix="_" if asset["name"][0].isdigit() else "",
        suffix="_",
    )

    # TODO(roy): add compatibility check, see `tools.cbloader.lib`

    Loader.log.info(
        "Running '%s' on '%s'" % (Loader.__name__, asset["name"])
    )

class Creator():
    pass 


class Loader():
    pass
