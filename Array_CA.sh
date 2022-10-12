#!/bin/bash

# deklarasikan array compound assignment
distroLinuxDesktop=('BlankOn' 'Ubuntu' 'ArchLinux' 'LinuxMint')
distroLinuxServer=('UbuntuServer' 'CentOS' 'FedroServer')

# cara mengambil nilai array
echo ${distroLinuxDesktop[*]}
echo ${distroLinuxServer[*]}








