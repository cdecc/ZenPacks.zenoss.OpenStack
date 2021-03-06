###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2011, Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 or (at your
# option) any later version as published by the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################

from Products.ZenUtils.Ext import DirectRouter, DirectResponse
from Products import Zuul


class OpenStackRouter(DirectRouter):
    def _getFacade(self):
        return Zuul.getFacade('openstack', self.context)

    def addOpenStack(self, device_name, username, api_key, project_id, auth_url,
                     region_name=None, collector='localhost'):

        facade = self._getFacade()
        success, message = facade.addOpenStack(
            device_name, username, api_key, project_id, auth_url,
            region_name=region_name, collector=collector)

        if success:
            return DirectResponse.succeed(jobId=message)
        else:
            return DirectResponse.fail(message)

    def getRegions(self, username, api_key, project_id, auth_url, collector):
        facade = self._getFacade()

        data = facade.getRegions(username, api_key, project_id, auth_url, collector)
        return DirectResponse(success=True, data=data)
