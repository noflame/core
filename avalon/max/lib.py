'''
Created on 2017.9.26

Standalone helper functions

@author: noflame
'''
import MaxPlus as MP


def unique_namespace(namespace, format="%02d", prefix="", suffix=""):
    unique = prefix + (namespace + format % 1)
    MXS = 'uniqueName "%s" numDigits:%s' % (unique, format[2])
    rel = MP.Core.EvalMAXScript(MXS)
    unique = rel.Get()
    return unique + suffix
