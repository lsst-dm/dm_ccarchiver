"""Sphinx configuration file for TSSW package"""

from documenteer.sphinxconfig.stackconf import build_package_configs
import lsst.dm.CCArchiver
import pkg_resources


_g = globals()
_g.update(build_package_configs(
    project_name='dm_CCArchiver',
    version=pkg_resources.get_distribution('dm_CCArchiver').version
))
