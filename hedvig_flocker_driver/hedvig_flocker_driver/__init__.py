# Copyright 2015 EMC Corporation

from flocker.node import BackendDescription, DeployerType
from hedvig_flocker_driver.hedvigdriver import *

def api_factory(cluster_id, **kwargs):
    return GetHedvigStorageApi(kwargs[u"username"], kwargs[u"password"])

FLOCKER_BACKEND = BackendDescription(
    name=u"hedvig_flocker_driver",
    needs_reactor=False, needs_cluster_id=True,
    api_factory=api_factory, deployer_type=DeployerType.block)
