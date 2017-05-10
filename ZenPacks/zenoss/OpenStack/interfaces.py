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

from Products.Zuul.form import schema
from Products.Zuul.interfaces import IFacade
from Products.Zuul.interfaces import IDeviceInfo
from Products.Zuul.interfaces.component import IComponentInfo
from Products.Zuul.utils import ZuulMessageFactory as _t


class IOpenStackFacade(IFacade):
    def addEndpoint(self, target, email, password, collector):
        """Add OpenStack Endpoint."""


class IEndpointInfo(IDeviceInfo):
    username = schema.TextLine(title=_t(u"Username"))
    project_id = schema.TextLine(title=_t(u"Project ID"))
    auth_url = schema.TextLine(title=_t(u"Auth URL"))
    insecure = schema.TextLine(title=_t(u"Insecure Connection"))
    region_name = schema.TextLine(title=_t(u"Region Name"))
    serverCount = schema.Int(title=_t(u"Total Servers"))
    flavorCount = schema.Int(title=_t(u"Total Flavors"))
    imageCount = schema.Int(title=_t(u"Total Images"))


class IFlavorInfo(IComponentInfo):
    flavorId = schema.TextLine(title=_t(u"Flavor ID"))
    flavorRAMString = schema.TextLine(title=_t(u"Flavor RAM"))
    flavorDiskString = schema.TextLine(title=_t(u"Flavor Disk"))
    serverCount = schema.Int(title=_t(u"Server Count"))


class IImageInfo(IComponentInfo):
    imageId = schema.TextLine(title=_t(u"Image ID"))
    imageStatus = schema.TextLine(title=_t(u"Image Status"))
    imageCreated = schema.TextLine(title=_t(u"Image Created"))
    imageUpdated = schema.TextLine(title=_t(u"Image Updated"))
    serverCount = schema.Int(title=_t(u"Server Count"))


class IServerInfo(IComponentInfo):
    serverStatus = schema.TextLine(title=_t(u"Server Status"))
    publicIps = schema.List(title=_t(u"Public IPs"))
    privateIps = schema.List(title=_t(u"Private IPs"))
    flavor = schema.Entity(title=_t(u"Server Flavor"))
    image = schema.Entity(title=_t(u"Server Image"))
    serverBackupEnabled = schema.Bool(title=_t(u"Server Backup Enabled"))
    serverBackupDaily = schema.TextLine(title=_t(u"Server Backup Daily"))
    serverBackupWeekly = schema.TextLine(title=_t(u"Server Backup Weekly"))
    hostId = schema.TextLine(title=_t(u"Host ID"))
    guestDevice = schema.Entity(title=_t(u"Guest Device"))
